import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time


options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--start-maximized")
# options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
driver_path = "D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
options.binary_location = brave_path

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.youtube.com/@CGMeetup/videos")
time.sleep(5)
link = driver.find_elements(By.XPATH,'(//div[@id="primary"])[3]//div[@id="contents"]//div//div//div[@id="dismissible"]//div[@id="thumbnail"]//a[@class="yt-simple-endpoint inline-block style-scope ytd-thumbnail"]')
print('length ----->>>>',len(link))

for i in link:
    jj = i.get_attribute('href')
    print(jj)
    time.sleep(20)
