import pytest
from config.config_reader import ConfigReader
from pages.main_page import MainPage
from pages.article_page import ArticlePage

@pytest.mark.parametrize("search_request", ['Нос', 'Шнобель'])
def test_requesting_test_in_article_title(search_request, driver):
    config_reader = ConfigReader()
    driver.get(config_reader.get_base_url())
    main_page = MainPage(driver)
    article_page = ArticlePage(driver)

    main_page.wait_to_load_page()
    main_page.input_search_request(search_request)

    article_page.wait_to_load_page()
    assert search_request == article_page.get_title()