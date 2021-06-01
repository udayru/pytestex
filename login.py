import time
import pytest

from selenium import webdriver


def test_login():
    driver = webdriver.Firefox(executable_path='/home/uk/PycharmProjects/browers/firefox/geckodriver')
    driver.get("https://github.com/mozilla/geckodriver/releases")
    time.sleep(10)
    driver.close()
