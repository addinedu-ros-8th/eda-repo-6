# -*- coding: utf-8 -*-
"""
scrape_jobs.py

사람인에서 '로봇 개발자' 키워드로 여러 페이지의 채용 공고를 수집하고 CSV로 저장합니다.
- User-Agent 위장
- 자동화 탐지 우회
- Selenium + BeautifulSoup 병행 사용
"""

import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def init_driver(headless: bool = False) -> webdriver.Chrome:
    """Chrome WebDriver를 초기화하여 반환합니다."""
    options = Options()

    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    )
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver


def parse_jobs_with_soup(driver, page: int):
    """Selenium driver에서 HTML을 가져와 BeautifulSoup으로 파싱"""
    soup = BeautifulSoup(driver.page_source, "html.parser")
    job_cards = soup.select("div.item_recruit")

    if not job_cards:
        print(f"[INFO] 페이지 {page} 공고 없음")
        return []

    job_list = []

    for card in job_cards:
        try:
            title_tag = card.select_one("h2.job_tit a")
            company_tag = card.select_one("div.area_corp strong.corp_name a")
            info_tags = card.select("div.job_condition span")

            title = title_tag.get_text(strip=True) if title_tag else "제목 없음"
            company = company_tag.get_text(strip=True) if company_tag else "회사 없음"

            salary = ""
            location = ""
            for tag in info_tags:
                txt = tag.get_text(strip=True)
                if "만원" in txt or "연봉" in txt:
                    salary = txt
                if any(loc in txt for loc in ["서울", "경기", "부산", "인천", "대전", "대구", "광주"]):
                    location = txt

            job_list.append({
                "title": title,
                "company": company,
                "salary": salary,
                "location": location
            })

        except Exception as e:
            print(f"[WARN] soup 파싱 실패: {e}")
            continue

    print(f"[INFO] 페이지 {page}에서 {len(job_list)}건 수집 완료")
    return job_list


def scrape_saramin(
    keyword: str = "로봇 개발자",
    max_pages: int = 5,
    output_path: str = "data/raw/saramin_jobs.csv",
    headless: bool = False
) -> None:
    """사람인 크롤링 메인 함수"""
    driver = init_driver(headless=headless)
    jobs = []

    try:
        base_url = "https://www.saramin.co.kr"
        search_url = (
            f"{base_url}/zf_user/search/recruit?"
            f"search_area=main&search_done=y&search_optional_item=n"
            f"&searchType=search&searchword={keyword}"
        )

        for page in range(1, max_pages + 1):
            url = f"{search_url}&recruitPage={page}"
            try:
                driver.get(url)
            except Exception as e:
                print(f"[ERROR] 페이지 로드 실패 (page {page}): {e}")
                break

            time.sleep(2)
            job_list = parse_jobs_with_soup(driver, page)
            if not job_list:
                break

            jobs.extend(job_list)
            time.sleep(1)

        # 결과 저장
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, mode="w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "company", "salary", "location"])
            writer.writeheader()
            for job in jobs:
                writer.writerow(job)

        print(f"[SARAMIN] 총 {len(jobs)}건 저장 → {output_path}")

    except Exception as e:
        print(f"[ERROR] 크롤링 도중 예외 발생: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    scrape_saramin(
        keyword="로봇 개발자",
        max_pages=5,
        output_path="data/raw/saramin_jobs.csv",
        headless=False
    )
