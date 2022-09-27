import os
import time
import pickle
import psutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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

def download(url,ep):
    driver.execute_script('''window.open(" '''+ url + EPLINK + str(ep) + '''","_blank");''')
    time.sleep(0.2)
    
    #Play & Pause Video
    delay_click("//*[@id=\"player\"]", 3)
    delay_click("//*[@id=\"player\"]", 0.2)
    delay_click("//*[@id=\"player\"]", 0.2)
    delay_click("//*[@id=\"player\"]", 0.2)
    


    #region Switch Frame & Press Download
    driver.switch_to.frame("iframe-embed")
    driver.switch_to.frame("external-embed")
    delay_click("//*[@id=\"mediaplayer\"]/div[2]/div[13]/div[4]/div[2]/div[13]", 100) #change to normal xpath not full for red
    
    #region Going to process to download video
    driver.switch_to.window(driver.window_handles[-1]) #last tab also check if reduntant
    
    #Choose Quality Button <--- put here chooseQuality();
    
    try:
        ChromeClick("//*[@id=\"F1\"]/button", 1000);
        
            except: (Exception)
            
                fail = True
            

            if (fail == True) #might switch flase firtst then true
            {
                chooseQuality();
            }
            else
            {
                try
                {
                    ChromeClick("//*[@id=\"F1\"]/button", 1000);
                }
                catch (Exception) { }
            }

            IList<IWebElement> elements = Driver.FindElements(By.TagName("div"));
            ReadOnlyCollection<IWebElement> link = elements[8].FindElements(By.TagName("a"));

            Driver.Navigate().GoToUrl(link[0].GetAttribute("href"));
            #endregion
    
       

def main():        
    if os.path.exists(pickle_path):        
        epCount = pickle.load(open(pickle_path, "rb"))
    else:
        print("Episode Data Missing")
        #find the latest episode by incrementing for 1 till get error page doesn't exit than save number
        #pickle.dump(epCount, open(pickle_path, "wb"))    
    
    print(isProcOpen("chrome.exe"))
    
    if not isProcOpen("chrome.exe"):
        driver.get(test) # FILLER    
    else: pass
        
    download(test, epCount)   

    time.sleep(1.5)

    for tabs in driver.window_handles:        
        driver.switch_to.window(driver.window_handles[-1]) #last tab
        if len(driver.window_handles) > 1: #so to keep first opened tab open    #//Check if can close final tab after download is complete
            driver.close()
    
if __name__ == "__main__": #might remove
    main()