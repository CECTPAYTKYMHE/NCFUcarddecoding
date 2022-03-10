import logging

from selenium import webdriver

def get_browser_log_entries(driver):
    """get log entreies from selenium and add to python logger before returning"""
    loglevels = { 'NOTSET':0 , 'DEBUG':10 ,'INFO': 20 , 'WARNING':30, 'ERROR':40, 'SEVERE':40, 'CRITICAL':50}

    #initialise a logger
    browserlog = logging.getLogger("chrome")
    #get browser logs
    slurped_logs = driver.get_log('browser')
    for entry in slurped_logs:
        #convert broswer log to python log format
        rec = browserlog.makeRecord("%s.%s"%(browserlog.name,entry['source']),loglevels.get(entry['level']),'.',0,entry['message'],None,None)
        rec.created = entry['timestamp'] /1000 # log using original timestamp.. us -> ms
        try:
            #add browser log to python log
            browserlog.handle(rec)
        except:
            print(entry)
    #and return logs incase you want them
    return slurped_logs

def demo():
    caps = webdriver.DesiredCapabilities.CHROME.copy()
    caps['goog:loggingPrefs'] = { 'browser':'ALL' }
    driver = webdriver.Chrome(executable_path='C:/GIT/files/chromiumdriver/chromedriver.exe',desired_capabilities=caps )

    driver.get("C:/GIT/firebase_get_ID-token.html")

    consolemsgs = get_browser_log_entries(driver)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)7s:%(message)s')
    logging.info("start")
    demo()
    logging.info("end")