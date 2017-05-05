# PROGRAM: login.py
# DESCRIPTION: practice with login form ... potential for hacking!!

import unittest, page
from selenium import webdriver

class LoginAuth(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()
		rootURL = "http://the-internet.herokuapp.com"
		self.driver.get (rootURL)

	def test_login_UI (self): # Test the login UI
		login_page = page.MainPage(self.driver)
		login_page.click_link(self)
		assert login_page.page_title_displayed()
		assert login_page.username_field_displayed()
		assert login_page.password_field_displayed()
		assert login_page.login_button_displayed()

	def test_login_incorrect_creds (self): # Enter invalid login credentials
		login_page = page.MainPage(self.driver)
		login_page.click_link(self)
		login_page.enter_login('tomsmith','admin') 
		assert login_page.login_error_displayed()

	def test_login (self): # Enter valid login credentials
		login_page = page.MainPage(self.driver)
		login_page.click_link(self)
		login_page.enter_login('tomsmith','SuperSecretPassword!')
		assert login_page.login_success_message_displayed()
		login_page.click_logout() 


	
	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()
		