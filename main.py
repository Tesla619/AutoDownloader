import os
import time
import pickle
import psutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Check on these pip commands
#pip install selenium
#pip install webdriver_manager

chrome_options = Options()
chrome_options.add_extension("uBlock-Origin.crx")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) #To Stop show USB backend error

#taskkill /IM chromedriver.exe /F
driver = webdriver.Chrome(service=Service(ChromeDriverManager(path = "Drivers").install()), options = chrome_options)

fail = False

EPLINK = "?ep="
epCount = 1058 + 2
pickle_path = "Episodes/conan.pickle"
show = "https://9anime.tube/watch/detective-conan/"

test = "https://www.google.com"
    
def delay_click(xpath, delay):
    driver.find_element("xpath", xpath).click()
    time.sleep(delay)

def isProcOpen(processName):
    for proc in psutil.process_iter():
        try:            
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def chooseQuality(): #try make it use computer vision to determine which button is the highest res
    try:
        delay_click("//*[@id=\"container\"]/div/table/tbody/tr[3]/td[1]/a", 0.5) #high res #change to normal xpath not full for red
        fail = False            
    except: fail = True
        
    if fail == True:
        try:
            delay_click("//*[@id=\"container\"]/div/table/tbody/tr[2]/td[1]/a", 0.5) #change to normal xpath not full for red
            fail = False
        except: pass            

def download(url,ep):
    driver.execute_script('''window.open(" '''+ url + EPLINK + str(ep) + '''","_blank");''')
    time.sleep(0.2)
    
    #Play & Pause Video
    delay_click("//*[@id=\"player\"]", 3)
    delay_click("//*[@id=\"player\"]", 0.2)
    delay_click("//*[@id=\"player\"]", 0.2)
    delay_click("//*[@id=\"player\"]", 0.2)

    #Switch Frame & Press Download
    driver.switch_to.frame("iframe-embed")
    driver.switch_to.frame("external-embed")
    delay_click("//*[@id=\"mediaplayer\"]/div[2]/div[13]/div[4]/div[2]/div[13]", 0.1) #change to normal xpath not full for red
    
    #Going to process to download video
    driver.switch_to.window(driver.window_handles[-1]) #last tab also check if reduntant
        
    chooseQuality() #selecting the link for the best resolution video
    
    try:
        delay_click("//*[@id=\"F1\"]/button", 1)        
    except: fail = True            
    
    if fail == True: #try implementing else from exception instead of this bool     //might switch flase firtst then true 
        chooseQuality()        
    else:
        try:
            delay_click("//*[@id=\"F1\"]/button", 1)                
        except: pass
        
    #Finding the link and loading it to download the video
    elements = driver.find_elements("tag name", "div")
    link = elements[8].find_elements("tag name", "a")
    driver.get(link[0].get_attribute("href"))

def main():        
    if os.path.exists(pickle_path):        
        epCount = pickle.load(open(pickle_path, "rb"))
    else:
        print("Episode Data Missing")
        #find the latest episode by incrementing for 1 till get error page doesn't exit than save number
        #pickle.dump(epCount, open(pickle_path, "wb"))    
    
    if not isProcOpen("chrome.exe"): #OR use it to close previouse chrome window since downloads are in different days
        driver.get(test) # FILLER    #might need to do it each time since scipt will run each time         
    else: pass
        
    download(test, epCount)   

    time.sleep(1.5)

    for tabs in driver.window_handles:        
        driver.switch_to.window(driver.window_handles[-1]) #last tab
        if len(driver.window_handles) > 1: #so to keep first opened tab open    #//Check if can close final tab after download is complete
            driver.close()
    
if __name__ == "__main__": #might remove
    main()