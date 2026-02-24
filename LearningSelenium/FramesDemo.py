import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.find_element(By.XPATH,"//div[@aria-label='Close']//*[name()='svg']").click()
time.sleep(4)
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").send_keys("I am doing automation")
time.sleep(5)
