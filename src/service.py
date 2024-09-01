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
from .utils import sleep

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
        self.driver.get("https://x.com/login")
        sleep(1)
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

    def accept_cookies(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='layers']/div/div/div/div/div/div[2]/button[1]")
            )
        )
        self.driver.find_element(
            By.XPATH, "//*[@id='layers']/div/div/div/div/div/div[2]/button[1]"
        ).click()

    def go_to_profile(self, username):
        self.driver.get(f"https://x.com/{username}")

    def get_followers(self, username):
        self.driver.get(f"https://x.com/{username}/followers")
        self.scroll_down()
        followers = self.driver.find_elements(By.XPATH, "//a[@data-testid='UserCell']")
        return [user.get_attribute("href") for user in followers]

    def get_following(self, username):
        self.driver.get(f"https://x.com/{username}/following")
        self.scroll_down()
        following = self.driver.find_elements(By.XPATH, "//a[@data-testid='UserCell']")
        return [user.get_attribute("href") for user in following]

    def scroll_down(self):
        self.last_height = self.driver.execute_script(
            "return document.body.scrollHeight"
        )
        while True:
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            sleep(1.5)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == self.last_height:
                break
            self.last_height = new_height

    def unfollow(self, user_cell, attempt=1):
        print(f"Unfollow Attempt {attempt}")
        unfollow_button = user_cell.find_elements(
            By.XPATH, ".//span[contains(text(), 'Following')]"
        )
        if unfollow_button:
            print("Clicking unfollow button")
            try:
                unfollow_button[0].click()
                sleep(0.5)
                # confirm popup
                confirm_popup = self.driver.find_element(
                    By.XPATH,
                    "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/button[1]",
                )
                print("Confirm popup found")
                confirm_popup.click()
                sleep(0.25)
            except ElementClickInterceptedException:
                self.driver.execute_script(
                    f"window.scrollTo(0, {user_cell.location['y']-(user_cell.size['height']*(1+(attempt/5)))});"
                )
                sleep(1.25)
                self.unfollow(user_cell, attempt + 1)

    def unfollow_all_non_followers(self):
        username = os.getenv("TWITTER_USERNAME")
        while True:
            self.driver.get(f"https://x.com/{username}/following")
            sleep(3.5)
            user_cells = self.driver.find_elements(
                By.XPATH,
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/*',
            )
            """
            //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]
            ...
            //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[31]
            """

            print(f"Found {len(user_cells)} user cells")
            if not user_cells:
                break
            for i in range(0, len(user_cells)):
                user_cell = user_cells[i]
                self.driver.execute_script(
                    f"window.scrollTo(0, {user_cell.location['y']-user_cell.size['height']});"
                )
                sleep(1)
                follows_you_tag = user_cell.find_elements(
                    By.XPATH,
                    ".//span[contains(text(), 'Follows you')]",
                )
                print(f"Follows you tag found: {bool(follows_you_tag)}")
                if not follows_you_tag:
                    self.unfollow(user_cell)
                    sleep(1)
