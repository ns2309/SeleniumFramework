import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "email").send_keys("nsulgudle@gamil.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath -//tagname[@attribute='value']
# CSS -tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Nishant Sulgudle")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)

assert "Success!" in message

#Static dropdown

dropdown= Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(0)
time.sleep(2)
dropdown.select_by_visible_text("Female")



time.sleep(2)