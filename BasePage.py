from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, *locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))


class OuterLinks(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "file:///C:/Users/ucore/PycharmProjects/Selenium_tests_run/src/web/home.html"
        self.google_link_locator = (By.LINK_TEXT, "Google")
        self.merriam_webster_link_locator = (By.LINK_TEXT, "Merriam-Webster Dictionary")
        self.jerusalem_link_locator = (By.LINK_TEXT, "Jerusalem Municipality")

    def open(self):
        self.driver.get(self.url)

    def click_google_link(self):
        self.wait_for_element(self.google_link_locator).click()

    def click_merriam_webster_link(self):
        self.wait_for_element(self.merriam_webster_link_locator).click()

    def click_jerusalem_link(self):
        self.wait_for_element(self.jerusalem_link_locator).click()
