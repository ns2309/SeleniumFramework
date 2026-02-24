import json
import pytest

from pageobjects.login import LoginPage
test_data_path = '../data/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    Shop_Page = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])
    Shop_Page.add_to_cart(test_list_item["productName"])
    print(Shop_Page.getTitle())
    checkout_confirmation = Shop_Page.go_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("Uni")
    checkout_confirmation.validate_order()





