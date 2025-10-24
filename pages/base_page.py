from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click_to_element(self, locator):
        try:
            self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()
        except TimeoutException:
            element = self.wait.until(expected_conditions.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", element)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def wait_until_element_is_invisible(self, locator):
        return WebDriverWait(self.driver, 60).until(expected_conditions.invisibility_of_element_located(locator))

    def wait_change_text_in_element(self, locator, text):
        try:
            self.wait.until_not(expected_conditions.text_to_be_present_in_element(locator, text))
            return True
        except TimeoutException:
            return False

    def wait_change_text_in_element_without_new_text(self, locator, old_text):
        try:
            WebDriverWait(self.driver, 60).until(lambda d: d.find_element(*locator).text != old_text)
            return True
        except TimeoutException:
            return False

    def wait_text_in_element(self, locator, text):
        try:
            self.wait.until(expected_conditions.text_to_be_present_in_element(locator, text))
            return True
        except TimeoutException:
            return False

    def hover_over_element(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def format_locators(self, not_formatted_locator, num):
        method, locator = not_formatted_locator
        locator = locator.format(num)
        return (method, locator)

    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element_with_wait(locator))
