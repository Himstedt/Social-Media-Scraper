from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import wget
import time

s = Service('C:\Windows\chromedriver.exe')
driver = webdriver.Chrome(service=s)

goal =  "theElonMusk"        #input("Who do you want to find?")
driver.get("http://www.facebook.com" + "/" + goal)

time.sleep(10)
driver.find_element(By.XPATH, "//span[text() = 'Only allow essential cookies']").click()

input()
