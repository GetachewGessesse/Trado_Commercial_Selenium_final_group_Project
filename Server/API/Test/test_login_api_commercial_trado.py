from Server.API.Constants.login_constants_trado_commercial import LoginConstants
import requests
import allure


class TestLogin_API:
    @allure.description('Login correctly')
    def test_login_correctly(self):
        url = LoginConstants.url
        data = LoginConstants.valid_phone_valid_valid_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_login_with_invalid_phone_invalid_code')
    def test_login_with_invalid_phone_invalid_code(self):
        url = LoginConstants.url
        data = LoginConstants.invalid_phone_invalid_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code ==200
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_login_with_null_phone_null_code')
    def test_login_with_null_phone_null_code(self):
        url = LoginConstants.url
        data = LoginConstants.null_phone_null_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5


    @allure.description('test_login_with_valid_phone_invalid_code')
    def test_login_with_valid_phone_invalid_code(self):
        url = LoginConstants.url
        data = LoginConstants.valid_phone_invalid_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5


    @allure.description('test_login_with_invalid_phone_valid_code')
    def test_login_with_invalid_phone_valid_code(self):
        url = LoginConstants.url
        data = LoginConstants.invalid_phone_valid_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_login_with_valid_phone_null_code')
    def test_login_with_valid_phone_null_code(self):
        url = LoginConstants.url
        data = LoginConstants.valid_phone_null_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_login_with_null_phone_valid_code')
    def test_login_with_null_phone_valid_code(self):
        url = LoginConstants.url
        data = LoginConstants.null_phone_valid_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_login_with_invalid_phone_null_code')
    def test_login_with_invalid_phone_null_code(self):
        url = LoginConstants.url
        data = LoginConstants.invalid_phone_null_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5


    @allure.description('test_login_with_null_phone_invalid_code')
    def test_login_with_null_phone_invalid_code(self):
        url = LoginConstants.url
        data = LoginConstants.null_phone_invalid_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_login_with_longValue_phone_valid_code')
    def test_login_with_longValue_phone_valid_code(self):
        url = LoginConstants.url
        data = LoginConstants.longValue_phone_valid_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_login_with_short_value_phone_valid_code')
    def test_login_with_short_value_phone_valid_code(self):
        url = LoginConstants.url
        data = LoginConstants.short_value_phone_valid_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_login_with_longValue_phone_invalid_code')
    def test_login_with_longValue_phone_invalid_code(self):
        url = LoginConstants.url
        data = LoginConstants.longValue_phone_invalid_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5


    @allure.description('test_login_with_short_value_phone_invalid_code')
    def test_login_with_short_value_phone_invalid_code(self):
        url = LoginConstants.url
        data = LoginConstants.short_value_phone_invalid_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_login_with_long_value_phone_null_code')
    def test_login_with_long_value_phone_null_code(self):
        url = LoginConstants.url
        data = LoginConstants.long_value_phone_null_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5


    @allure.description('test_login_with_short_value_phone_null_code')
    def test_login_with_short_value_phone_null_code(self):
        url = LoginConstants.url
        data = LoginConstants.short_value_phone_null_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5


    @allure.description('test_login_with_valid_phone_long_value_code')
    def test_login_with_valid_phone_long_value_code(self):
        url = LoginConstants.url
        data = LoginConstants.valid_phone_long_value_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5


    @allure.description('test_login_with_valid_value_phone_ShortValue_code')
    def test_login_with_valid_value_phone_ShortValue_code(self):
        url = LoginConstants.url
        data = LoginConstants.valid_value_phone_ShortValue_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_login_with_stringValue_phone_valid_code')
    def test_login_with_stringValue_phone_valid_code(self):
        url = LoginConstants.url
        data = LoginConstants.stringValue_phone_valid_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_login_with_valid_phone_stringValue_code')
    def test_login_with_valid_phone_stringValue_code(self):
        url = LoginConstants.url
        data = LoginConstants.valid_phone_stringValue_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code ==200
        assert res.elapsed.total_seconds() < 5


    @allure.description('test_login_with_SpecialCharacterValue_phone_valid_code')
    def test_login_with_SpecialCharacterValue_phone_valid_code(self):
        url = LoginConstants.url
        data = LoginConstants.SpecialCharacterValue_phone_valid_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5

    @allure.description('test_login_with_valid_phone_SpecialCharacter_code')
    def test_login_with_valid_phone_SpecialCharacter_code(self):
        url = LoginConstants.url
        data = LoginConstants.valid_phone_SpecialCharacter_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5