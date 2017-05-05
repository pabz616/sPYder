# PAGE OBJECT CLASSES 
# FEATURES THE OBJECTS TO USE IN A TEST CASE

from elements import BasePageElement
from locators import MainPageLocators


class BasePage(object):
	""" INITIALIZE THE BASE PAGE """
	def __init__(self, driver):
		self.driver = driver
		self.driver.implicitly_wait(5)
		self.timeout = 30

class MainPage(BasePage):
	""" SET ATTRIBUTES AND METHODS HERE """

	def click_link(self, LOGIN_LINK):
		loginLink = self.driver.find_element(*MainPageLocators.LOGIN_LINK)
		loginLink.click()
	
	def set_username (self, USN_FIELD):
		usernameInput = self.driver.find_element(*MainPageLocators.USN_FIELD)
		usernameInput.send_keys(USN_FIELD)

	def set_password (self, PWD_FIELD):
		passwordInput = self.driver.find_element(*MainPageLocators.PWD_FIELD)
		passwordInput.send_keys(PWD_FIELD)

	def click_login (self):
		loginButton = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
		loginButton.click()

	def click_logout (self):
		logoutButton = self.driver.find_element(*MainPageLocators.LOGOUT_BUTTON)
		logoutButton.click()	

	def enter_login (self, USN_FIELD, PWD_FIELD):
		self.set_password(PWD_FIELD)
		self.set_username(USN_FIELD)
		self.click_login()

	def page_title_displayed(self):
		logingPageTitle = self.driver.find_element(*MainPageLocators.LOGIN_TITLE)
		return logingPageTitle.is_displayed()

	def username_field_displayed(self):
		usnTextField = self.driver.find_element(*MainPageLocators.USN_FIELD)
		return usnTextField.is_displayed()

	def password_field_displayed(self):
		pwdTextField = self.driver.find_element(*MainPageLocators.PWD_FIELD)
		return pwdTextField.is_displayed()

	def login_button_displayed(self):
		loginBTN = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
		return loginBTN.is_displayed()

	def login_success_message_displayed(self):
		loginSuccessMsg = self.driver.find_element(*MainPageLocators.LOGIN_SUCCESS)
		return loginSuccessMsg.is_displayed()

	def login_error_displayed(self):
		validationMsg = self.driver.find_element(*MainPageLocators.LOGIN_ERROR)
		return validationMsg.is_displayed()

