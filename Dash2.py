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
    # Input username
    wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginId"))).send_keys('cjgomez')
    # Input password
    wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password"))).send_keys(password)
    # Click logon button
    wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#logonButton"))).click()
    # Click the programs tab
    wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-link-CurrMgrPrograms"))).click()
    # Enter the Program name
    wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#programName"))).send_keys(program)
    program_name = browser.find_element_by_css_selector('#programName')
    program_name.submit()
    # Wait for the program link to appear, then save the text and click on the link
    wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    program_session = browser.find_element_by_css_selector(css_selector)
    program_session_name = program_session.text
    program_session.click()
    # Wait for the program tab to appear and then hover over the program tab
    wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-link-CurrMgrPrograms")))
    hover_over_programs_tab = browser.find_element_by_css_selector("#menu-link-CurrMgrPrograms")
    hover = ActionChains(browser).move_to_element(hover_over_programs_tab)
    hover.perform()
    # Click on dashboard
    wait(browser, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#menu-link-CurrMgrProgramsProgramProfileDashboard"))).click()
    # If the dashboard appears, get the data. If there is no dashboard then there are zero students
    try:
        enrolled = browser.find_element_by_css_selector(
            '#genderSummary > tfoot:nth-child(2) > tr:nth-child(1) > td:nth-child(3)')
        number_enrolled = round(float(enrolled.text))
        print('\t The Dashboard number for ' + program_session_name + ' is ' + str(number_enrolled))
        browser.quit()
    except NoSuchElementException:
        print('\t The Dashboard number for ' + program_session_name + ' is 0')
        browser.quit()
        return

def iep_numbers(start, number_of_sessions, skip, program):
    program_values = {'AIEP': 1, 'IECP': 2, 'ACC': 3}
    for i in range(start, start + number_of_sessions):
        if i in skip:
            continue
        enrollment_numbers(password, '#programOfferingProfile_PR000' + str(program_values[program]) + '_0'
                           + str(i) + '_name', program)


print('Current Numbers:')
# Get all AIEP, IECP, and ACC sessions for this quarter
iep_numbers(24, 1, [], 'AIEP')
iep_numbers(58, 4, [], 'IECP')
iep_numbers(47, 3, [], 'ACC')

print('Upcoming Numbers: ')
# Get all upcoming AIEP, IECP, and ACC sessions for next quarter
iep_numbers(25, 1, [], 'AIEP')
iep_numbers(62, 4, [], 'IECP')
iep_numbers(50, 3, [], 'ACC')