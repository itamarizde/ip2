from selenium import webdriver
from getpass import getpass

usr = input('Enter your username or email id : ')
pwd = getpass('Enter your password : ')

driver = webdriver.chrome()
driver.get('https://facebook.com/')

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_id('u_0_a')
login_btn.submit()