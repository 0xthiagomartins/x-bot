from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os, time
from selenium.common.exceptions import NoSuchElementException

load_dotenv()


class XBot:
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def is_logged_in(self):
        try:
            self.driver.find_element(By.XPATH, "//a[@data-testid='loginButton']")
            return False
        except NoSuchElementException:
            return True

    def login(self):
        self.driver.get("https://x.com")
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='loginButton']"))
        )
        login_button.click()
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "text"))
        )
        username = os.getenv("TWITTER_USERNAME")
        username_field.send_keys(username)
        next_button = self.driver.find_element(By.XPATH, "//span[text()='Next']")
        next_button.click()
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password = os.getenv("TWITTER_PASSWORD")
        password_field.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, "//span[text()='Log in']")
        login_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(
                (By.XPATH, "//div[@data-testid='spinner']")
            )
        )

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(
                (By.XPATH, "//div[@data-testid='spinner']")
            )
        )

    def go_to_profile(self, username):
        self.driver.get(f"https://x.com/{username}")

    def get_followers(self):
        followers_button = self.driver.find_element(
            By.XPATH, "//a[@data-testid='followers']"
        )
        followers_button.click()
        followers = self.driver.find_elements(
            By.XPATH, "//a[@data-testid='user-profile']"
        )
        return followers

    def get_following(self):
        following_button = self.driver.find_element(
            By.XPATH, "//a[@data-testid='following']"
        )
        following_button.click()
        following = self.driver.find_elements(
            By.XPATH, "//a[@data-testid='user-profile']"
        )
        return following

    def unfollow_all_non_followers(self):
        # get all followers
        # get all following
        # unfollow all non-followers
        # follow all non-following
        # follow all followers
        # follow all following
        pass
