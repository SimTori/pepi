
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import json
import schedule
import time

with open("user.json", "r") as data:
    user = json.load(data)
    

ID = user['ID']
PW = user['PW']


URL = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%95%84%ED%82%A4%EC%97%90%EC%9D%B4%EC%A7%80&oquery=%EC%95%84%ED%82%A4%EC%97%90%EC%9E%8A&tqi=U%2F5y4sp0J14sstjEaKossssssMZ-077460'


def start():
    options = Options()
    options.headless = False

    driver = webdriver.Chrome(executable_path='./chromedriver', options=options)
    driver.implicitly_wait(30)

    driver.get(url=URL)


    driver.find_element_by_xpath('//*[@id="main_pack"]/section[1]/div[2]/div[1]/div/div[2]/dl/div[5]/dd/a[2]').click()


    driver.switch_to.window(driver.window_handles[1])

    # 아키에이지 로그인 페이지
    print(driver.current_url)
    if "promotion" in driver.current_url:
        print("진입", driver.current_url)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/h1/a').click()

    driver.find_element_by_css_selector('#portal-gnb > div.account-util > a').click()


    # 아키에이지 로그인
    ac_login = driver.find_element_by_id('id_field')
    ac_login.send_keys(ID)

    ac_login = driver.find_element_by_id('pw_field')
    ac_login.send_keys(PW)

    xpath = """//*[@id="loginButton"]"""
    driver.find_element_by_xpath(xpath).click()

    # 아이케이지 페피 출석 페이지
    xpath = """//*[@id="__5"]/a"""
    driver.find_element_by_xpath(xpath).click()
    time.sleep(2)

    # 아키에이지 페피 출석 버튼
    driver.switch_to_frame("eventFrame")
    driver.find_element_by_css_selector('body > div.event-wrap > div.section3 > div > a.link-gift').click()
    driver.quit()
 
 
schedule.every().day.at("00:10").do(start)
schedule.every().day.at("09:10").do(start)
schedule.every().day.at("17:10").do(start)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)