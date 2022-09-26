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

def custom_EP_XML(ep):
    return """//*[@id="list-eps"]/li["""+str(ep)+"""]/a"""

def download(url,ep):
    #driver.get(url+EPLINK+ep)
    print(url+EPLINK+str(ep))

#driver.switch_to.frame
#driver.switch_to.window

#driver.get(anime1) FILLER 
for i in range(1, 5 + 1):
    download(anime1,i)