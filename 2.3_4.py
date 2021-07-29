import time
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element_by_css_selector("button[type='submit']").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_css_selector("#input_value").text
    browser.find_element_by_css_selector("#answer").send_keys(calc(x))
    browser.find_element_by_css_selector("button[type='submit']").click()
    final_answer = browser.switch_to.alert.text.split()[-1]
    print(final_answer)
finally:
    browser.quit()


