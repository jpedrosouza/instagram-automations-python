import time
import datetime

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def likeTask(login, password, hashtag): 

    print('Iniciating like task...')

    count = 0

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.instagram.com/')

    time.sleep(5)

    driver.find_element_by_xpath('//input[@type="text"]').send_keys(login)
    driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()

    time.sleep(5)

    startTime = datetime.datetime.now()

    print('Hour', startTime.hour)

    x = True

    while True: 
        atualTime = datetime.datetime.now()

        if (atualTime.hour >= startTime.hour + 1):
            startTime = atualTime
            print('Minute', atualTime.minute)
    
