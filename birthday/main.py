from selenium import webdriver
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get('https://www.facebook.com')

username = "harsh.sinha@students.iiit.ac.in"
with open('pass', 'r') as myfile: 
	password = myfile.read().replace('\n', '') 
# select html element for username
text_box = driver.find_element_by_id('email')
# enter username
text_box.send_keys(username)
# select html element for password
text_box = driver.find_element_by_id('pass')
# enter password
text_box.send_keys(password)
python_button = driver.find_elements_by_xpath("//input[@value='Log In']")[0]
python_button.click()