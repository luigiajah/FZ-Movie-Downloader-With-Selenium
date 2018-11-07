import os
import time
import urllib.request
import pyautogui
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path = 'D:\Python\Restricted\Work\chromedriver')
#Requesting For User Input
movieName = input("Hello Mike, Which Movie Would You Like To Download? ")
print ("You requested to download: ", movieName , "I'm Working On It Right Now")
type(movieName)
driver.get('http://fzmovies.net')
#Searching For Content
xpath ='/html/body/div[4]/center/form/input[1]'
box = driver.find_element_by_xpath(xpath)
time.sleep(1)
query = movieName
box.send_keys(query)
time.sleep(1)
#Clicking Search Button
search ='/html/body/div[4]/center/form/input[5]'
btn = driver.find_element_by_xpath(search)
btn.click()
time.sleep(2)
#Selecting Movie
movie ='/html/body/div[13]/ul/li/a'
btn1 = driver.find_element_by_xpath(movie)
btn1.click()
time.sleep(2)
#Pop Up Handling
alert = driver.switch_to_alert()
alert.dismiss()
#second movie selection
movieselect ='High MP4'
btn2 = driver.find_element_by_link_text(movieselect)
btn2.click()
time.sleep(1)
#download procedure selection
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
movieselect1 ='//a[contains(text(), ".mp4")]'
btn3 = driver.find_element_by_xpath(movieselect1)
btn3.click()
time.sleep(1)
#pre-final selector
downloader ='body > div.moviedesc1 > ul > li:nth-child(1) > a'
down = driver.find_element_by_css_selector(downloader)
down.click()
time.sleep(2)
#Switch Tabs
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
#Select Server
server = 'Secure Download Link 1'
servermain = driver.find_element_by_link_text(server)

ActionChains(driver).key_down(Keys.ALT).click(servermain).key_up(Keys.ALT).perform()
time.sleep(2)
ActionChains(driver).key_down(Keys.ESCAPE)
#Switch Tabs
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
print (movieName ," is downloading, please wait")
#Download
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
#Handling The Issue Of Chrome Not Downloading Automatically
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
