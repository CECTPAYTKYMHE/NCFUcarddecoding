
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='C:/GIT/files/chromiumdriver/chromedriver.exe')

url = 'https://nft.bigtime.gg/explore'
# try:
driver.get(url=url)
time.sleep(5)
k = driver.page_source
print(k)
with open('c:/git/files/nft2.html', 'w+',encoding='utf-8') as f:
    f.write(k)
    f.close()
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()
    
    

