from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait
import time 
phones=["8009083498","9650023649","9721859952","8009083498"]
# from selenium.webdriver import Chromefrom selenium.webdriver.chrome.options 
# import Options

browser = Chrome("./chromedriver")
browser.maximize_window()
wait = WebDriverWait(browser, 30)

unsucess_phone = []
success_phone = []
first = True
for phone in phones:

	browser.get("https://api.whatsapp.com/send?phone=91{}".format(phone))
	# try:
	# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	# user.click()
	# if first:
	# 	first = False
	# else:
	# 	time.sleep(10)


	try:
		wait.until(EC.visibility_of_element_located((By.ID, "action-button")))
		msg = browser.find_element_by_id("action-button")
		msg.click()
		
	except Exception as e:
		print e
		unsucess_phone.append(phone)
		continue
		


	try:
		wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "action__link")))
		use_whatsapp = browser.find_element_by_class_name("action__link")
		use_whatsapp.click()
	except Exception as e:
		print e
		unsucess_phone.append(phone)
		continue
	

	try:
		wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_3u328")))
		msg_box = browser.find_element_by_class_name('_3u328')
		msg_box.send_keys("Have a good day... or good night right now")
	except Exception as e:
		print e
		unsucess_phone.append(phone)
		continue


	try:
		time.sleep(10)
		wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_3M-N-")))
		send = browser.find_element_by_class_name('_3M-N-')
		send.click()
	except Exception as e:
		print e
		unsucess_phone.append(phone)
		continue
	time.sleep(5)
	success_phone.append(phone)

time.sleep(5)

browser.close()

print "====Task Complete===="
print "SUCCESS: {} candidate(s)".format(len(success_phone))
print success_phone
print "FAILED: {} candidate(s)".format(len(unsucess_phone))
print unsucess_phone



