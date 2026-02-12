from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config_reader import ConfigReader
from tests.driver_singleton import Driver


class ArticlePage:
    HEADER = (By.ID, 'mw-head')
    TITLE = (By.ID, 'firstHeading')

    config_reader = ConfigReader()

    def __init__(self, driver, timeout=config_reader.get_timeout()):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def wait_to_load_page(self):
        self.wait.until(EC.visibility_of_element_located(self.HEADER))

    def get_title(self, search_request):
        return self.wait.until(EC.visibility_of_element_located(TITLE)).text