from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv


service = Service(executable_path=r"E:/python/chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.maximize_window() #maximum the window
driver.get("https:\\www.google.com\maps\search\%E9%A4%90%E5%BB%B3\@25.0139774,121.5064857,16z?authuser=0&entry=ttu") # driver.get(URL) URL is the address of website which you want  to search
time.sleep(5)

    
with open('output.csv', 'w', newline='' ,encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['comment'])

               
elements = driver.find_elements(By.CLASS_NAME, "hfpxzc")

for element in elements[:1]:
    for comment in  driver.find_elements(By.XPATH, '//div[@class="Gpq6kf fontTitleSmall" and text()="Reviews"]'):
        comment.click()
        time.sleep(4)

#scrolling down manually

    comments = driver.find_elements(By.CLASS_NAME, 'wiI7pd')

    with open('output.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        for comment in comments:
            comment_text = comment.text
            writer.writerow([comment_text])
            time.sleep(4)

import pandas as pd

data = pd.read_csv("output.csv")
