import pyinputplus
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import pandas as pd

categories_dict = {
    "IP-ACLA" : "table.regularForm:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > select:nth-child(1) > option:nth-child(2)",
    "IP-Certificate" : "table.regularForm:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > select:nth-child(1) > option:nth-child(3)",
    "IP-Dentistry" : "table.regularForm:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > select:nth-child(1) > option:nth-child(4)",
    "IP-Discount" : "table.regularForm:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > select:nth-child(1) > option:nth-child(5)",
    "IP-ICCP" : "table.regularForm:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > select:nth-child(1) > option:nth-child(6)",
    "IP-LCI" : "table.regularForm:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > select:nth-child(1) > option:nth-child(7)",
    "IP-Legacy Fee" : "table.regularForm:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > select:nth-child(1) > option:nth-child(8)",
    "IP-NCAA Partnership" : "table.regularForm:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > select:nth-child(1) > option:nth-child(9)",
    "IP-New Fee" : "table.regularForm:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > select:nth-child(1) > option:nth-child(10)",
    "IP-Online Student" : "table.regularForm:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > select:nth-child(1) > option:nth-child(11)",
    "IP-Partner Recruit" : "table.regularForm:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > select:nth-child(1) > option:nth-child(12)",
    "IP-Study Abroad" : "table.regularForm:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > select:nth-child(1) > option:nth-child(13)"
}


# Make firefox run in the background
options = Options()
options.add_argument('--headless')

print('Type your Destiny password: ', end='')
password = pyinputplus.inputPassword()

browser = webdriver.Firefox(options=options)
browser.get('https://uclatestsv.destinysolutions.com/srs/logon.do?method=logoff&firstTime=yes')
# Input username
wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginId"))).send_keys('cjgomez')
# Input password
wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password"))).send_keys(password)
# Click logon button
wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#logonButton"))).click()

# Navigate to enrollment
wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".selectedItem > div:nth-child(1)"))).click()
wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-link-EnrolMgr"))).click()

def category_upload(XID, category):
    try:
        # Navigate to XID profile
        id_search = wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "table.fullWidthTable:nth-child(1) > tbody:nth-child(3) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > input:nth-child(3)")))
        id_search.send_keys(XID)
        id_search.submit()
        wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchResultItemNameLink_0"))).click()

        # Click on categories
        wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "table.regularForm:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > select:nth-child(1)"))).click()
        wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, categories_dict[category]))).click()
        wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#add_stu_category_button"))).click()

        # Save the page
        action = ActionChains(browser)
        action.key_down(Keys.ALT).key_down(Keys.SHIFT).send_keys("S").key_up(Keys.ALT).key_up(Keys.SHIFT).perform()

        # Get the url of the page while it is being changed
        current_url = browser.current_url
        # Wait for url to change before starting a new session
        wait(browser, 15).until(EC.url_changes(current_url))
        # Click to start new session
        wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#newSession"))).click()        

    except:
        # If anything fails, print error and start a new session
        print("ERROR ERROR ERROR")
        wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#newSession"))).click()


dataframe = pd.read_excel('categories_upload.xlsx')
for index, row in dataframe.iterrows():
    try:
        print("Working on", row["Student ID"], "on row", index + 2)
        category_upload(row["Student ID"], row["Category"])
    # Very broad except clause for any errors
    except:
        print("\nERROR:", row["Student ID"], "on row", index + 2)

print("Officially done!")
browser.quit()