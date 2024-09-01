import pytest
from src.service import XBot
from src.driver import DriverInitializer


@pytest.fixture(scope="session")
def driver_manager():
    manager = DriverInitializer()
    yield manager
    manager.driver.quit()  # Clean up after all tests


@pytest.fixture(scope="session")
def driver(driver_manager):
    return driver_manager.driver


@pytest.fixture(scope="session")
def xbot(driver):
    return XBot(driver)


def test_login(xbot):
    xbot.login()
    assert xbot.is_logged_in()


def test_get_followers(xbot):
    xbot.go_to_profile("0xthiagomartins")
    followers = xbot.get_followers()
    assert len(followers) > 0


def test_get_following(xbot):
    xbot.go_to_profile("0xthiagomartins")
    following = xbot.get_following()
    assert len(following) > 0
