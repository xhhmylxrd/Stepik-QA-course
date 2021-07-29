from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.implicitly_wait(10)
    WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()
    x = browser.find_element_by_css_selector("#input_value").text
    browser.find_element_by_css_selector("#answer").send_keys(calc(x))
    browser.find_element_by_css_selector("button[type='submit']").click()
    final_answer = browser.switch_to.alert.text.split()[-1]
    print(final_answer)
finally:
    browser.quit()
