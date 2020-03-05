from selenium import webdriver
import time
import math
def result(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()
    #time.sleep(1)
    confirm = browser.switch_to.alert
    confirm.accept()
    #time.sleep(1)
    x = browser.find_element_by_id("input_value").text
    y = result(x)
    input_result = browser.find_element_by_id("answer")
    input_result.send_keys(y)
    button_submit = browser.find_element_by_tag_name("button")
    button_submit.click()
finally:
    time.sleep(10)
    browser.quit()