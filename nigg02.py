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
driver2 = webdriver.Chrome(options=options, executable_path=r"C:\\Projects\\chromedriver.exe")
url = "https://help.steampowered.com/en/wizard/HelpWithLoginInfo?accountsearch=1&issueid=408&reset=1"
path ="C:\\Projects\\chromedriver.exe" #path for the driver
bahane = ["I was inactive from a long time due to work reasons, apparently my account has been hijacked. An unknown email is attached to it, I have first email as proof", "There is some unknown email attached to my account, i was not active because of work. I have first email as ownership proof", "My account is hijacked, some unknown email is linked to my account, I was inactive from long time and i have ownership proof that is my first email that i used to register this account"]
os.system('cls||clear')
with open("revoke.txt","r") as fp:
    x = len(fp.readlines())
    print ("Number of accounts: " + str(x))
for line in open("revoke.txt","r").readlines():
    login_info = line.split()
    username = login_info[0] 
    email = login_info[1]   
    print(username + " " + email)
    print("-------------------------------------------------------------------------")  
    driver2.get(url)
    driver2.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[2]/div[2]/div/div[2]/div[1]/div[3]/form/input[6]').click() #Username klik
    driver2.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[2]/div[2]/div/div[2]/div[1]/div[3]/form/input[6]').send_keys(username) #Username 
    WebDriverWait(driver2, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div[1]/div[7]/div[2]/div[2]/div/div[2]/div[1]/div[3]/form/div[3]/div[1]/div/div/div/iframe')))
    driver2.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border').click() 
    driver2.switch_to.default_content()
    time.sleep(1)
    WebDriverWait(driver2, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="create_help_request_email_address"]')))
    driver2.find_element(By.XPATH,'/html/body/div[1]/div[7]/div[2]/div[2]/div/div[2]/div/div[4]/form/div[1]/div[2]/input').click()
    time.sleep(1)
    driver2.find_element(By.XPATH,'/html/body/div[1]/div[7]/div[2]/div[2]/div/div[2]/div/div[4]/form/div[1]/div[2]/input').send_keys(email)
    time.sleep(1)
    driver2.find_element(By.XPATH,'/html/body/div[1]/div[7]/div[2]/div[2]/div/div[2]/div/div[4]/form/div[4]/div[1]/div/input').click()
    time.sleep(1)
    driver2.find_element(By.XPATH,'/html/body/div[1]/div[7]/div[2]/div[2]/div/div[2]/div/div[4]/form/div[4]/div[1]/div/input').send_keys(email)
    driver2.find_element(By.XPATH,'//*[@id="extended_string_message"]').send_keys(random.choice(bahane))#randi rona
    WebDriverWait(driver2, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div[1]/div[7]/div[2]/div[2]/div/div[2]/div/div[4]/form/div[9]/div[1]/div/div/div/iframe')))
    driver2.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border').click() 
    driver2.switch_to.default_content()
    ans = int(input("enter 1 to restart: "))
    if(ans == 1):
        continue
