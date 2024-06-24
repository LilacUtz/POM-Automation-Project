from unittest import TestCase
from selenium import webdriver
from Locators import MainPageTitles
import time


class MainPageTitlesTests(TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.main_page_title = MainPageTitles(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print("--> Ending tests of MainPage")
        time.sleep(3)
        cls.driver.quit()

    def test_01_tab_title(self):
        '''checking if the page title name is correct'''
        print("test_tab_title #1")
        self.main_page_title.open()
        tab_title = self.main_page_title.get_tab_title()
        self.assertEqual("Automation Project", tab_title, "Wrong page title")

    def test_02_title_main_page(self):
        '''checking if the page header name is correct'''
        print("test_title_main_page #2")
        self.main_page_title.open()
        title_main_page = self.main_page_title.get_main_header()
        self.assertEqual("Automation Project - Main Page", title_main_page, "NOT CORRECT")

    def test_03_h2_titles(self):
        '''checking if the title is correct'''
        print("test_cities_of_the_world #3")
        self.main_page_title.open()
        exp_titles = ["Cities of the World", "Student Details", "Form", "A demonstration of how to access a PROGRESS element", "Text Demo", "Links"]
        act_titles = self.main_page_title.get_h2_titles()
        for i in range(len(act_titles)):
            self.assertEqual(act_titles[i], exp_titles[i], "wrong title")

    def test_04_table_of_cities(self):
        '''test if the info is correct'''
        print("test_table_of_cities #4")
        self.main_page_title.open()
        tr_elements = self.main_page_title.get_cities_table_rows()
        self.assertEqual(len(tr_elements), 3, "WRONG NUM OF ROWS")
