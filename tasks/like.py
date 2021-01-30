from re import search
import time
import sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver =  webdriver.Chrome(ChromeDriverManager().install())
interactedPeople = []

# Start the task, being the centralizer of all actions to be performed by it.
def likeTask(login, password, optionNumber, citys, message):
    # Initialize variables
    count = 0
    optionLocation = False
    likes = 0
    searchObject = ''
    listIndex = 0

    if optionNumber == 1:
        optionLocation = False
    elif optionNumber == 2:
        optionLocation = True

    print('Iniciating task...')
    print('')

    driver.get('https://www.instagram.com/')

    time.sleep(5)

    driver.find_element_by_xpath('//input[@type="text"]').send_keys(login)
    driver.find_element_by_xpath(
        '//input[@type="password"]').send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()

    time.sleep(5)
    
    searchObject = citys[0]
    
    checkAndStartAction(optionLocation, searchObject)  

    while 1:
        time.sleep(25)  # 25s in production

        svgs = driver.find_elements_by_class_name('_8-yf5')

        try:
            if svgs[6].get_attribute("aria-label") == "Curtir":
                    time.sleep(75)  # 75s in production

                    driver.find_element_by_xpath(
                        '//span[@class="fr66n"] //button[@class="wpO6b "]').click()

                    count += 1
                    likes += 1
                    print(str(count) + ' posts liked')

                    if likes % 15 == 0: # 15 in production
                        sendDirects(message)
                        
                        print('Direct sending completed, returning to the home page.')
                        print('')
                        
                        # 90 for breaks every 3 hours and 180 for breaks every 
                        # 6 hours.
                        if likes % 180 == 0:
                            print('Pausing for 1 hour')
                            time.sleep(3600)
                            
                        if optionLocation == True:  
                            
                            if listIndex >=0 and listIndex < 4:
                                listIndex +=1
                            else:
                                listIndex = 0         
                            
                            if listIndex == 0:
                                searchObject = citys[0]
                            elif listIndex == 1:
                                searchObject = citys[1]    
                            elif listIndex == 2:
                                searchObject = citys[2]
                            elif listIndex == 3:
                                searchObject = citys[3]
                            elif listIndex == 4:
                                searchObject = citys[4]        
                                

                        checkAndStartAction(optionLocation, searchObject) 

            else:
                    print('This image has already been liked.')
        except :
            print('An error occurred while liking the last image.')
            print('Reason for error (save this information for support cases) =>', sys.exc_info()[0])
            
        
        driver.find_element_by_css_selector('.coreSpriteRightPaginationArrow').click()    

# Check which option the user chooses (Like hashtag or location), thus 
# forwarding to the respective page.
def checkAndStartAction(optionLocation, searchObject):
    if optionLocation == False:
        driver.get('https://www.instagram.com/explore/tags/' +
                   searchObject + '/ ')
    else:
        driver.find_element_by_xpath('//div[@class="LWmhU _0aCwM"]').click()
        driver.find_element_by_css_selector(
            'input.focus-visible').send_keys(searchObject)

        time.sleep(5)

        driver.find_element_by_xpath(
            '//div[@class="nebtz coreSpriteLocation"]').click()

    time.sleep(7)

    content = driver.find_elements_by_css_selector('._9AhH0')

    time.sleep(2)

    content[9].click()

    time.sleep(5)

# Directs directs to users who have not yet received one and after the end of 
# their action, it goes back to the instagram homepage.    
def sendDirects(message):
    print('')
    print('Starting task of sending directs.')
    print('')
    
    interactedPeople.clear()

    driver.get(
        'https://www.instagram.com/direct/inbox/?hl=pt-br')

    time.sleep(10)

    div = driver.find_element_by_css_selector('.N9abW')

    for x in range(50):
        driver.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollHeight', div)
        
        time.sleep(5) # 5s in production 
        
        divs = driver.find_elements_by_xpath(
            '//div[@class="_7UhW9   xLCgt      MMzan  KV-D4              fDxYl     "]')

        try:
            # with each scroll the program will catch all users it finds and will 
            # check if they are in the list, otherwise they will be added to the 
            # list to be ignored.
            for x in range(len(divs)):
                if x % 2 == 0: 
                    userName = divs[x].text

                    if userName not in interactedPeople:
                        print('User to ignore: ', userName)
                        interactedPeople.append(userName)
        except:
            print('There was an error adding a person to the list.')                

                            
    print('')        

    try:
        driver.find_element_by_xpath(
            '//button[@class="aOOlW   HoLwm "]').click()
    except:
        print('')

    driver.find_element_by_css_selector('._6q-tv').click()

    time.sleep(1)

    driver.find_element_by_css_selector('.-qQT3').click()
                    
    time.sleep(7)
                    
    driver.find_element_by_css_selector('.eLAPa').click()

    time.sleep(10)

    buttons = driver.find_elements_by_xpath(
        '//button[@class="sqdOP yWX7d     _8A5w5    "]')
                    
    buttons[1].click()

    time.sleep(5)

    likesContainer = driver.find_element_by_xpath(
        '//div[@class="                     Igw0E     IwRSH      eGOV_        vwCYk                                                                            i0EQd                                   "] //div')

    for x in range(40):
        driver.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollHeight', likesContainer)
        
        time.sleep(5) # 5s in production
        
        peopleLikes = driver.find_elements_by_xpath(
                '//a[@class="FPmhX notranslate MBL3Z"]')

        for x in range(len(peopleLikes)):
            if peopleLikes[x].text not in interactedPeople:
                choosedUser = peopleLikes[x].text
                print('The user chosen to send directs was: ', peopleLikes[x].text)
                print('')                

                driver.find_elements_by_css_selector('.wpO6b')[8].click()
                driver.find_elements_by_css_selector('.wpO6b')[7].click()

                driver.find_element_by_css_selector('.xWeGp').click()

                time.sleep(5)

                driver.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]').click()

                time.sleep(1)

                driver.find_element_by_name('queryBox').click()
                driver.find_element_by_name('queryBox').send_keys(choosedUser)

                time.sleep(5)

                driver.find_element_by_xpath('//button[@class="dCJp8 "]').click()
                driver.find_element_by_xpath('//button[@class="sqdOP yWX7d    y3zKF   cB_4K  "]').click()

                time.sleep(5)

                driver.find_element_by_xpath('//textarea[@placeholder="Mensagem..."]').send_keys(message)

                time.sleep(2)

                driver.find_elements_by_xpath('//button[@class="sqdOP yWX7d    y3zKF     "]')[3].click()   
                
                time.sleep(2)
                
                driver.get('https://www.instagram.com/?hl=pt-br')

                interactedPeople.append(choosedUser)

                time.sleep(5)

                return True