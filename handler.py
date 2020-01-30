import os
import json
import urllib.parse as urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def handler(event, context):
    run_scrapper('https://www.yelp.com/biz/studs-new-york')


def run_scrapper(business_url):
    dir = os.path.dirname(os.path.abspath(__file__))
    try:
        driver_path = dir + "/bin/chromedriver"
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--single-process')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.binary_location = dir + "/bin/headless-chromium"
        driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)
        driver.get(business_url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        items = soup.find("div", class_="main-content-wrap--full").find_all("li")
        print(len(items))
    except Exception as e:
        print(e)

    return {
        "business_name": business_url
    }


if __name__ == "__main__":
    ret = run_scrapper('https://www.yelp.com/biz/studs-new-york')
    print(ret)
