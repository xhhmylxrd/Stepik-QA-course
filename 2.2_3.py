import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import math
browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/selects2.html")
    s = browser.find_element_by_css_selector("span#num1").text
    s1 = browser.find_element_by_css_selector("span#num2").text
    n = str(int(s)+int(s1))
    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(n)
    browser.find_element_by_css_selector("button[type='submit']").click()
finally:
    time.sleep(10)
    browser.quit()
