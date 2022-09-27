import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_extension("uBlock-Origin.crx")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) #To Stop show USB backend error

#taskkill /IM chromedriver.exe /F
driver = webdriver.Chrome(service=Service(ChromeDriverManager(path = "Drivers").install()), options = chrome_options)

EPLINK = "?ep="
epCount = 1058 + 2
pickle_path = "Episodes/conan.pickle"
show = "https://9anime.tube/watch/detective-conan/"

test = "https://www.google.com"
    
def readEpisode():
    with open('readme.txt') as f:
        lines = f.readlines()
        
def writeEpisode():
    with open('readme.txt', 'w') as f:
        f.write('readme')
    
def delay_click(xpath, delay):
    driver.find_element("xpath",xpath).click()
    time.sleep(delay)

def download(url,ep):
    driver.execute_script('''window.open(" '''+ url + EPLINK + str(ep) + '''","_blank");''')
    #driver.get(url+EPLINK+ep)    

def main():        
    if os.path.exists(pickle_path):        
        epCount = pickle.load(open(pickle_path, "rb"))
    else:
        print("Episode Data Missing")
        #pickle.dump(epCount, open(pickle_path, "wb"))    
    
    driver.get(test) # FILLER
    download(test, epCount)   

    time.sleep(1.5)

    for tabs in driver.window_handles:        
        driver.switch_to.window(driver.window_handles[-1]) #last tab
        if len(driver.window_handles) > 1: #so to keep first opened tab open    #//Check if can close final tab after download is complete
            driver.close()
    
if __name__ == "__main__":
    main()