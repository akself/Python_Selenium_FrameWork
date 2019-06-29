"""
@author: Akbar Khan
@email:  akbar.khan@gmail.com
@date:   29-June-2019
"""


class WelcomePage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _pageTitle = "The Internet"

    def verify_welcome_page(self):
        actualTitle = self.driver.title
        assert actualTitle == self._pageTitle, f'Expected Title : {actualTitle} but got Actual Title : {self._pageTitle}'
        return self
