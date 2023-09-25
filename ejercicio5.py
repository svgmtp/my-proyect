import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


class AssetionError:
    pass


try:
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(5)
    for i in range(10):
        try:
            tbx__username = driver.find_element(By.NAME, "username")
            break
        except:
            pass
        time.sleep(1)
    else:
        raise AssetionError("tbx__username no encontrado")

    tbx__username.send_keys("tomsmith")
    tbx__password = driver.find_element(By.NAME, "password")
    tbx__password.send_keys("SuperSecretPassword!")
    btn__login = driver.find_element(By.CSS_SELECTOR, "#login > button > i")
    btn__login.click()
    btn__logout = driver.find_element(By.CSS_SELECTOR, "#content > div > a > i")
    btn__logout.click()
finally:
    driver.quit()