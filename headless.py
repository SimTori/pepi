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
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('disable-gpu')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('lang=ko_KR')
    prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
    options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(executable_path='./chromedriver', options=options)
    driver.implicitly_wait(30)
    driver.get(url=URL)


    # 아키에이지 공식홈페이지 클릭
    # oh = driver.find_element_by_css_selector('#main_pack > section.sc_new.cs_common_module._cs_newgame.case_normal.color_10 > div.cm_content_wrap.cm_game > div:nth-child(1) > div > div.detail_info > dl > div:nth-child(5) > dd > a:nth-child(1)')
    # oh.click()
    driver.find_element_by_xpath('//*[@id="main_pack"]/section[1]/div[2]/div[1]/div/div[2]/dl/div[5]/dd/a[2]').click()
    driver.switch_to.window(driver.window_handles[1])

    if "promotion" in driver.current_url:

        driver.find_element_by_xpath('/html/body/div[2]/div[1]/h1/a').click()
    # 아키에이지 로그인 프로세스
    driver.find_element_by_css_selector('#portal-gnb > div.account-util > a').click()

    ac_login = driver.find_element_by_id('id_field')
    ac_login.send_keys(ID)

    ac_login = driver.find_element_by_id('pw_field')
    ac_login.send_keys(PW)

    xpath = """//*[@id="loginButton"]"""
    driver.find_element_by_xpath(xpath).click()

    xpath = """//*[@id="account_util"]/div[1]/div/span/a/strong"""
    print(driver.find_element_by_xpath(xpath).text)

    # 페피출석 페이지 
    xpath = """//*[@id="__5"]/a"""
    driver.find_element_by_xpath(xpath).click()
    print("출석페이지 로드")

    # iframe 전환
    driver.switch_to_frame("eventFrame")
    print("iframe")

    # 출석 버튼 클릭
    print(driver.current_url)
    element = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/a[3]")
    driver.execute_script("arguments[0].click();", element)

    driver.save_screenshot("success1.png")

    driver.quit()


schedule.every().day.at("00:10").do(start)
schedule.every().day.at("09:10").do(start)
schedule.every().day.at("17:10").do(start)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)