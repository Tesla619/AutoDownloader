import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_extension("uBlock-Origin.crx")

#taskkill /IM chromedriver.exe /F
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=Service(ChromeDriverManager(path = "Drivers").install()), options = chrome_options)

EPLINK = "?ep="
anime1 = "https://9anime.tube/watch/detective-conan/"
anime2 = "https://9anime.tube/watch/boruto-naruto-next-generations/"
anime3 = "https://9anime.tube/watch/one-piece-episode-of-merry-mou-hitori-no-nakama-no-monogatari/"
anime4 = "https://9anime.tube/watch/pokemon-2019/"

def custom_Ep_Xpath(ep):
    return """//*[@id="list-eps"]/li["""+str(ep)+"""]/a"""

def delay_click(xpath, delay):
    driver.find_element("xpath",xpath).click()
    time.sleep(delay)

def download(url,ep):
    #driver.get(url+EPLINK+ep)
    #print(url+EPLINK+str(ep))
    driver.get(anime1)

#driver.switch_to.frame
#driver.switch_to.window

#driver.get(anime1) FILLER 