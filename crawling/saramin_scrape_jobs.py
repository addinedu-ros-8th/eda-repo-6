# -*- coding: utf-8 -*-
"""
saramin_scrape_jobs.py

▶        
- Search Saramin for job posts matching a keyword (default: “·로봇 개발자")
- Collect multi-page job cards
- Visit each job detail page for extended info (career, education, salary, etc)
- Export CSV to: data/raw/saramin_jobs.csv
"""

import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


# WebDriver init

def init_driver(headless: bool = False) -> webdriver.Chrome:
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


# 상세페이지 정보 추출
def get_detail_info(driver, url):
    try:
        driver.get(url)
        time.sleep(1.5)
        soup = BeautifulSoup(driver.page_source, "html.parser")

        def get_text(dt_name):
            try:
                dt = soup.select_one(f'dl > dt:contains("{dt_name}")')
                dd = dt.find_next_sibling("dd") if dt else None
                return dd.get_text(strip=True) if dd else ""
            except:
                return ""

        return {
            "career": get_text("\uacbd\ub825"),
            "education": get_text("\ud559\ub825"),
            "employment": get_text("\uadfc\ubb34\ud615\ud0dc"),
            "preferred": get_text("\uc6b0\ub300\uc0ac\ud56d"),
            "salary_detail": get_text("\ae08\uc6d0"),
            "work_days": get_text("\uadfc\ubb34\uc694\uc77c"),
            "work_place": get_text("\uadfc\ubb34\uc9c0\uc5ed")
        }
    except Exception as e:
        print(f"[WARN] 상세 페이지 파싱 실패: {e}")
        return {}


# Main crawl func
def scrape_saramin(keyword="\ub85c\ubcfc \uac1c\ubc1c\uc790", max_pages=5,
                   output_path="data/raw/saramin_jobs.csv", headless=False):
    driver = init_driver(headless=headless)
    jobs = []
    base_url = "https://www.saramin.co.kr"

    try:
        search_url = (
            f"{base_url}/zf_user/search/recruit?search_area=main&search_done=y"
            f"&search_optional_item=n&searchType=search&searchword={keyword}"
        )

        for page in range(1, max_pages + 1):
            driver.get(f"{search_url}&recruitPage={page}")
            time.sleep(2)

            soup = BeautifulSoup(driver.page_source, "html.parser")
            job_cards = soup.select("div.item_recruit")
            if not job_cards:
                print(f"[INFO] 페이지 {page} 공고 없음")
                break

            print(f"[INFO] 페이지 {page}에서 {len(job_cards)}건 수집 중...")

            for card in job_cards:
                try:
                    title_tag = card.select_one("h2.job_tit a")
                    company_tag = card.select_one("div.area_corp strong.corp_name a")
                    info_tags = card.select("div.job_condition span")

                    title = title_tag.get_text(strip=True) if title_tag else ""
                    company = company_tag.get_text(strip=True) if company_tag else ""
                    salary = location = ""

                    for tag in info_tags:
                        txt = tag.get_text(strip=True)
                        if "만원" in txt or "연봉" in txt:
                            salary = txt
                        if any(loc in txt for loc in ["서울", "경기", "부산", "인천", "대전", "대구", "광주"]):
                            location = txt

                    detail_url = base_url + title_tag['href'] if title_tag and 'href' in title_tag.attrs else None
                    detail_info = get_detail_info(driver, detail_url) if detail_url else {}

                    jobs.append({
                        "title": title,
                        "company": company,
                        "salary": salary,
                        "location": location,
                        **detail_info
                    })

                except Exception as e:
                    print(f"[WARN] 공고 파싱 실패: {e}")
                    continue

            time.sleep(1)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, mode="w", encoding="utf-8-sig", newline="") as f:
            fieldnames = [
                "title", "company", "salary", "location",
                "career", "education", "employment", "preferred",
                "salary_detail", "work_days", "work_place"
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for job in jobs:
                writer.writerow(job)

        print(f"[SARAMIN] 총 {len(jobs)}건 저장 → {output_path}")

    except Exception as e:
        print(f"[ERROR] 크롤링 도중 예외 발생: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    scrape_saramin(keyword="로봇 개발자", max_pages=5,
                   output_path="data/raw/saramin_jobs.csv", headless=False)
