import bs4, pyinputplus, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

print('Type your Destiny password: ')
password = pyinputplus.inputPassword()

def numbers(hello, css_selector, program):
    browser = webdriver.Firefox()
    browser.get('https://uclasv.destinysolutions.com/srs/logon.do?method=logoff&firstTime=yes')
    elem1 = browser.find_element_by_css_selector('#loginId')
    elem1.click()
    elem1.send_keys('cjgomez')
    elem2 = browser.find_element_by_css_selector('#password')
    elem2.click()
    elem2.send_keys(hello)
    elem3 = browser.find_element_by_css_selector('#logonButton')
    elem3.click()
    AIEPc1 = browser.find_element_by_css_selector('#menu-link-CurrMgrPrograms')
    AIEPc1.click()
    AIEPc2 = browser.find_element_by_css_selector('#programName')
    AIEPc2.click()
    AIEPc2.send_keys(program)
    AIEPc2.submit()
    time.sleep(2)
    AIEPc3 = browser.find_element_by_css_selector(css_selector)
    Name1 = AIEPc3.text
    AIEPc3.click()
    time.sleep(1)
    element_to_hover_over = browser.find_element_by_css_selector('#menu-link-CurrMgrPrograms')
    hover = ActionChains(browser).move_to_element(element_to_hover_over)
    hover.perform()
    AIEPc4 = browser.find_element_by_css_selector('#menu-link-CurrMgrProgramsProgramProfileDashboard')
    AIEPc4.click()
    try:
        #browser.find_element_by_css_selector('#genderSummary > tfoot:nth-child(2) > tr:nth-child(1) > td:nth-child(3)')
        AIEPc5 = browser.find_element_by_css_selector('#genderSummary > tfoot:nth-child(2) > tr:nth-child(1) > td:nth-child(3)')
        hi = round(float(AIEPc5.text))
        print('\t The Dashboard number for ' + Name1 + ' is ' + str(hi))
        browser.quit()
    except NoSuchElementException:
        print('\t The Dashboard number for ' + Name1 + ' is 0.')
        browser.quit()
    

print('Current Numbers:')
AIEP = numbers(password, '#programOfferingProfile_PR0001_024_name', 'AIEP')
IECP12 = numbers(password, '#programOfferingProfile_PR0002_058_name', 'IECP')
IECP_A = numbers(password, '#programOfferingProfile_PR0002_059_name', 'IECP')
IECP_B = numbers(password, '#programOfferingProfile_PR0002_060_name', 'IECP')
IECP_C = numbers(password, '#programOfferingProfile_PR0002_061_name', 'IECP')
ACC_A = numbers(password, '#programOfferingProfile_PR0003_047_name', 'ACC')
ACC_B = numbers(password, '#programOfferingProfile_PR0003_048_name', 'ACC')
ACC_C = numbers(password, '#programOfferingProfile_PR0003_049_name', 'ACC')

print('Upcoming Numbers: ')
AIEP1 = numbers(password, '#programOfferingProfile_PR0001_025_name', 'AIEP')
IECP121 = numbers(password, '#programOfferingProfile_PR0002_062_name', 'IECP')
IECP_A1 = numbers(password, '#programOfferingProfile_PR0002_063_name', 'IECP')
IECP_B1 = numbers(password, '#programOfferingProfile_PR0002_064_name', 'IECP')
IECP_C1 = numbers(password, '#programOfferingProfile_PR0002_065_name', 'IECP')
ACC_A1 = numbers(password, '#programOfferingProfile_PR0003_050_name', 'ACC')
ACC_B1 = numbers(password, '#programOfferingProfile_PR0003_051_name', 'ACC')
ACC_C1 = numbers(password, '#programOfferingProfile_PR0003_052_name', 'ACC')







