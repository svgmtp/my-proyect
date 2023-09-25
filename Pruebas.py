import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestOpciones(unittest.TestCase):

    def test_jsalert(self):

        driver = webdriver.Chrome()

        try:

            driver.get("https://the-internet.herokuapp.com/javascript_alerts")
            jsalert = driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(1) > button")
            jsalert.click()
            alert = driver.switch_to.alert
            alert.accept()
            jsalert = driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(1) > button")

            assert driver.find_element(By.ID, "result").text == "You successfully clicked an alert"

        finally:
            time.sleep(3)
            driver.quit()

if __name__ == '__main__':
    unittest.main()
