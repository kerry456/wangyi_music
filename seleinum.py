# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import random
import requests
import time
USER_AGENTS = {
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win026 Firefox/16.0'
}
myuser = input('输入账号：')
mypasswd = input('输入密码:')
#phantomjs_path = "/usr/local/share/phantomjs-1.9.8-linux-x86_64/bin/phantomjs"
agent = dict(DesiredCapabilities.PHANTOMJS)
agent["phantomjs.page.settings.userAgent"] =('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36')
driver = webdriver.PhantomJS(desired_capabilities=agent)
driver.get('http://www.zhaogang.com/')
driver.maximize_window()
driver.implicitly_wait(15)
print(driver.title)
#driver.get_screenshot_as_file('zhao.png')//*[@id="topbar_login_btn"]
login = driver.find_element_by_css_selector('#topbar_login_btn')
#login = driver.find_elements_by_xpath('//[@id="topbar_login_btn"]')
login.click()
driver.get_screenshot_as_file('zhao.png')
user = driver.find_element_by_css_selector('#txt_loginmobile')
user.clear()
user.send_keys(myuser)
passwd = driver.find_element_by_css_selector('')

driver.quit()
'''

import requests
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
fire_options = Options()
fire_options.add_argument('--headless')
firefox_path = '/geckodriver'
def get_cookies():
    driver = webdriver.Firefox(firefox_options=fire_options,executable_path=firefox_path)
    wait = WebDriverWait(driver,10)
    driver.get('https://music.163.com/') # 不考虑验证码的情况
    # button = wait.until(EC.presence_of_element_located((By.ID,'auto-id-qS1fBwU4JNmsQgDJ')))
    driver.find_element_by_xpath('//*[@id="srch"]').send_keys('可不可以',Keys.ENTER)
    cookies = driver.get_cookies()
    driver.close()
    c = requests.cookies.RequestsCookieJar()
    for item in cookies:
         c.set(item["name"],item["value"])
    return c

# s=requests.Session()
# s.cookies.update(c) #载入cookie
# res = s.get(url='https://music.163.com/')
#
# print(res.text)
#s.post()
if __name__ == '__main__':
    pass
#     get_cookies()

