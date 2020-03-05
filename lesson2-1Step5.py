from selenium import webdriver

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

element = browser.find_element_by_id("input_value")
x = element.text
y = calc(x)
input_answer = browser.find_element_by_id("answer")
input_answer.send_keys(y)

input_checkbox = browser.find_element_by_id("robotCheckbox")
input_checkbox.click()

input_radio = browser.find_element_by_id("robotsRule")
input_radio.click()

button1 = browser.find_element_by_tag_name("button")
button1.click()

