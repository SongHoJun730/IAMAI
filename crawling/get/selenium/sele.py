from selenium import webdriver
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

# selenium의 webdriver로 크롬 브라우저를 실행한다
driver = webdriver.Chrome("C:/Users/syslab/Desktop/crawling/get/selenium/chromedriver/chromedriver.exe")


# "Google"에 접속한다
driver.get("http://www.google.co.kr")

# 페이지의 제목을 체크하여 'Google'에 제대로 접속했는지 확인한다
assert "Google" in driver.title
# assert "Naver" in driver.title

# 검색 입력 부분에 커서를 올리고
# 검색 입력 부분에 다양한 명령을 내리기 위해 elem 변수에 할당한다
elem = driver.find_element_by_name("q")

# 입력 부분에 default로 값이 있을 수 있어 비운다
elem.clear()

# 검색어를 입력한다
elem.send_keys("강아지상 얼굴")

# 검색을 실행한다
elem.submit()

# 검색이 제대로 됐는지 확인한다
assert "No results found." not in driver.page_source
a = driver.find_element_by_xpath('//*[@id="dimg_19"]')
print(a)

a.screenshot("test.png")

# time.sleep(1)
# time.sleep(1)
# 브라우저를 종료한다
# driver.close()
