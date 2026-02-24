import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice")

checkboxes= driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value")== "option2":
        checkbox.click()
        assert checkbox.is_selected()
        time.sleep(2)
        break

radiobuttons = driver.find_elements(By.CSS_SELECTOR,"input[class='radioButton']")
radiobuttons[2].click()
time.sleep(2)
assert radiobuttons[2].is_selected()