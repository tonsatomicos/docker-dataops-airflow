from config.selenium_config import get_chrome_options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

class WebDriver:
    def __init__(self):
        self.options = get_chrome_options()

    def get_browser(self) -> webdriver.Chrome:
        chromedriver_path = os.environ.get("CHROMEDRIVER_PATH", "/usr/lib/chromium/chromedriver")
        service = Service(executable_path=chromedriver_path)
        return webdriver.Chrome(service=service, options=self.options)