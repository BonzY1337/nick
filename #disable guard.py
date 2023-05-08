#disable guard
from os import system
import time
import random
from selenium_stealth import stealth
import urllib3
import os
import re
from tokenize import Name
from unicodedata import name
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome #importing driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--browser')
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver2 = "C:\\Projects\\chromedriver.exe"
url = "https://store.steampowered.com/login/?redir=twofactor%2Fmanage&redir_ssl=1"
url2 = "https://steamcommunity.com/friends/"
path ="C:\\Projects\\chromedriver.exe"
driver2 = Chrome(executable_path=path) #path works
os.system('cls||clear')
with open("guard.txt","r") as fp:
    x = len(fp.readlines())
    print ("Number of accounts: " + str(x))
for line in open("guard.txt","r").readlines():
    login_info = line.split()
    username = login_info[0] 
    password = login_info[1]   
    print("Current account: " + username + " " + password)
    print("-------------------------------------------------------------------------")  
    driver2.maximize_window()
    driver2.get(url)
    time.sleep(2)
    driver2.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div/div[1]/div/div/div/div[2]/div/form/div[1]/input').click() #Username klik
    driver2.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div/div[1]/div/div/div/div[2]/div/form/div[1]/input').send_keys(username) #Username 
    time.sleep(1)
    driver2.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div/div[1]/div/div/div/div[2]/div/form/div[2]/input').click()
    driver2.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div/div[1]/div/div/div/div[2]/div/form/div[2]/input').send_keys(password) #Username 
    time.sleep(1)
    driver2.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div/div[1]/div/div/div/div[2]/div/form/div[4]/button').click()
    WebDriverWait(driver2, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="none_authenticator_check"]')))
    driver2.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div[2]/div/div/div[1]/form[3]/div/div[1]/input').click()
    time.sleep(1)
    driver2.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div[2]/div/div/div[1]/form/div/div/div[4]/a[2]').click()
    driver2.get(url2)
    driver2.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[3]/div/div[2]/div[2]/div/div[1]/button[1]/span').click()
    time.sleep(1)
    driver2.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/span/span[2]/a').click()
    time.sleep(1)
    driver2.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[3]/div/div[2]/div[2]/div/div[2]/div[2]/div/span[1]/span').click()
    driver2.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[1]/div/div[3]/div/span').click()
    driver2.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[1]/div/div[3]/div/div[3]/div/a[3]').click()
    continue