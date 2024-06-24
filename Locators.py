import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from POM.BasePage import BasePage
import time


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "file:///C:/Users/ucore/PycharmProjects/Selenium_tests_run/src/web/home.html"

    def open(self):
        self.driver.get(self.url)

    def fill_personal_info(self, first_name, last_name, city_index, email, phone_index, mobile, gender, profession):
        self.find_element(By.ID, "first-name").send_keys(first_name)
        self.find_element(By.NAME, "last-name").send_keys(last_name)
        Select(self.find_element(By.ID, "city")).select_by_index(city_index)
        self.find_element(By.ID, "email").send_keys(email)
        Select(self.find_element(By.NAME, "area-code")).select_by_index(phone_index)
        self.find_element(By.ID, "mobile").send_keys(mobile)
        self.find_element(By.ID, gender).click()
        self.find_element(By.ID, profession).click()

    def start_download(self):
        self.find_element(By.CSS_SELECTOR, '[onclick="startDownload()"]').click()

    def confirm_download(self):
        self.find_element(By.CSS_SELECTOR, '[onclick="confirmMessage(this)"]').click()

    def insert_text_to_alert(self, text):
        self.find_element(By.XPATH, "/html/body/section/main/button[1]").click()
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def go_to_next_page(self):
        self.find_element(By.LINK_TEXT, "Next Page").click()

    def get_title(self):
        return self.driver.title

    def click_change_name_button(self):
        self.find_element(By.XPATH, "/html/body/section/main/button").click()


class MainPageTitles(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "file:///C:/Users/ucore/PycharmProjects/Selenium_tests_run/src/web/home.html"
        self.tab_title_locator = (By.TAG_NAME, "title")
        self.main_header_locator = (By.TAG_NAME, "h1")
        self.h2_titles_locator = (By.TAG_NAME, "h2")
        self.cities_table_locator = (By.TAG_NAME, "table")

    def open(self):
        self.driver.get(self.url)

    def get_tab_title(self):
        return self.driver.title

    def get_main_header(self):
        return self.wait_for_element(self.main_header_locator).text

    def get_h2_titles(self):
        return [element.text for element in self.driver.find_elements(*self.h2_titles_locator)]

    def get_cities_table_rows(self):
        table = self.driver.find_elements(*self.cities_table_locator)[0]
        tbody = table.find_element(By.TAG_NAME, "tbody")
        return tbody.find_elements(By.TAG_NAME, "tr")


class GooglePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_field_locator = (By.ID, "APjFqb")
        self.junit_link_locator = (By.XPATH, "//*[@id=\"rso\"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a")
        self.user_guide_link_locator = (By.LINK_TEXT, "User Guide")
        self.h1_locator = (By.TAG_NAME, "h1")

    def search_for(self, query):
        search_field = self.wait_for_element(self.search_field_locator)
        search_field.send_keys(query)
        search_field.send_keys(Keys.ENTER)

    def click_junit_link(self):
        self.wait_for_element(self.junit_link_locator).click()

    def click_user_guide_link(self):
        self.wait_for_element(self.user_guide_link_locator).click()

    def get_h1_text(self):
        return self.wait_for_element(self.h1_locator).text


class MerriamWebsterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.games_quizzes_link_locator = (By.LINK_TEXT, "Games & Quizzes")

    def click_games_quizzes_link(self):
        self.wait_for_element(self.games_quizzes_link_locator).click()


class JerusalemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.ma_kore_bair_link_locator = (By.LINK_TEXT, "מה קורה בעיר")

    def click_ma_kore_bair_link(self):
        self.wait_for_element(self.ma_kore_bair_link_locator).click()
