from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent


class Page():
    def __init__(self, url: str, ua: str):
        self.browser = self.get_browser(ua)
        if not self.browser: raise RuntimeError("Failed to initialize browser")

        self.browser.get(url)

    def get_browser(self, ua: str) -> webdriver.Chrome:
        options = Options()
        options.add_argument(f"user-agent={ua}")

        driver = ChromeDriverManager().install()
        service = Service(driver)

        browser = webdriver.Chrome(options=options, service=service)
        return browser
        
    def login(self, username: str, password: str):
        username_input, password_input = self.browser.find_elements(By.XPATH, '//input[@class="input_error form_input"]')
        username_input.send_keys(username)
        password_input.send_keys(password)

        login_btn = self.browser.find_element(By.XPATH,'//input[@class="submit-button btn_action"]')
        login_btn.click()
    
    def add_to_cart(self, id: str = "add-to-cart-sauce-labs-bolt-t-shirt"):
        add_btn = self.browser.find_element(By.XPATH, f'//button[@id="{id}"]')
        add_btn.click()

    def open_cart(self): #! It would be more efficient to just open by url, but clicking button is fancier ig
        cart_btn = self.browser.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
        cart_btn.click()

    def check_if_in_cart(self):
        products = self.browser.find_elements(By.XPATH, '//div[@class="cart_item_label"]')
        if len(products) != 1: raise RuntimeError("Product not in the cart.")

    def open_checkout(self): #! It would be more efficient to just open by url, but clicking button is fancier ig
        cart_btn = self.browser.find_element(By.XPATH, '//button[@id="checkout"]')
        cart_btn.click()
    
    def input_checkout(self, name: str, surname: str, zip_code: int):
        name_input, surname_input, zip_code_input = self.browser.find_elements(By.XPATH, '//input[@class="input_error form_input"]')
        name_input.send_keys(name)
        surname_input.send_keys(surname)
        zip_code_input.send_keys(zip_code)
        
        submit_btn = self.browser.find_element(By.XPATH, '//input[@class="submit-button btn btn_primary cart_button btn_action"]')
        submit_btn.click()
        input('')
    
    def close(self):
        self.browser.close()
        self.browser.quit()



def main():
    url = "https://www.saucedemo.com/"

    username = "standard_user"
    password = "secret_sauce"

    name = "Name"
    surname = "Surname"
    zip_code = 11111

    ua = UserAgent().random

    page = Page(url, ua)
    page.login(username, password)
    page.add_to_cart()
    page.open_cart()
    page.check_if_in_cart()
    page.open_checkout()
    page.input_checkout(name, surname, zip_code)
    page.close()



if (__name__ == "__main__"):
    main()