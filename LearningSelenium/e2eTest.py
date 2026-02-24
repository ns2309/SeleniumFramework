from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
products= driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products:
    ProductName=product.find_element(By.XPATH,"div/h4/a").text
    if ProductName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()


driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,"button[class*='btn-success']").click()
driver.find_element(By.ID,"country").send_keys("Uni")
Wait= WebDriverWait(driver,10)
Wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"United States of America")))
driver.find_element(By.LINK_TEXT,"United States of America").click()

driver.find_element(By.CSS_SELECTOR,"div[class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
Success= driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text

assert "Success! Thank you! Your" in Success
driver.close()