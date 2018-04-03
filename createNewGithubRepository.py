from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(input("Enter chrome web driver location"))

newRepoUrl = "https://github.com/new"

driver.get(newRepoUrl)

namefield = driver.find_element_by_name('login')
namefield.send_keys(input("Enter the user name\n"))

phonefield = driver.find_element_by_name('password')
phonefield.send_keys(input("Enter the password\n"))

signInbutton = driver.find_element_by_name('commit')
signInbutton.click()

repoName = driver.find_element_by_id('repository_name')
repoName.send_keys(input("Enter the name of new repo\n"))

sleep(1.0)

create = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/form/div[4]/button')
create.click()
