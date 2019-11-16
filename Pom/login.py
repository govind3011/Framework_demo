from selenium import webdriver

class Login:

    _username="username"
    _password="password"
    _login_button="//input[@type='submit']"
    _project="//*[contains(text,'Your projects')]"

    def __init__(self):
        #globals driver

        driver=webdriver.Chrome()

    def login_to_account(self):
        self.driver.get("https://pypi.org/")
        self.driver.find_element_by_xpath(self._username).send_keys("govind3011")
        self.driver.find_element_by_xpath(self._password).send_keys("govind@3011")
        self.driver.find_element_by_xpath(self._login_button).click()
        self.driver.find_element_by_xpath(self._username).send_keys("govind3011")

        pass

    def verify_login(self):
        return self.driver.find_element_by_xpath(self._project).is_displayed()


