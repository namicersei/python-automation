from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(input("Enter chrome web driver location"))

formUrl = "http://localhost/form-submission-mysql-php/html/index.html"

driver.get(formUrl);

email = driver.find_element_by_id("email")
phone = driver.find_element_by_id("phone")
password = driver.find_element_by_id("pwd")
submit = driver.find_element_by_id("button-btm")

email.send_keys(input("Enter the email address\n"))
phone.send_keys(input("Enter the phone no\n"))
password.send_keys(input("Enter the password\n"))

submit.click()
