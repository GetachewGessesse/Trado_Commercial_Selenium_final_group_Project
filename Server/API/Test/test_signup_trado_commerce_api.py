

from Server.API.Constants.signup_constants_trado_commercial_api import SignupConstants
import requests
import allure


class TestLogin_API:
    @allure.description('test_signin_api_using_valid_phone')
    def test_signin_api_using_valid_phone(self):
        url = SignupConstants.url
        data = SignupConstants.valid_phone
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5


    @allure.description('test_signin_api_using_invalid_phone_less_than_10_digit')
    def test_signin_api_using_invalid_phone_less_than_10_digit(self):
        url = SignupConstants.url
        data = SignupConstants.invalid_phone_less_than_10_digit
        res = requests.post(url, data)
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_signin_api_using_invalid_phone_more_than_10_digit')
    def test_signin_api_using_invalid_phone_more_than_10_digit(self):
        url = SignupConstants.url
        data = SignupConstants.invalid_phone_more_than_10_digit
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5


    @allure.description('test_signin_api_using_invalid_phone_null_digit')
    def test_signin_api_using_invalid_phone_null_digit(self):
        url = SignupConstants.url
        data = SignupConstants.invalid_phone_null_digit
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_signin_api_using_invalid_stringValue_phone')
    def test_signin_api_using_invalid_stringValue_phone(self):
        url = SignupConstants.url
        data = SignupConstants.invalid_stringValue_phone
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_signin_api_using_invalid_specialCharacterValue_phone')
    def test_signin_api_using_invalid_specialCharacterValue_phone(self):
        url = SignupConstants.url
        data = SignupConstants.invalid_specialCharacterValue_phone
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_signin_api_using_invalid_string_and_specialValue_phone')
    def test_signin_api_using_invalid_string_and_specialValue_phone(self):
        url = SignupConstants.url
        data = SignupConstants.invalid_string_and_specialValue_phone
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5


    @allure.description('test_signin_api_using_invalid_string_and_integer_phone')
    def test_signin_api_using_invalid_string_and_integer_phone(self):
        url = SignupConstants.url
        data = SignupConstants.invalid_string_and_integer_phone
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5


    @allure.description('test_signin_api_using_invalid_special_and_integerValue_phone')
    def test_signin_api_using_invalid_special_and_integerValue_phone(self):
        url = SignupConstants.url
        data = SignupConstants.invalid_special_and_integerValue_phone
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5