import allure

from helpers import BasePage


class HeaderElement(BasePage):
    object_locator = '//ul/li/a[text()="Объекты"]'
    subscription_types_locator = '//ul/li/a[text()="Типы подписок"]'
    become_partner_locator = '//ul/li/a[text()="Стать партнером"]'
    contacts_locator = '//ul/li/a[text()="Контакты"]'
    locale_dropdown_selection = '//button[@class="button-select"]'
    found_text_on_object_page = 'выберите подписку'
    found_text_on_subscription_types_pege = 'Типы подписки'
    found_text_on_become_partner_pege = 'Развивайте ваш бизнес с нами!'
    found_text_on_contacts_pege = 'Контакты'
    BY_locale = '//a[@href="/by/"]'
    AM_locale = '//a[@href="/am/"]'
    AM_EN_locale = '//a[@href="/en_am/"]'
    RU_locale = '//a[@href="/ru/"]'
    found_text_on_BY_locale = 'Минск'
    found_text_on_AM_locale = 'Գյումրի'
    found_text_on_AM_EN_locale = 'Վանաձոր'
    found_text_on_RU_locale = 'Нижний Новгород'
    city_locator = '//div[@class="city-region-select"]//button[@class="empty"]'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.allsports.fit/by/')

    @allure.step("Open the web page")
    def open(self):
        self.driver.get('https://www.allsports.fit/by/')

    @allure.step("Click on 'Objects' button")
    def click_on_button_objects(self):
        self.click_on(self.object_locator)

    @allure.step("Click on 'Subscription Types' button")
    def click_on_button_subscription_types(self):
        self.click_on(self.subscription_types_locator)

    @allure.step("Click on 'Become a Partner' button")
    def click_on_button_become_partner(self):
        self.click_on(self.become_partner_locator)

    @allure.step("Click on 'Contacts' button")
    def click_on_button_contacts(self):
        self.click_on(self.contacts_locator)

    @allure.step("Click on 'Locale Dropdown' button")
    def click_on_button_locale_dropdown(self):
        self.click_on(self.locale_dropdown_selection)

    @allure.step("Click on 'BY' locale link")
    def click_on_BY(self):
        self.click_on(self.BY_locale)

    @allure.step("Click on 'AM' locale link")
    def click_on_AM(self):
        self.click_on(self.AM_locale)

    @allure.step("Click on 'AM EN' locale link")
    def click_on_AM_EN(self):
        self.click_on(self.AM_EN_locale)

    @allure.step("Click on 'RU' locale link")
    def click_on_RU(self):
        self.click_on(self.RU_locale)

    @allure.step("Click on 'Select City Dropdown' button")
    def click_on_select_city_dropdown(self):
        self.click_on(self.city_locator)

    @allure.step("Assert current object page")
    def assert_current_object_page(self):
        self.assert_text_on_page(self.found_text_on_object_page)

    @allure.step("Assert current subscription types page")
    def assert_current_subscription_types_page(self):
        self.assert_text_on_page(self.found_text_on_subscription_types_pege)

    @allure.step("Assert current become a partner page")
    def assert_current_become_partner_page(self):
        self.assert_text_on_page(self.found_text_on_become_partner_pege)

    @allure.step("Assert current contacts page")
    def assert_current_contacts_page(self):
        self.assert_text_on_page(self.found_text_on_contacts_pege)

    @allure.step("Assert city by AM locale visibility")
    def assert_city_by_locale_AM_visible(self):
        self.assert_text_on_page(self.found_text_on_AM_locale)

    @allure.step("Assert city by BY locale visibility")
    def assert_city_by_locale_BY_visible(self):
        self.assert_text_on_page(self.found_text_on_BY_locale)

    @allure.step("Assert city by AM EN locale visibility")
    def assert_city_by_locale_AM_EN_visible(self):
        self.assert_text_on_page(self.found_text_on_AM_EN_locale)

    @allure.step("Assert city by RU locale visibility")
    def assert_city_by_locale_RU_visible(self):
        self.assert_text_on_page(self.found_text_on_RU_locale)
