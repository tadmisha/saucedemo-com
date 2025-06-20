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

    
    def close(self):
        self.browser.close()
        self.browser.quit()



def main():
    ua = UserAgent().random
    print(type(ua))
    url = "https://www.saucedemo.com/"
    page = Page(url, ua)
    page.login("standard_user", "secret_sauce")
    page.close()



if (__name__ == "__main__"):
    main()