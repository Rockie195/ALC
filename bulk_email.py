import pyinputplus
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import pandas as pd
import time

# Make firefox run in the background
options = Options()
# options.add_argument('--headless')

print('Type your Zendesk password: ', end='')
password = pyinputplus.inputPassword()


# def email_student(XID, category):
    # try:

dataframe = pd.read_excel('bulk_emails.xlsx')
browser = webdriver.Firefox(options=options)
browser.get('https://support.uclaextension.edu/agent')
# Input username
wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#logon"))).send_keys('christian1344')
# Input password
wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pass"))).send_keys(password)
# Click logon button
wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".primary-button"))).click()

# Sart a new email
action = ActionChains(browser)
# wait(browser, 10).until(EC.url_to_be("https://unexsupport.zendesk.com/agent/dashboard"))

# for i in range(6):
#     current_url = browser.current_url

for index, row in dataframe.iterrows():
    try:
        print(row["Email"], "successfully received the email.")
        wait(browser, 15).until(EC.url_contains("dashboard"))

        action.key_down(Keys.ALT).key_down(Keys.CONTROL).send_keys("N").key_up(Keys.CONTROL).key_up(Keys.ALT).perform()


        wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sc-19x57y9-2"))).click()
        wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#downshift-10-input"))).send_keys(row["Email"])


        action.key_down(Keys.ALT).key_down(Keys.CONTROL).send_keys("M").key_up(Keys.CONTROL).key_up(Keys.ALT).perform()
        wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#downshift-4-input"))).send_keys("Bulk Email")
        time.sleep(0.5)
        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sc-1hg3so9-2"))).click()
        wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#\\33 60184071671")))
        browser.get("https://unexsupport.zendesk.com/agent/dashboard")
        wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sc-o4bj3t-0 > div:nth-child(1)")))
    except:
        print("ERROR: Please check on ", row["Email"])

print("Officially done!")








# Get the url of the page while it is being changed
# current_url = browser.current_url
# Wait for url to change before starting a new session
# wait(browser, 15).until(EC.url_changes(current_url))

# Terrible crm won't reload after adding
# browser.quit()
    # except:
        # print("ERROR ERROR ERROR")
        # browser.quit()




#     try:
#         print("Working on ", row["Student ID"], " on row ", index + 2)
#         email_student(row["Student ID"], row["Category"])
#     # Very broad except clause
#     except:
#         print("\nERROR: ", row["Student ID"], " on row ", index + 2)
#         break

# print("Officially done!")