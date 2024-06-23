import os
import time
from unittest import TestCase
from selenium import webdriver
from Locators import MainPage  # Adjust the import based on your file structure


class MainPageBoxTests(TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.main_page = MainPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print("--> Ending tests of MainPage")
        time.sleep(3)
        cls.driver.quit()

    def test_05_personal_information_form(self):
        print("test_Personal_information_form #5")
        self.main_page.open()
        self.main_page.fill_personal_info(
            first_name="Lilac",
            last_name="Utz",
            city_index=2,
            email="blabla@gmail.com",
            phone_index=2,
            mobile="5555444",
            gender="female",
            profession="biology"
        )
        # time.sleep(3)
        # self.main_page.submit_form()  # Uncomment and implement if needed

    def test_06_downloading_progress(self):
        print("test_downloading_progress #6")
        self.main_page.open()
        self.main_page.start_download()
        time.sleep(3)
        self.main_page.confirm_download()
        time.sleep(3)

    def test_07_text_demo(self):
        print("test_text_demo #7")
        self.main_page.open()
        self.main_page.insert_text_to_alert("THIS IS A TEST!!!!!!!!!!!")
        time.sleep(3)

    def test_08_next_page_link(self):
        print("test_next_page_link #8")
        self.main_page.open()
        time.sleep(2)
        self.main_page.go_to_next_page()
        first_tab_title = self.main_page.get_title()
        self.assertEqual("Next Page", first_tab_title, "NOT CORRECT")
        self.main_page.click_change_name_button()
        second_tab_title = self.main_page.get_title()
        self.assertEqual("Finish", second_tab_title, "NOT CORRECT")
        print("the second title is:", second_tab_title)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
