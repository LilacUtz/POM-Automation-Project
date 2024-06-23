import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from POM.BasePage import BasePage


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
