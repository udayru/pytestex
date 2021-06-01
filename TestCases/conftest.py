from selenium import webdriver
import pytest


@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Firefox(executable_path='/home/uk/PycharmProjects/browers/firefox/geckodriver')
    request.cls.driver = driver
    yield
    driver.close()
