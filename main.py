from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

optObj = Options()
optObj.headless = True

#if condition for install if first time or driver needs updating
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(options = optObj)


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, executable_path="path/to/executable")
driver.get('https://www.google.com')
