from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        (WebDriverWait(self.driver, 15)
         .until(ec.element_to_be_clickable(locator))
         .click())

    def input_(self, locator, text):
        element = (WebDriverWait(self.driver, 15)
                   .until(ec.element_to_be_clickable(locator)))
        element.send_keys(Keys.COMMAND + Keys.CONTROL + "a")
        element.send_keys(text)

    def wait_for_element(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def get_content(self, locator):
        return WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(locator)).text.strip()

    def wait_for_url_contains(self, url_part):
        WebDriverWait(self.driver, 15).until(ec.url_contains(url_part))

    def wait_for_text_change(self, locator, text):
        WebDriverWait(self.driver, 15).until(ec.text_to_be_present_in_element(locator, text))

    def get_current_url(self):
        return self.driver.current_url
