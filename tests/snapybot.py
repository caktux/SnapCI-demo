#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class Snapybot(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://snapybot.com"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.delete_all_cookies()
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1280, 1024)
    
    def test_snapybot(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.save_screenshot('screenshot.png')
        driver.find_element_by_link_text("WHAT IS IT").click()
