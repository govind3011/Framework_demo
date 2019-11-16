import pytest
from selenium import  webdriver

from FrameworkDemo.pom.login import *

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestClassDemo:
    @pytest.fixture(autouse=True)
    def classSetup(self):

        self.log_in=Login()

        print("class level setup of pypi")
        yield
        print("Logging out of pypi org")

    def test_tc123_verify_login(self):

        assert self.log_in.login_to_account()
        assert self.log_in.verify_login


