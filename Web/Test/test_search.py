import pytest
from Web.Page.search_page import Search
import time
import allure

class Test_search:

    @allure.description('test_the_existing_product')
    @pytest.mark.sanity
    def test_the_existing_product(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("milk")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('milk')
        assertion = search.assertion_for_existing_product
        assert "goats milk" == assertion

    @allure.description('test_non_existing_product')
    @pytest.mark.sanity
    def test_non_existing_product(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("cow")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('cow')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "0 תוצאות" == assertion

    @allure.description('test_to_insert_numbers_into_the_search_box')
    @pytest.mark.sanity
    def test_to_insert_numbers_into_the_search_box(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("12345")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('12345')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "0 תוצאות" == assertion

    @allure.description('test_to_search_without_inserting_any_products ')
    @pytest.mark.sanity
    def test_to_search_without_inserting_any_products  (self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box(" ")
        time.sleep(2)
        search.send_keys_on_search_box_second_time(' ')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "" == assertion

    @allure.description('test_to_search_by_inserting_the_single_letter ')
    @pytest.mark.sanity
    def test_to_search_by_inserting_the_single_letter(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box(" ש ")
        time.sleep(2)
        search.send_keys_on_search_box_second_time(' ש ')
        time.sleep(2)
        assertion = search.assertion_for_existing_product
        assert "Hennessy VSOP Privilege Cognac" == assertion

    @allure.description('test_that_the_search_results_are_sorted_correctly')
    @pytest.mark.sanity
    def test_that_the_search_results_are_sorted_correctly(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box(" milk ")
        time.sleep(2)
        search.send_keys_on_search_box_second_time(' milk ')
        time.sleep(2)

    @allure.description('test_that_the_search_functionality_works_correctly_when_multiple_search_terms_are_used')
    @pytest.mark.sanity
    def test_that_the_search_functionality_works_correctly_when_multiple_search_terms_are_used(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("milk,goats milk")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('milk,goats milk')
        time.sleep(2)
        assertion = search.assertion_for_existing_product
        assert "goats milk" == assertion

    @allure.description('test_that_the_search_functionality_works_correctly_when_multiple_search_terms_are_used')
    @pytest.mark.sanity
    def test_that_entering_an_invalid_search_term_and_verifying_that_no_results_are_displayed(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("dhhhdh@gmail.com")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('dhhhdh@gmail.com')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "0 תוצאות" == assertion

    @allure.description('test_to_search_multiple_words')
    @pytest.mark.sanity
    def test_to_search_multiple_words(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("diaper,milk,coca cola")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('diaper,milk,coca cola')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "0 תוצאות" == assertion

    @allure.description('test_to_search_term_with_special_characters_and_verify_that_the_correct_results_are_displayed')
    @pytest.mark.sanity
    def test_to_enter_a_search_term_with_special_characters_and_verify_that_the_correct_results_are_displayed(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("@milk,")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('@milk')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "0 תוצאות" == assertion

    @allure.description('test_that_the_search_functionality_works_as_expected_when_the_search_term_is_a_misspelling')
    @pytest.mark.sanity
    def test_that_the_search_functionality_works_as_expected_when_the_search_term_is_a_misspelling(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("@milk,")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('@milk')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "0 תוצאות" == assertion

    @allure.description('test_that_the_search_functionality_by_searching_for_a_term_with_uppercase_letters')
    @pytest.mark.sanity
    def test_that_the_search_functionality_by_searching_for_a_term_with_uppercase_letters(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("MILK")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('MILK')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "2 תוצאות" == assertion


    @allure.description('test_that_the_search_functionality_by_searching_for_a_term_with_lowercase_letters')
    @pytest.mark.sanity
    def test_that_the_search_functionality_by_searching_for_a_term_with_lowercase_letters(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("milk")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('milk')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "2 תוצאות" == assertion
        print(assertion)

    @allure.description('test_that_the_search_functionality_by_searching_for_a_term_with_lowercase_and_uppercase_letters')
    @pytest.mark.sanity
    def test_that_the_search_functionality_by_searching_for_a_term_with_lowercase_and_uppercase_letters(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("miLK")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('miLK')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "2 תוצאות" == assertion
        print(assertion)

    @allure.description('test_to_search_term_with_special_characters_and_verify_that_the_correct_results_are_displayed')
    @pytest.mark.sanity
    def test_to_enter_a_search_term_with_special_characters_and_verify_that_the_correct_results_are_displayed(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("@milk,")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('@milk')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "0 תוצאות" == assertion

    @allure.description('test_that_the_search_functionality_works_as_expected_when_the_search_term_is_a_misspelling')
    @pytest.mark.sanity
    def test_that_the_search_functionality_works_as_expected_when_the_search_term_is_a_misspelling(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("@milk,")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('@milk')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "0 תוצאות" == assertion

    @allure.description('test_that_the_search_functionality_by_searching_for_a_term_with_uppercase_letters')
    @pytest.mark.sanity
    def test_that_the_search_functionality_by_searching_for_a_term_with_uppercase_letters(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("MILK")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('MILK')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "2 תוצאות" == assertion

    @allure.description('test_that_the_search_functionality_by_searching_for_a_term_with_lowercase_letters')
    @pytest.mark.sanity
    def test_that_the_search_functionality_by_searching_for_a_term_with_lowercase_letters(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("milk")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('milk')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "2 תוצאות" == assertion


    @allure.description(
        'test_that_the_search_functionality_by_searching_for_a_term_with_lowercase_and_uppercase_letters')
    @pytest.mark.sanity
    def test_that_the_search_functionality_by_searching_for_a_term_with_lowercase_and_uppercase_letters(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("miLK")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('miLK')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "2 תוצאות" == assertion

    @allure.description('test_to_search_multiple_words')
    @pytest.mark.sanity
    def test_to_search_multiple_words(self):
        search = Search(self)
        search.open_trado()
        search.click_option1()
        search.click_option2()
        search.click_save_button()
        time.sleep(2)
        search.send_keys_on_search_box("diaper,milk,coca cola")
        time.sleep(2)
        search.send_keys_on_search_box_second_time('diaper,milk,coca cola')
        time.sleep(2)
        assertion = search.assertion_for_no_product
        assert "0 תוצאות" == assertion







