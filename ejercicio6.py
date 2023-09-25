import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By


def checkboxes(check1, check2):

    try:
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        el1 = driver.find_element(By.CSS_SELECTOR,"#checkboxes > input[type=checkbox]:nth-child(1)")
        el2 = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(3)")
        esta_marcado_el1 = el1.get_property("checked")
        esta_marcado_el2 = el2.get_property("checked")




        if check1 and not esta_marcado_el1:
            el1.click()
        if check2 and not esta_marcado_el2:
            el2.click()
        if not check1 and esta_marcado_el1:
            el1.click()
        if not check2 and esta_marcado_el2:
            el2.click()

    finally:
        time.sleep(3)
        driver.quit()



checkboxes(True, True)
checkboxes(True, False)
checkboxes(False, True)
checkboxes(False, False)