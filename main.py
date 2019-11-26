from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
options.add_argument("--headless")  
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=options)
driver.get('https://www.facebook.com')

with open('credentials.txt', 'r') as myfile: 
	cred = myfile.read().split('\n')
	username = cred[0]
	password = cred[1]
	message = cred[2]
def post(username, password, message):
	# select html element for username
	text_box = driver.find_element_by_id('email')
	# enter username
	text_box.send_keys(username)

	# select html element for password
	text_box = driver.find_element_by_id('pass')
	# enter password
	text_box.send_keys(password)

	# select login button
	login = driver.find_elements_by_xpath("//input[@value='Log In']")[0]
	login.click()

	# waits for 35 sec for 2 factor authentication
	time.sleep(35)

	driver.get('https://www.facebook.com/events/birthdays/') 

	#get all the text boxes
	text_boxes = driver.find_elements_by_xpath("//*[@class ='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']") 
	# iterate over text boxes and write message
	for text_box_element in text_boxes:
		eid = str(text_box_element.get_attribute('id'))
		text_box = driver.find_element_by_xpath('//*[@id ="' + eid + '"]') 
		# enter message
		text_box.send_keys(message)
		# press enter
		text_box.send_keys(Keys.RETURN) 
post(username, password, message)

