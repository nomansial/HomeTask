from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from data.locators import SearchPageLocators
from pages.base_page import BasePage


class SearchPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://www.google.com/?hl=en"
        self.startPageURL = "https://www.startpage.com/"
        self.locator = SearchPageLocators
        super().__init__(driver, wait)

    def go_to_search_page(self):
        self.go_to_page(self.url)

    def make_a_Google_search(self, input_text):
        self.wait.until(EC.visibility_of_element_located(self.locator.SEARCH_INPUT))
        self.driver.find_element(*self.locator.SEARCH_INPUT).send_keys(input_text)
        self.driver.find_element(*self.locator.SEARCH_INPUT).send_keys(Keys.RETURN)

    def get_google_search_results_title(self):
        """
            Get all search results title elements
        """
        elements = self.driver.find_elements(*self.locator.GOOGLE_TITLE_XPATH)
        text_of_title = []

        """
            Get Text from all search result title elements
        """
        for value in elements:
            cell_value = value.text
            text_of_title.append(cell_value)
        return text_of_title

    def get_google_search_results_URLS(self):
        """
             Get all search results URL elements
        """
        elements = self.driver.find_elements(*self.locator.GOOGLE_URL_XPATH)
        url_of_title = []

        """
             Get Text from all search result URL elements
        """

        for value in elements:
            cell_value = value.text
            url_of_title.append(cell_value)
        return url_of_title

    def get_google_search_results_description(self):
        """
            Get all search results Description elements
        """
        elements = self.driver.find_elements(*self.locator.GOOGLE_DESCRIPTION_XPATH)
        des_of_title = []
        """
            Get Text from all search result Description elements
        """
        for value in elements:
            cell_value = value.text
            des_of_title.append(cell_value)
        return des_of_title

    def make_start_page_search(self, input_text):
        self.go_to_page(self.startPageURL)
        self.wait.until(EC.visibility_of_element_located(self.locator.STARTPAGE_SEARCH_INPUT_ID))
        self.driver.find_element(*self.locator.STARTPAGE_SEARCH_INPUT_ID).send_keys(input_text)
        self.driver.find_element(*self.locator.STARTPAGE_SEARCH_INPUT_ID).send_keys(Keys.RETURN)

    def get_startpage_search_results_title(self):
        """
            Get all search results title elements
        """
        elements = self.driver.find_elements(*self.locator.STARTPAGE_TITLE_XPATH)
        text_of_title = []

        """
             Get Text from all search result Description elements
        """
        for value in elements:
            cell_value = value.text
            text_of_title.append(cell_value)
        return text_of_title

    def get_startpage_search_results_URLS(self):
        """
           Get all search results URL elements
        """
        elements = self.driver.find_elements(*self.locator.STARTPAGE_URL_XPATH)
        url_of_title = []

        """
           Get Text from all search result URLS elements
        """
        for value in elements:
            cell_value = value.text
            url_of_title.append(cell_value)
        return url_of_title

    def get_start_page_results_description(self):
        """
            Get all search results description elements
        """
        elements = self.driver.find_elements(*self.locator.STARTPAGE_DESCRIPTION_XPATH)
        des_of_title = []
        """
            Get Text from all search result description elements
        """
        for value in elements:
            cell_value = value.text
            des_of_title.append(cell_value)
        return des_of_title
