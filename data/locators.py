from selenium.webdriver.common.by import By


class SearchPageLocators:
    """
       Google Page Locators
    """

    SEARCH_INPUT = (By.XPATH, "//input[@name='q']")
    GOOGLE_URL_XPATH = (By.XPATH, "//div[@class='yuRUbf']/a/div/cite")
    GOOGLE_TITLE_XPATH = (By.XPATH, "//div[@class='yuRUbf']/a/h3")
    GOOGLE_DESCRIPTION_XPATH = (By.XPATH, "//div[@class='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf']/span")

    """
       Start Page Locators
    """
    STARTPAGE_SEARCH_INPUT_ID = (By.XPATH, "//input[@id='q']")
    STARTPAGE_TITLE_XPATH = (By.XPATH, "//div[@class='w-gl__result-second-line-container']/a/h3")
    STARTPAGE_URL_XPATH = (By.XPATH, "//div[@class='w-gl__result-url-container']/a[2]")
    STARTPAGE_DESCRIPTION_XPATH = (By.XPATH, "//p[@class='w-gl__description']")
