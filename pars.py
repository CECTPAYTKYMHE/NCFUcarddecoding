from gettext import find
from xml.dom.minidom import Element
from selenium import webdriver as wd
import time

url = 'https://instagram.com'
options = wd.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36')
driver = wd.Chrome(executable_path='C:/GIT/files/chromiumdriver/chromedriver.exe',options=options)

try:
    driver.get(url=url)
    time.sleep(5)
 
    login_input = driver.find_element_by_name('username')
    login_input.click()
    login_input.send_keys('89187591088')
    time.sleep(30)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
