import pytest

from pages.search_page import SearchPage
from tests.base_test import BaseTest


class TestSearch(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = SearchPage(self.driver, self.wait)
        self.page.go_to_search_page()

    def test_search_on_Google_and_search_on_Start_Page_and_compare_results(self, load_pages):
        """
            This test case will first search on Google and The Search on Start Page and then print out common
            search resutls in both engines.
        """

        search_input = 'Mango Man'

        self.page.make_a_Google_search(search_input)
        """
            Search on Google and collect results in a List
        """
        Google_List = self.page.get_google_search_results_title()

        self.page.make_start_page_search(search_input)
        """
            Search on Start Page and collect results in a List
        """
        Bing_List = self.page.get_startpage_search_results_title()

        print("\n""\n" "GOOGLE SEARCH RESULTS" "\n""\n" + "\n".join(Google_List))
        print("\n""\n" "START PAGE SEARCH RESULTS" "\n""\n" + "\n".join(Bing_List) + "\n""\n")

        """
            Compare and print common results in both search engines
        """
        print("\n""\n" "COMMON RESULTS IN BOTH ENGINES" "\n""\n" + "\n".join(set(Google_List).intersection(Bing_List)))

    def test_search_on_google(self, load_pages):
        """
            This Test case will search on Google and print results
        """
        search_input = 'Mango Man'

        self.page.make_a_Google_search(search_input)
        Google_List = self.page.get_google_search_results_title()

        print("\n""\n" "GOOGLE SEARCH RESULTS" "\n""\n" + "\n".join(Google_List))

        self.page.get_google_search_results_URLS()
        self.page.get_google_search_results_description()

    def test_search_on_bing(self, load_pages):
        """
            This Test case will search on Start Page and print results
        """

        search_input = 'Mango Man'

        self.page.make_start_page_search(search_input)
        Bing_List = self.page.get_startpage_search_results_title()
        self.page.get_startpage_search_results_URLS()
        self.page.get_start_page_results_description()

        print("\n""\n" "START PAGE SEARCH RESULTS" "\n""\n" + "\n".join(Bing_List))
