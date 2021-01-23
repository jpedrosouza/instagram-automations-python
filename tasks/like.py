import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def likeTask(login, password, optionNumber, searchObject): 

    # Initialize variables
    count = 0
    optionLocation = False

    if optionNumber == 1:
        optionLocation = False
    elif optionNumber == 2:
        optionLocation = True    

    print('Iniciating like task...')

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.instagram.com/')

    time.sleep(5)

    driver.find_element_by_xpath('//input[@type="text"]').send_keys(login)
    driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()

    time.sleep(5)

    if optionLocation == False:
        driver.get('https://www.instagram.com/explore/tags/' + searchObject +  '/ ')
    else:
        driver.find_element_by_xpath('//div[@class="LWmhU _0aCwM"]').click()
        driver.find_element_by_css_selector('input.focus-visible').send_keys(searchObject)
        
        time.sleep(2)

        driver.find_element_by_xpath('//div[@class="nebtz coreSpriteLocation"]').click()

    time.sleep(7)

    content = driver.find_elements_by_css_selector('._9AhH0')

    time.sleep(2)

    content[9].click()

    time.sleep(5)

    while 1:
        time.sleep(5)

        svgs = driver.find_elements_by_class_name('_8-yf5')

        if svgs[6].get_attribute("aria-label") == "Curtir":
            time.sleep(95)
            
            driver.find_element_by_xpath('//span[@class="fr66n"] //button[@class="wpO6b "]').click()
        
            count +=1
            print(str(count) + ' posts liked')

        else:
            print('This image has already been liked.') 

        driver.find_element_by_css_selector('.coreSpriteRightPaginationArrow').click()     
        

   
            
    
