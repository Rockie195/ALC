"""
Quick and messy solution to change unneeded applications from active
status to inactive status.
"""

# Imports from previous automations
import bs4, pyinputplus, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options

deactivate_applications = [277, 276, 275, 274, 273, 272, 271, 270, 269,
                           225, 224, 223, 222, 221, 212, 7, 6, 5, 4, 3]

# Make firefox run in the background
options = Options()
options.add_argument('--headless')

print('Type your Destiny password: ', end='')
password = pyinputplus.inputPassword()

browser = webdriver.Firefox(options=options)
browser.get('https://uclasv.destinysolutions.com/')

# Input username
wait(browser, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "#loginId"))).send_keys('cjgomez')

# Input password
wait(browser, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "#password"))).send_keys(password)

# Click logon button
wait(browser, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "#logonButton"))).click()


def main_app_page():
    """ Navigate to the Applications page. """
    wait(browser, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#menu-link-CurrMgrApplicationManager")))
    hover_over_programs_tab = browser.find_element_by_css_selector(
        "#menu-link-CurrMgrApplicationManager")
    hover = ActionChains(browser).move_to_element(hover_over_programs_tab)
    hover.perform()
    wait(browser, 20).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#menu-link-CurrMgrApplicationManagerApplicationSearch"))).click()
    wait(browser, 20).until(EC.visibility_of_element_located(
                                (By.CSS_SELECTOR, "#search"))).click()

failed_value = deactivate_applications[0]
try:
    for i in deactivate_applications:
        main_app_page()
        wait(browser, 20).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[2]/div[4]/div/div/div[1]/form/div[2]/table/tbody/tr[' + str(i) + ']/td[1]/a'))).click()
        wait(browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="content01"]/form/div[1]/table[1]/tbody/tr/td[2]/input'))).send_keys(Keys.HOME, "zzz-")
        wait(browser, 20).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[2]/div[4]/div/div/div[1]/form/div[1]/table[1]/tbody/tr/td[4]/select'))).click()
        wait(browser, 20).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[2]/div[4]/div/div/div[1]/form/div[1]/table[1]/tbody/tr/td[4]/select/option[2]'))).click()
        wait(browser, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#save'))).click()
except:
    print(f"{failed_value} failed to be deactivated.")