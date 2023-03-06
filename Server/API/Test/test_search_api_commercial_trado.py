

from Server.API.Constants.search_constants import SearchConstrants
import requests
import allure


class TestLogin_API:
    @allure.description('test_search_api_using_existing_product')
    def test_search_api_using_existing_product(self):
        url = SearchConstrants.url
        data = SearchConstrants.valid_existing_data
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5


    @allure.description('test_search_api_using_non_existing_product')
    def test_search_api_using_non_existing_product(self):
        url = SearchConstrants.url
        data = SearchConstrants.invalid_non_exsting_product
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_search_api_using_null_data')
    def test_search_api_using_null_data(self):
        url = SearchConstrants.url
        data = SearchConstrants.invalid_null_data
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_search_api_using_invalid_number_value')
    def test_search_api_using_invalid_number_value(self):
        url = SearchConstrants.url
        data = SearchConstrants.invalid_number_value
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5


    @allure.description('test_search_api_using_invalid_special_character')
    def test_search_api_using_invalid_special_character(self):
        url = SearchConstrants.url
        data = SearchConstrants.invalid_special_character
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_search_api_using_invalid_space_data')
    def test_search_api_using_invalid_space_data(self):
        url = SearchConstrants.url
        data = SearchConstrants.invalid_space_data
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_search_api_using_invalid_number_and_special')
    def test_search_api_using_invalid_number_and_special(self):
        url = SearchConstrants.url
        data = SearchConstrants.invalid_number_and_special
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_search_api_using_invalid_number_and_string')
    def test_search_api_using_invalid_number_and_string(self):
        url = SearchConstrants.url
        data = SearchConstrants.invalid_number_and_string
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5


    @allure.description('test_search_api_using_invalid_special_and_string')
    def test_search_api_using_invalid_special_and_string(self):
        url = SearchConstrants.url
        data = SearchConstrants.invalid_special_and_string
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('invalid_only_one_character')
    def test_search_api_using_invalid_only_one_character(self):
        url = SearchConstrants.url
        data = SearchConstrants.invalid_only_one_character
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_search_api_using_invalid_multiple_string_product')
    def test_search_api_using_invalid_multiple_string_product(self):
        url = SearchConstrants.url
        data = SearchConstrants.invalid_multiple_string_product
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5



