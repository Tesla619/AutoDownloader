from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#Update To Do: if condition for install if first time or driver needs updating
driver = webdriver.Chrome(ChromeDriverManager().install())


def google(): #using func doesn't auto close browser
    driver.get('https://www.google.com')

#if __name__ == "__main__":
google()
    
    