#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class SnapCISauce(unittest.TestCase):
    def setUp(self):
        caps = webdriver.DesiredCapabilities.CHROME
        caps['platform'] = "Linux"
        caps['version'] = ""

        caps['name'] = 'snapybot.com on Sauce'

        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://caktux:9f6d2e20-fa00-418e-a418-790d8731058e@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(10)

        # Add Sauce sessionId for nose-sauce
        self.sessionId = self.driver.session_id

    def test_snapci_sauce(self):
        driver = self.driver
        driver.get("https://staging-snapci.caktux.ca/")
        driver.find_element_by_link_text("Easy").click()
        driver.find_element_by_link_text("WHAT IS IT").click()
        driver.find_element_by_link_text("DOCS").click()
        driver.find_element_by_link_text("FAQ").click()
        driver.find_element_by_link_text("CONTACT").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
