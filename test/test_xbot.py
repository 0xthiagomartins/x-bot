from src.driver import DriverInitializer
from src.service import XBot
import pytest


@pytest.fixture
def driver_manager():
    return DriverInitializer()


@pytest.fixture
def driver(driver_manager):
    return driver_manager.driver


@pytest.fixture
def xbot(driver):
    return XBot(driver)


def test_login(xbot):
    xbot.login()
    assert xbot.is_logged_in()


def test_get_followers(xbot):
    followers = xbot.get_followers()
    assert len(followers) > 0


def test_get_following(xbot):
    following = xbot.get_following()
    assert len(following) > 0
