from selenium import webdriver
import time

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=options)
driver.get('https://www.facebook.com')
# driver = webdriver.Chrome()


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

# select login button
login = driver.find_elements_by_xpath("//input[@value='Log In']")[0]
login.click()
driver.get('https://www.facebook.com/events/birthdays/') 


text_boxes = driver.find_elements_by_xpath("//*[@class ='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']") 
for text_box_element in text_boxes:
	eid = str(text_box_element.get_attribute('id')) 
	text_box = driver.find_element_by_xpath('//*[@id ="' + eid + '"]') 
	text_box.send_keys("Happy Birthday!!!")

