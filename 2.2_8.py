import time
import os
from selenium import webdriver


browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/file_input.html")
    cwd = os.getcwd()
    file_path = os.path.join(cwd, 'test.txt')
    browser.find_element_by_css_selector("input[name='firstname']").send_keys("aaaaaa")
    browser.find_element_by_css_selector("input[name='lastname']").send_keys("aaaaaa")
    browser.find_element_by_css_selector("input[name='email']").send_keys("aaaaaa")
    browser.find_element_by_css_selector("input#file").send_keys(file_path)
    browser.find_element_by_css_selector("button[type='submit']").click()
finally:
    time.sleep(10)
    browser.quit()


