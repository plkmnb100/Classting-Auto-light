from bs4 import BeautifulSoup
from selenium import webdriver
import time
while True == True:
    sigan = time.strftime('%X', time.localtime(time.time()))
    if sigan == "09:50:00":
        print("자동 출석 중입니다. 잠시만 기다려 주세요!")
        path = 'chromedriver.exe'
        driver = webdriver.Chrome(path)
        driver.get('https://oauth.classting.com/v1/oauth2/login?client_id=078b740b0390682197218af33e46b8a0&response_type=code&redirect_uri=https%3A%2F%2Fwww.classting.com%2Foauth_callback&continue_url=%2F&scope=public_profile%20private_profile%20email%20mobile&backUrl=%2Fv1%2Foauth2%2Fauthorize')

        idform = driver.find_element_by_id("auth_username")
        idform.send_keys("클래스팅 아이디를 여기에 넣어주세요")
        pwform = driver.find_element_by_id("auth_password")
        pwform.send_keys("클래스팅 비밀번호를 여기에 넣어주세요")
        time.sleep(0.5)
        driver.find_element_by_class_name("btn").click()
        time.sleep(10)
        driver.find_element_by_class_name("btn-litup").click()

    else:
        print("9시 50분까지 대기중입니다.. 현재시각 " + sigan)