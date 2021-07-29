from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x = browser.find_element_by_css_selector("img#treasure").get_attribute("valuex")
    y = calc(x)
    answer_form = browser.find_element_by_css_selector("input#answer")
    answer_form.send_keys(y)
    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("#robotsRule").click()
    submit_button = browser.find_element_by_css_selector("button[type=submit]")
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
