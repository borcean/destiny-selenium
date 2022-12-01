# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

serial_numbers = [line.rstrip('\n') for line in open("serials.txt")]
auth = [line.rstrip('\n') for line in open("auth.txt")]
destiny_url = "https://library4.cascadetech.org/common/welcome.jsp?site=SITE_ID&context=beaverton"
destiny_url = destiny_url.replace('SITE_ID', auth[2])

class TestCheckin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  def test_checkin(self):
      for serial in serial_numbers:
        print(serial)
        self.driver.get(destiny_url)
        self.driver.set_window_size(1387, 875)
        self.driver.find_element(By.CSS_SELECTOR, "#Login > img").click()
        self.driver.find_element(By.ID, "ID_userLoginName").send_keys(auth[0])
        self.driver.find_element(By.ID, "ID_userLoginPassword").send_keys(auth[1])
        self.driver.find_element(By.NAME, "submit").click()
        self.driver.find_element(By.CSS_SELECTOR, "#TopLevelCirculation > span").click()
        self.driver.find_element(By.CSS_SELECTOR, "#Check\\ In\\ Items > span").click()
        self.driver.find_element(By.NAME, "barcode").send_keys(serial)
        self.driver.find_element(By.NAME, "barcode").send_keys(Keys.ENTER)
        time.sleep(1)
        if self.driver.find_elements(By.NAME, "transferYes"):
          time.sleep(1)
          self.driver.find_element(By.NAME, "transferYes").click()
          self.driver.find_element(By.CSS_SELECTOR, "#TopLevelCirculation > span").click()
          self.driver.find_element(By.CSS_SELECTOR, "#Check\\ In\\ Items > span").click()
          self.driver.find_element(By.NAME, "barcode").send_keys(serial)
          self.driver.find_element(By.NAME, "barcode").send_keys(Keys.ENTER)
        if self.driver.find_elements(By.NAME, "UpdateComponents"):
          time.sleep(1)
          self.driver.find_element(By.NAME, "UpdateComponents").click()
        self.driver.find_element(By.CSS_SELECTOR, "#Home > span").click()
        self.driver.find_element(By.CSS_SELECTOR, "#Logout > img").click()