# crawling/test_selenium.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_driver():
    # ──── 크롬 옵션 설정 ────
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/113.0.0.0 Safari/537.36"
    )
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # WebDriver 인스턴스 생성 & 자동화 탐지 우회
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    try:
        # 1. 사람인 메인 페이지 열기
        driver.get("https://www.saramin.co.kr")
        print("[INFO] 사람인 페이지 로딩됨")
        time.sleep(3)

        # 2. 검색 버튼 클릭 (입력창 표시를 위해)
        btn_search = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_search"))
        )
        btn_search.click()
        print("[INFO] 검색 버튼 클릭 성공")
        time.sleep(1)

        # 3. 검색 입력창 로딩 대기
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ipt_keyword_recruit"))
        )
        print("[INFO] 검색 입력창 감지됨, placeholder:", search_input.get_attribute("placeholder"))

        # 4. 입력창 클릭 후 키워드 입력 ─
        # 입력창이 활성화되어 있지 않을 수 있어서 click() 추가
        search_input.click()
        time.sleep(0.5)
        search_input.send_keys("로봇 개발자")
        search_input.send_keys("\n")
        print("[INFO] 검색어 입력 및 엔터 완료")
        time.sleep(4)  # 검색 결과가 로드될 시간 확보

        # 5. 첫 번째 채용 공고 제목 가져오기
        first_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.item_recruit h2.job_tit a"))
        )
        print("[RESULT] 첫 번째 공고 제목:", first_title.text.strip())

    except Exception as e:
        print("[ERROR]", e)
        # 페이지 소스를 저장해두면 차단 여부 등 디버깅에 도움이 됩니다.
        with open("error_page.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("[DEBUG] 에러 발생 시 페이지 저장됨: error_page.html")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_driver()
