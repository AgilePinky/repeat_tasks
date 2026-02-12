from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config_reader import ConfigReader
from tests.driver_singleton import Driver

class MainPage:

    HEADER = (By.ID, 'mw-head')
    SEARCH_INPUT = (By.ID, 'searchInput')

    config_reader = ConfigReader()

    def __init__(self, driver, timeout=config_reader.get_timeout()):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def wait_to_load_page(self):
        self.wait.until(EC.visibility_of_element_located(self.HEADER))

    def input_search_request(self, search_request):
        self.wait.until(EC.element_to_be_clickable(SEARCH_INPUT)).input(search_request)