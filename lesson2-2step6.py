from selenium import webdriver
import time
import math

def result(x):
    return math.log(abs(12*math.sin(x)))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id("input_value").text)
    y = str(result(x))

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("arguments[0].scrollIntoView();", radio)
    radio.click()

    button_submit = browser.find_element_by_tag_name("button")
    button_submit.click()


finally:
    time.sleep(10)
    browser.quit()