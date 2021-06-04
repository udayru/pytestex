import datetime
import time

from selenium import webdriver
import pytest
driver = None


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#
#     # set a report attribute for each phase of a call, which can
#     # be "setup", "call", "teardown"
#
#     setattr(item, "rep_" + rep.when, rep)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(autouse=True, scope='session')
def setup(request):
    driver = webdriver.Firefox(executable_path='/home/uk/PycharmProjects/browers/firefox/geckodriver')
    #request.cls.driver = driver
    #//div[@class='sg-col-inner']/descendant::div[@class='a-section a-spacing-none']

    yield driver
    driver.close()

