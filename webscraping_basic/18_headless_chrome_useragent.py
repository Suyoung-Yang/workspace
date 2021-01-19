import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


"""

"""

from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-siez=1920x1080")
# headless 사용시 user-agent 입력이 필요할 수 있음.
options.add_argument("user-agent =Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

#
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()
