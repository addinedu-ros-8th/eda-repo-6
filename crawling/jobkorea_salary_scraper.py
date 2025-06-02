import re
import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException


def init_driver(headless: bool = True) -> webdriver.Chrome:
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 Chrome/113.0.0.0 Safari/537.36"
    )
    driver = webdriver.Chrome(options=options)
    # webdriver 속성 숨겨서 탐지 회피
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.implicitly_wait(1)
    return driver


def search_jobkorea_salary(company_name: str, driver: webdriver.Chrome) -> str:
    """
    company_name: CSV에 들어있는 회사명 (예: '(주)베스텔라랩')
    driver: init_driver()로 생성된 WebDriver
    반환값: 평균 연봉 문자열(예: '3887만원') 또는 'N/A'
    """
    try:
        # 1) "(주)"나 "주식회사 " 같은 접두어 제거
        simple_name = re.sub(r'^\(주\)|^주식회사\s*', '', company_name).strip()
        print(f"검색어 (prefix 제거): '{simple_name}'")

        # 2) 검색 페이지 열기
        search_url = f"https://www.jobkorea.co.kr/Search/?stext={simple_name}"
        driver.get(search_url)
        print(f"검색 페이지 열림: {search_url}")

        # 3) 검색 결과: “기업정보” 탭 버튼 클릭
        try:
            corp_tab = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[.//span[text()='기업정보']]")
                )
            )
            driver.execute_script("arguments[0].click();", corp_tab)
            print("‘기업정보’ 탭 클릭 완료")
        except TimeoutException:
            print(f"[WARN] {company_name} - ‘기업정보’ 탭을 찾지 못함, N/A 처리")
            return "N/A"

        # 4) “기업정보” 탭 클릭 후 잠시 대기 (탭 내부가 렌더링될 때까지)
        time.sleep(1.0)

        # 5) 회사 상세 페이지 링크(a[href*='/Recruit/Co_Read/C/']) 선택 → href 추출 → driver.get(detail_url)
        try:
            elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/Recruit/Co_Read/C/']"))
            )
            detail_url = elem.get_attribute("href")
            print(f"상세 페이지 URL 확인: {detail_url}")
            driver.get(detail_url)
        except TimeoutException:
            print(f"[WARN] {company_name} 검색 결과 없음 → N/A")
            return "N/A"

        # 6) 상세 페이지 로드 대기 (필요 시 특정 요소 확인)
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("/Recruit/Co_Read/C/")
            )
            print(f"상세 페이지 로드 완료: {driver.current_url}")
        except TimeoutException:
            print(f"[WARN] {company_name} 상세 페이지 로드 지연 → N/A")
            return "N/A"

        # 7) 현재 URL에서 "/Recruit/Co_Read/C/" → "/Recruit/Salary/" 치환
        current = driver.current_url
        if "/Recruit/Co_Read/C/" in current:
            salary_url = current.replace("/Recruit/Co_Read/C/", "/Recruit/Salary/")
            print(f"연봉 페이지 URL 생성: {salary_url}")
        else:
            print(f"[WARN] {company_name} 상세 페이지 URL 포맷 예상과 다름 → N/A")
            return "N/A"

        # 8) 연봉 페이지로 이동
        driver.get(salary_url)

        # 9) 연봉 페이지 로드 대기 (’전체 평균 연봉’ 영역)
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.salary-table-item.salary-table-average")
                )
            )
            print(f"연봉 페이지 로드 완료: {driver.current_url}")
        except TimeoutException:
            print(f"[WARN] {company_name} 연봉 페이지 로드 지연 → N/A")
            return "N/A"

        # 10) 평균 연봉 추출
        try:
            value_elem = driver.find_element(
                By.CSS_SELECTOR,
                "div.salary-table-item.salary-table-average div.salary div.value"
            )
            unit_elem = driver.find_element(
                By.CSS_SELECTOR,
                "div.salary-table-item.salary-table-average div.salary div.unit"
            )
            # “3,887” → “3887”, 단위 “만원”
            value_text = value_elem.text.strip().replace(",", "")
            unit_text = unit_elem.text.strip()
            avg_salary = f"{value_text}{unit_text}"
            print(f"평균 연봉 추출 성공: {avg_salary}")
            return avg_salary
        except Exception:
            print(f"[WARN] {company_name} 평균 연봉 요소 추출 실패 → N/A")
            return "N/A"

    except Exception as e:
        print(f"[ERROR] {company_name} 예외 발생 → {e}")
        return "N/A"


def scrape_salary_for_csv(input_csv: str, headless: bool = True):
    df = pd.read_csv(input_csv)
    df["salary"] = df["salary"].astype(str)

    driver = init_driver(headless=headless)

    try:
        for i, row in df.iterrows():
            company = row["company"]
            # 이미 “만원” 단위 정보가 있으면 건너뛰기
            if pd.notnull(row["salary"]) and "만원" in row["salary"]:
                print(f"[SKIP] {i+1}/{len(df)} - {company} (이미 연봉 있음)")
                continue

            print(f"[INFO] {i+1}/{len(df)} - {company} 연봉 검색 중...")
            avg_salary = search_jobkorea_salary(company, driver)
            df.at[i, "salary"] = avg_salary
            print(f"[RESULT] {company} → {avg_salary}\n")
            time.sleep(random.uniform(1.2, 2.5))

    finally:
        driver.quit()

    df.to_csv(input_csv, index=False, encoding="utf-8-sig")
    print(f"[DONE] 연봉 정보 업데이트 완료 → {input_csv}")


if __name__ == "__main__":
    scrape_salary_for_csv("data/raw/saramin_jobs.csv", headless=False)
