class Locators():

    #HomePage Locators
    sign_in_button_xpath = "//*[@id='nav-link-accountList']"

    #EmailPage Locators
    email_textbox_id = "ap_email"
    email_continue_id = "continue"

    #PasswordPage Locators
    password_textbox_id = "ap_password"
    password_sign_in_button_id = "signInSubmit"

    #SearchArea Locators
    search_textbox_id = "twotabsearchtextbox"
    search_button_xpath = "//*[@id='nav-search']/form/div[2]/div/input"

    #PageNumberAndProduct Locators
    page_number_link_text = "2"
    click_third_product_xpath = "//*[@id='search']/div[1]/div[2]/div/span[4]/div[1]/div[3]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span"

    #AddAndDeleteWishList Locators
    get_text_id = "productTitle"
    add_to_list_button_id = "add-to-wishlist-button-submit"
    wish_list_xpath = "//*[@id='WLNEW_section_wlType']/div[2]/div[2]/div/div"
    create_list_button_xpath = "//*[@id='WLNEW_create']/span/span/input"
    view_list_button_link_text = "View List"
    delete_from_wish_list_xpath = "//*[@id='a-autoid-7']/span/input"