import os
from contextlib import contextmanager
import time
import json
from tempfile import mkdtemp
import traceback
from typing import Literal

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

WAIT_SECS = 20  # Added for Upwork env

# Extracted from our code
def create_hchb_driver(mode: Literal["demo", "fastapi", "lambda"]) -> webdriver.Remote:
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:automationName": "uiautomator2",
        "appium:deviceName": "Android",
        "appium:appPackage": "com.hchb.android.pc.ui.training",
        "appium:appActivity": "com.hchb.android.pc.ui.PCStartup",
        "appium:language": "en",
        "appium:locale": "US",
        "appium:autoGrantPermissions": True,
    })
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(WAIT_SECS)  # seconds
    ###################
    # START OF YOUR CODE - do not delete this comment

    # was not able to enter login page of the app due to page
    # not accepting the user info provided in the test doc
    # used validate page for the coding task instead >_<
    passwordFieldId = "com.hchb.android.pc.ui.training:id/password1"
    passwordFieldEl = driver.find_element(by=AppiumBy.ID, value=passwordFieldId)

    password = "Smeshbros8G"
    passwordFieldEl.send_keys(password)

    passwordConfirmFieldId = "com.hchb.android.pc.ui.training:id/password2"
    passwordConfirmFieldEl = driver.find_element(by=AppiumBy.ID, value=passwordConfirmFieldId)

    password = "Smeshbros8G"
    passwordConfirmFieldEl.send_keys(password)

    validateBtnId = "com.hchb.android.pc.ui.training:id/validate"
    validateBtnEl = driver.find_element(by=AppiumBy.ID, value=validateBtnId)

    validateBtnEl.click()

    # END OF YOUR CODE - do not delete this comment
    ###################
    return driver

if __name__ == "__main__":
    create_hchb_driver("demo")
