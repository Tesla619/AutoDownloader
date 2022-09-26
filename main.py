import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_extension("uBlock-Origin.crx")

#Update To Do: if condition for install if first time or driver needs updating
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

EPLINK = "?ep="
anime1 = "https://9anime.tube/watch/detective-conan/"
anime2 = "https://9anime.tube/watch/boruto-naruto-next-generations/"
anime3 = "https://9anime.tube/watch/one-piece-episode-of-merry-mou-hitori-no-nakama-no-monogatari/"
anime4 = "https://9anime.tube/watch/pokemon-2019/"

def custom_Ep_fullXpath(ep):
    return """/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/ul/li["""+ str(ep) +"""]/a"""

def custom_Ep_Xpath(ep):
    return """//*[@id="list-eps"]/li["""+str(ep)+"""]/a"""

def delay_click(xpath, delay):
    driver.find_element("xpath",xpath).click
    time.sleep(delay)

def download(url,ep):
    #driver.get(url+EPLINK+ep)
    #print(url+EPLINK+str(ep))
    driver.get(anime1)

#driver.switch_to.frame
#driver.switch_to.window

#driver.get(anime1) FILLER 

download(anime1,1)
#driver.switch_to.frame()
#delay_click(custom_Ep_Xpath(1059), 1)
delay_click(custom_Ep_fullXpath(1059), 1)