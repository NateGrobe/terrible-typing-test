#!/usr/bin/env python3

from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://www.typingtest.com/test.html?minutes=1&textfile=aesop.txt')
driver.find_elements_by_class_name('sc-bwzfXH')[-1].click()
text = driver.find_element_by_class_name('test-text-area').text
entry = driver.find_element_by_class_name('test-edit-area')
timer = driver.find_element_by_class_name('test-timer')

while timer.text != "0:00":
    for t in text:
        entry.send_keys(t)

