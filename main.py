import os
import time
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
anime1 = "https://9anime.tube/watch/detective-conan/"
anime2 = "https://9anime.tube/watch/boruto-naruto-next-generations/"
anime3 = "https://9anime.tube/watch/one-piece-episode-of-merry-mou-hitori-no-nakama-no-monogatari/"
anime4 = "https://9anime.tube/watch/pokemon-2019/"

test = "https://www.google.com"

#Gather episode numbers from memory / txt file
epCount1 = 1058 + 2 # +2 cause fuck up from 9anime naming
epCount2 =  269
epCount3 = 1035
epCount4 =  127

def Ideas():
    """Ideas:
    1) Make show and episodes in a 2 arrays (maybe 2D, most likley would be wasteful)
    """
    
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

driver.get(test) # FILLER
download(test, epCount1)   

time.sleep(1.5)

for tabs in driver.window_handles:        
    driver.switch_to.window(driver.window_handles[-1]) #last tab
    if len(driver.window_handles) > 1: #so to keep first opened tab open    #//Check if can close final tab after download is complete
        driver.close()
        
""" Pickling Example
import os
#import cPickle as pickle
import pickle

pickle_filepath = "/path/to/picklefile.pickle"

if not os.path.exists(pickle_filepath):
    # Read data set from disk
    with open('mydata', 'r') as in_handle:
        mytext = in_handle.read()
    # Extract relevant results from data set
    mydata = parse_data(mytext)
    result = initial_operations(mydata)
    with open(pickle_filepath, 'w') as pickle_handle:
        pickle.dump(result, pickle_handle)
else:
    with open(pickle_filepath) as pickle_handle:
        result = pickle.load(pickle_handle)
"""