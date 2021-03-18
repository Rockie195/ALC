import bs4, pyinputplus, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options

# Make firefox run in the background
options = Options()
options.add_argument('--headless')

print('Type your Destiny password: ', end='')
password = pyinputplus.inputPassword()

browser = webdriver.Firefox(options=options)
browser.get('https://uclasv.destinysolutions.com/srs/logon.do?method=logoff&firstTime=yes')
# Input username
wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginId"))).send_keys('cjgomez')
# Input password
wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password"))).send_keys(password)
# Click logon button
wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#logonButton"))).click()

def enrollment_numbers(css_selector, program):
    # Click the programs tab, if something obscures it, wait for the obscuring element to disappear
    try:
        wait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#menu-link-CurrMgrPrograms"))).click()
    except:
        wait(browser, 20).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "#lui_programOfferingPlacementGrid")))
        wait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#menu-link-CurrMgrPrograms"))).click()
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
    hover.reset_actions()
    # If the dashboard appears, get the data. If there is no dashboard then there are zero students
    try:
        enrolled = browser.find_element_by_css_selector(
            '#genderSummary > tfoot:nth-child(2) > tr:nth-child(1) > td:nth-child(3)')
        number_enrolled = round(float(enrolled.text))
        print('\t The Dashboard number for ' + program_session_name + ' is ' + str(number_enrolled))
    except NoSuchElementException:
        print('\t The Dashboard number for ' + program_session_name + ' is 0')
    return

def iep_numbers(start, number_of_sessions, skip, program):
    program_values = {'AIEP': 1, 'IECP': 2, 'ACC': 3}
    for i in range(start, start + number_of_sessions):
        if i in skip:
            continue
        enrollment_numbers('#programOfferingProfile_PR000' + str(program_values[program]) + '_0'
                           + str(i) + '_name', program)


print('Current Numbers:')
# Get all AIEP, IECP, and ACC sessions for this quarter
iep_numbers(31, 1, [], 'AIEP')
iep_numbers(78, 4, [], 'IECP')
iep_numbers(62, 3, [], 'ACC')

print('Upcoming Numbers: ')
# Get all upcoming AIEP, IECP, and ACC sessions for next quarter
iep_numbers(32, 3, [], 'AIEP')
iep_numbers(82, 4, [], 'IECP')
iep_numbers(65, 3, [], 'ACC')

browser.quit()