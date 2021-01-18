import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser= webdriver.Chrome()
# browser.maximize_window() # 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click() # 이번달
# browser.find_elements_by_link_text("28")[0].click() # 이번달

# 다음달 27일, 28일 선택
browser.find_elements_by_link_text("27")[1].click() # 다음달
browser.find_elements_by_link_text("28")[1].click() # 다음달

# 제주도 클릭
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]/div/span").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click() #항공권 검색 클릭

# 첫번째 결과 출력
"""
화면 로딩 시간 때문에, 검색 하고 바로 출력하려하면 문제가 발생하게 됨.

방법은 2가지 인데, 1. sleep, 2. element 나올 때 까지 기다리기.



"""
# 10초를 기다리는데, 해당 내용이 나오면 진행, XPATH 조건으로 해당 XPATH 나오면 진행
try:
    elem = WebDriverWait(browser, 200).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit()

# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)
