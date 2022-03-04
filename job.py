from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# enable browser logging
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(executable_path='d:/GIT/files/chromiumdriver/chromedriver.exe')

# load the desired webpage
driver.get('d:/git/firebase_get_ID-token.html')
time.sleep(3)
# print messages
print(driver.__str__)
