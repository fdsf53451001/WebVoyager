from selenium.webdriver.chrome.options import Options
from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument("user-data-dir=D:\WebVoyager\selenium")
driver = webdriver.Chrome(options=chrome_options)
#for selenium 4.15.2 options instead of chrome_options
#driver = webdriver.Chrome(options=chrome_options) 
driver.get("https://www.google.com")

input()