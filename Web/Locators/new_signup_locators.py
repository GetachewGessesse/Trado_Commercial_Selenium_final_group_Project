
class SignupLocators:

    website = "https://qa.trado.co.il/"
    connection_className = "header_userAreaLink"
    option1_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[2]'
    option2_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]'
    save = '//*[@id="root"]/div/div[4]/div/div/div/button'
    signup_link_xpath = "//span[contains(text(),'הרשם')]"
    login_facebook_button_className = 'login_facebook'
    login_google_button_className = 'login_google'
    login_twitter_button_className = 'login_twitter'
    login_phone_input_xpath = "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]/input[1]"
    user_name_xpath = "//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[5]/label[1]/div[1]/div[2]"
    password_xpath = "//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[5]/label[2]/div[1]/div[3]"
    login_button_class_name = "form_submitBtn"
    privacy_policy_checkbox_xpath = "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/span[1]/span[1]/span[1]/i[1]"
    business_number_field_xpath = "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]/input[1]"
    privacy_poicy_error_message_xpath = "//div[contains(text(),'please approve our policy')]"