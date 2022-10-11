"""
Quick and messy solution to change unneeded fees from active status to
inactive status.
"""

# Imports from previous automations
import bs4, pyinputplus, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options

deactivate_srs = [1577, 1359, 1358, 1357, 1356, 977, 976, 975, 974, 973,
                  972, 971, 970, 969, 968, 967, 966, 965, 964, 963, 962,
                  961, 958, 957, 956, 955, 954, 953, 952, 951, 950, 949,
                  948, 947, 946, 945, 944, 943, 942, 941, 940, 939, 938,
                  937, 936, 935, 934, 933, 932, 931, 930, 929, 928, 927,
                  926, 925, 924, 923, 922, 921, 920, 919, 918, 917, 916,
                  915, 914, 913, 912, 911, 910, 909, 908, 907, 906, 905,
                  904, 903, 902, 901, 900, 899, 898, 897, 896, 895, 894,
                  893, 892, 891, 890, 889, 888, 887, 886, 885, 884, 883,
                  882, 881, 880, 879, 878, 877, 876, 875, 874, 873, 872,
                  871, 870, 869, 868, 867, 866, 865, 864, 863, 862, 861,
                  860, 859, 858, 857, 856, 855, 854, 853, 852, 851, 850,
                  849, 848, 847, 846, 845, 844, 843, 842, 841, 840, 839,
                  838, 837, 836, 835, 834, 833, 832, 831, 830, 829, 828,
                  827, 826, 825, 824, 823, 822, 821, 820, 819, 818, 817,
                  816, 815, 814, 813, 812, 811, 810, 809, 808, 807, 806,
                  805, 804, 803, 802, 801, 800, 799, 798, 797, 796, 795,
                  794, 793, 792, 791, 790, 789, 788, 787, 786, 785, 784,
                  783, 782, 781, 780, 779, 778, 777, 776, 775, 774, 773,
                  772, 771, 770, 769, 768, 767, 766, 765, 764, 763, 762,
                  761, 760, 759, 758, 757, 756, 755, 754, 753, 752, 751,
                  750, 749, 748, 747, 746, 745, 744, 743, 742, 741, 740,
                  712, 711, 710, 709, 708, 707, 706, 704, 703, 290, 289,
                  288, 287, 286, 285, 284, 277, 276, 275, 274, 273, 272,
                  271, 270, 269, 268, 267, 266, 265, 264, 263, 262, 261,
                  260, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250,
                  249, 248, 247, 246, 245, 244, 243, 242, 241, 240, 239,
                  238, 237, 236, 235, 234, 233, 232, 231, 230, 229, 228,
                  227, 226, 225, 224, 223, 222, 221, 220, 219, 218, 217,
                  216, 215, 214, 213, 212, 211, 210, 209, 208, 207, 206,
                  205, 204, 203, 202, 201, 200, 199, 198, 197, 196, 195,
                  194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184,
                  183, 182, 181, 180, 179, 178, 177, 176, 175, 174, 173,
                  172, 171, 170, 169, 168, 167, 166, 165, 164, 163, 162,
                  161, 160, 159, 158, 157, 156, 155, 154, 153, 152, 151,
                  150, 149, 130, 129, 128, 127, 126, 125, 124, 123, 122,
                  121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111,
                  110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100,
                  99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87,
                  86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74,
                  73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61,
                  60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48,
                  47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35,
                  34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22,
                  21, 20, 19, 18, 17, 16, 15, 14, 13, 12]

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

# Navigate to the SR Fees page
wait(browser, 20).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#mainMenu"))).click()
wait(browser, 20).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#menu-link-SysAdmin"))).click()
wait(browser, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "#menu-link-SysAdminFee")))
hover_over_programs_tab = browser.find_element_by_css_selector(
    "#menu-link-SysAdminFee")
hover = ActionChains(browser).move_to_element(hover_over_programs_tab)
hover.perform()
wait(browser, 20).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#menu-link-SysAdminFeeSpecialRequest"))).click()

# Switch unwanted SR fee to inactive
try:
    failed_value = deactivate_srs[0]
    for i in deactivate_srs:
        wait(browser, 20).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="activeSpecialRequests"]/tbody/tr[' + str(i) + ']/td[4]/a/img'))).click()
        wait(browser, 20).until(EC.visibility_of_element_located(
            (By.XPATH,
             '//*[@id="content01"]/form/table/tbody/tr/td/table/tbody/tr[2]/td/table[1]/tbody/tr/td[1]/table[3]/tbody/tr/td[3]/select'))).click()
        wait(browser, 20).until(EC.visibility_of_element_located(
            (By.XPATH,
             '/html/body/div[2]/div[4]/div/div/div[1]/form/table/tbody/tr/td/table/tbody/tr[2]/td/table[1]/tbody/tr/td[1]/table[3]/tbody/tr/td[3]/select/option[2]'))).click()
        wait(browser, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#savePage'))).click()
        failed_value = i
except:  # Capture all exceptions when trying to deactivate
    print(f"{failed_value} failed to be deactivated.")


