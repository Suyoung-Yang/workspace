"""
크롬 버전: 87.0.4280.141



"""
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from selenium import webdriver
import time

browser = webdriver.Chrome() # 현재 폴더에 없는 경우에는 Chromedriver 위치를 적어줘야한다

#1. 네이버 이동
browser.get("http://naver.com/") # 해당 웹사이트로 이동..ㅠ

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id/pw 입력

browser.find_element_by_id("id").send_keys("thsus76")

browser.find_element_by_id("pw").send_keys("1234")

# # 4. 로그인 버튼 클릭
# browser.find_element_by_id("log.login").click()
# time.sleep(3)
# 5. id를 새로 입력하기.
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("thsus")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
browser.close() # 해당 탭만 종료
browser.quit() # 전체 종료
