from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
f = open("27-a.txt")
try:
    browser.get("http://suninjuly.github.io/execute_script.html")
    x = int(browser.find_element_by_css_selector("#input_value").text)
    y = calc(x)
    answer_form = browser.find_element_by_css_selector("input#answer")
    answer_form.send_keys(y)
    browser.find_element_by_css_selector("#robotCheckbox").click()
    submit_button = browser.find_element_by_css_selector("button[type=submit]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    browser.find_element_by_css_selector("#robotsRule").click()
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
