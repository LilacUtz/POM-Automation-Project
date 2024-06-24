import time
from unittest import TestCase
from selenium import webdriver
from Locators import JerusalemPage, MerriamWebsterPage, GooglePage
from BasePage import OuterLinks


class OuterLinksTests(TestCase):
    driver = None

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.home_page = OuterLinks(cls.driver)
        cls.google_page = GooglePage(cls.driver)
        cls.merriam_webster_page = MerriamWebsterPage(cls.driver)
        cls.jerusalem_page = JerusalemPage(cls.driver)

    @classmethod
    def tearDown(cls):
        print("--> Ending tests of MainPage")
        time.sleep(3)
        cls.driver.quit()

    def test_09_google_link(self):
        '''test google links and search'''
        print("test_google_link #9")
        self.home_page.open()
        self.home_page.click_google_link()
        self.assertEqual(self.driver.current_url, "https://www.google.com/", "Wrong URL")
        self.google_page.search_for("JUnit")
        self.google_page.click_junit_link()
        self.google_page.click_user_guide_link()
        junit_title = self.google_page.get_h1_text()
        self.assertEqual("JUnit 5 User Guide", junit_title, "Wrong title")

    def test_10_merriam_webster_link(self):
        '''test the link to the web and the link inside the web'''
        print("test_merriam_webster_link #10")
        self.home_page.open()
        self.home_page.click_merriam_webster_link()
        self.merriam_webster_page.click_games_quizzes_link()

    def test_11_jerusalem_muni(self):
        '''test the link to the web and link inside the web'''
        print("test_jerusalem_muni #11")
        self.home_page.open()
        self.home_page.click_jerusalem_link()
        time.sleep(2)
        self.jerusalem_page.click_ma_kore_bair_link()
        time.sleep(2)
