import pytest
from src.service import XBot
from src.driver import DriverInitializer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
)
from src.utils import sleep

# Initialize the driver manager and driver
driver_manager = DriverInitializer()
driver = driver_manager.driver

# Initialize XBot and log in
xbot = XBot(driver)
xbot.login()
sleep(3)
xbot.accept_cookies()

# Start an interactive shell with the initialized objects
import code

code.interact(local=locals())
