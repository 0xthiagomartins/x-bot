from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

load_dotenv()
BROWSER = os.getenv("BROWSER", "chrome")
BASE_URL = os.getenv("BASE_URL", "http://ddg.gg")


class DriverInitializer:
    def __init__(self, browser: str = BROWSER, home: str = BASE_URL):
        match browser:
            case "firefox":
                self.driver = webdriver.Firefox(
                    service=FirefoxService(GeckoDriverManager().install())
                )
            case "chrome":
                options = webdriver.ChromeOptions()
                self.driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install()),
                    options=options,
                )
            case _:
                raise ValueError(f"Invalid browser: {browser}")
        self.driver.get(home)
