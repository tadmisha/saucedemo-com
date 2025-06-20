from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent


class Page():
    def browser(ua: str):
        try:
            options = Options()
            options.add_argument(f"user-agent={ua}")

            driver = ChromeDriverManager().install()
            service = Service(driver)

            browser = webdriver.Chrome(options=options, service=service)
            return browser

        except Exception as ex:
            print(type(ex), "\n\n")
            print(ex)


def main():
    ua = UserAgent().random
    print(type(ua))
    url = "https://www.saucedemo.com/"



if (__name__ == "__main__"):
    main()