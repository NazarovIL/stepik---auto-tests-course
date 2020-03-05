from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element_by_name("firstname")
    input_name.send_keys("Igor")
    input_lastname = browser.find_element_by_name("lastname")
    input_lastname.send_keys("Petrov")
    input_email = browser.find_element_by_name("email")
    input_email.send_keys("123@mail.ru")

    element = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '2-2.txt')
    element.send_keys(file_path)

    button_submit = browser.find_element_by_tag_name("button")
    button_submit.click()
finally:
    time.sleep(10)
    browser.quit()