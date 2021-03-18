import bs4, pyinputplus, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

print('Type your Destiny password: ')
password = pyinputplus.inputPassword()


def enrollment_numbers(password, css_selector, program):
    browser = webdriver.Firefox()
    browser.get('https://uclasv.destinysolutions.com/srs/logon.do?method=logoff&firstTime=yes')
    username_box = browser.find_element_by_css_selector('#loginId')
    username_box.click()
    username_box.send_keys('cjgomez')
    password_box = browser.find_element_by_css_selector('#password')
    password_box.click()
    password_box.send_keys(password)
    logon_button = browser.find_element_by_css_selector('#logonButton')
    logon_button.click()
    programs_tab = browser.find_element_by_css_selector('#menu-link-CurrMgrPrograms')
    programs_tab.click()
    program_name = browser.find_element_by_css_selector('#programName')
    program_name.click()
    program_name.send_keys(program)
    program_name.submit()
    time.sleep(2)
    program_session = browser.find_element_by_css_selector(css_selector)
    program_session_name = program_session.text
    program_session.click()
    time.sleep(1)
    hover_over_programs_tab = browser.find_element_by_css_selector('#menu-link-CurrMgrPrograms')
    hover = ActionChains(browser).move_to_element(hover_over_programs_tab)
    hover.perform()
    dashboard = browser.find_element_by_css_selector('#menu-link-CurrMgrProgramsProgramProfileDashboard')
    dashboard.click()
    try:
        # browser.find_element_by_css_selector('#genderSummary > tfoot:nth-child(2) > tr:nth-child(1) > td:nth-child(3)')
        enrolled = browser.find_element_by_css_selector(
            '#genderSummary > tfoot:nth-child(2) > tr:nth-child(1) > td:nth-child(3)')
        number_enrolled = round(float(enrolled.text))
        print('\t The Dashboard number for ' + program_session_name + ' is ' + str(number_enrolled))
        browser.quit()
    except NoSuchElementException:
        print('\t The Dashboard number for ' + program_session_name + ' is 0.')
        browser.quit()


print('Current Numbers:')
AIEP = enrollment_numbers(password, '#programOfferingProfile_PR0001_024_name', 'AIEP')
IECP12 = enrollment_numbers(password, '#programOfferingProfile_PR0002_058_name', 'IECP')
IECP_A = enrollment_numbers(password, '#programOfferingProfile_PR0002_059_name', 'IECP')
IECP_B = enrollment_numbers(password, '#programOfferingProfile_PR0002_060_name', 'IECP')
IECP_C = enrollment_numbers(password, '#programOfferingProfile_PR0002_061_name', 'IECP')
ACC_A = enrollment_numbers(password, '#programOfferingProfile_PR0003_047_name', 'ACC')
ACC_B = enrollment_numbers(password, '#programOfferingProfile_PR0003_048_name', 'ACC')
ACC_C = numbers(password, '#programOfferingProfile_PR0003_049_name', 'ACC')

print('Upcoming Numbers: ')
AIEP1 = enrollment_numbers(password, '#programOfferingProfile_PR0001_025_name', 'AIEP')
IECP121 = enrollment_numbers(password, '#programOfferingProfile_PR0002_062_name', 'IECP')
IECP_A1 = enrollment_numbers(password, '#programOfferingProfile_PR0002_063_name', 'IECP')
IECP_B1 = enrollment_numbers(password, '#programOfferingProfile_PR0002_064_name', 'IECP')
IECP_C1 = enrollment_numbers(password, '#programOfferingProfile_PR0002_065_name', 'IECP')
ACC_A1 = enrollment_numbers(password, '#programOfferingProfile_PR0003_050_name', 'ACC')
ACC_B1 = enrollment_numbers(password, '#programOfferingProfile_PR0003_051_name', 'ACC')
ACC_C1 = enrollment_numbers(password, '#programOfferingProfile_PR0003_052_name', 'ACC')
