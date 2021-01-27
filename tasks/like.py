import time
import sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def likeTask(login, password, optionNumber, searchObject):

    # Initialize variables
    count = 0
    optionLocation = False
    likes = 0
    interactedPeople = []

    if optionNumber == 1:
        optionLocation = False
    elif optionNumber == 2:
        optionLocation = True

    print('Iniciating like task...')

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.instagram.com/')

    time.sleep(5)

    driver.find_element_by_xpath('//input[@type="text"]').send_keys(login)
    driver.find_element_by_xpath(
        '//input[@type="password"]').send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()

    time.sleep(5)

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

    while 1:
        time.sleep(5)  # 25s in production

        svgs = driver.find_elements_by_class_name('_8-yf5')

        # try:
        if svgs[6].get_attribute("aria-label") == "Curtir":
                time.sleep(5)  # 75s in production

                driver.find_element_by_xpath(
                    '//span[@class="fr66n"] //button[@class="wpO6b "]').click()

                count += 1
                likes += 1
                print(str(count) + ' posts liked')

                if likes == 1:
                    print('Starting task of sending directs.')
                    print('')

                    driver.get(
                        'https://www.instagram.com/direct/inbox/?hl=pt-br')

                    time.sleep(10)

                    div = driver.find_element_by_css_selector('.N9abW')

                    for x in range(3):
                        driver.execute_script(
                            'arguments[0].scrollTop = arguments[0].scrollHeight', div)

                    divs = driver.find_elements_by_xpath(
                        '//div[@class="_7UhW9   xLCgt      MMzan  KV-D4              fDxYl     "]')

                    for x in range(len(divs)):
                        if (x % 2) == 0:
                            userName = divs[x + 1].text
                            print('The username is: ', userName)
                            interactedPeople.append(userName)

                    try:
                        driver.find_element_by_xpath(
                            '//div[@class="aOOlW   HoLwm "]').click()
                    except:
                        print('')

                    driver.find_element_by_css_selector('._6q-tv').click()

                    time.sleep(1)

                    driver.find_element_by_xpath(
                        '//div[@class="                     Igw0E   rBNOH        eGOV_     ybXk5    _4EzTm                                                                                   XfCBB          HVWg4                  La5L3 ZUqME"]').click()

                    time.sleep(5)

                    driver.find_element_by_css_selector('._9AhH0').click()

                    time.sleep(10)

                    buttons = driver.find_elements_by_xpath(
                        '//div[@class="sqdOP yWX7d     _8A5w5    ]')
                    buttons[2].click()

                    time.sleep(5)

                    likesContainer = driver.find_element_by_xpath(
                        '//div[@class="                     Igw0E     IwRSH      eGOV_        vwCYk                                                                            i0EQd                                   "]')

                    for x in range(6):
                        driver.execute_script(
                            'arguments[0].scrollTop = arguments[0].scrollHeight', likesContainer)

                    peopleLikes = driver.find_elements_by_xpath(
                        '//div[@class="FPmhX notranslate MBL3Z"]')

                    for x in range(len(peopleLikes)):
                        print(peopleLikes[x].text)

                        if peopleLikes[x].text in interactedPeople:
                            interactedPeople.append(peopleLikes[x].text)

        else:
                print('This image has already been liked.')
        # except :
        #     print('An error occurred while liking the last image.')
        #     print('Ocurred', sys.exc_info()[0])

        driver.find_element_by_css_selector('.coreSpriteRightPaginationArrow').click()
