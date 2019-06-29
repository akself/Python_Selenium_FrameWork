"""
@author: Akbar Khan
@email:  akbar.khan@gmail.com
@date:   29-June-2019
"""

from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class WelcomePageTest(DriverManager):
    def test_welcomepage(self):
        welcomePage = WelcomePage(self.driver)
        welcomePage.verify_welcome_page()
