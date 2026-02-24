import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
time.sleep(3)
windowsOpened= driver.window_handles

driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
time.sleep(3)
driver.close()
driver.switch_to.window(windowsOpened[0])
time.sleep(3)
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text


