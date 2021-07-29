from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")
x_element = browser.find_element_by_css_selector("span.nowrap#input_value")
x = x_element.text
y = calc(x)
answer_form = browser.find_element_by_css_selector("#answer.form-control")
answer_form.send_keys(y)
browser.find_element_by_css_selector("#robotCheckbox").click()
browser.find_element_by_css_selector("#robotsRule").click()
submit_button = browser.find_element_by_css_selector("button[type=submit]")
submit_button.click()
time.sleep(10)
browser.quit()
