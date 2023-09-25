from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('acceder a la pagina')
def step_impl(context):
   driver = webdriver.Chrome()
   driver.get("https://the-internet.herokuapp.com/javascript_alerts")
   assert

@when('pulsa en jsalert')
def step_impl(context):
    jsalert = driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(1) > button")
    jsalert.click()

@when('acepta alert')
def step_impl(context):
    alert = driver.switch_to.alert
    alert.accept()



@then('se muestra el resultado')
def step_impl(context):
   assert driver.find_element(By.ID, "result").text == "You successfully clicked an alert"