# PAGE LOCATORS
# SEPARATED FORM THE PLACE WHERE THEY ARE BEING USED

from selenium.webdriver.common.by import By

class MainPageLocators(object):
	""" SET PAGE LOCATORS HERE """
	LOGIN_LINK = (By.LINK_TEXT, "Form Authentication")
	USN_FIELD = (By.NAME, "username")
	PWD_FIELD = (By.NAME, "password")
	LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]//button')
	LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")
	LOGIN_ERROR = (By.ID,"flash")
	LOGIN_TITLE = (By.XPATH, '//div[@id="content"]/div/h2')
	LOGIN_SUCCESS = (By.XPATH, '//div[@id="content"]/div/h2')

