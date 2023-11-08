from charset_normalizer import detect

import allure

from helpers import BasePage


class Local(BasePage):
    LOCAL = "//div[@class='country-switch']//button[@class='button-select']"
    LOCAL_BU = "//div[@class='country-switch']//div[@class='link-item'][1]/a"
    LOCAL_AM = "//div[@class='country-switch']//div[@class='link-item'][2]/a"
    LOCAL_AM_EN = "//div[@class='country-switch']//div[@class='link-item'][3]/a"
    LOCAL_RU = "//div[@class='country-switch']//div[@class='link-item'][4]/a"

    OBJECTS = "//div[@class='list-wrapper']/ul/li[1]/a"
    SUBSCRIPTION_TYPES = "//div[@class='list-wrapper']/ul/li[2]/a"
    VIEW_OLL = '//*[@id="gatsby-focus-wrapper"]/main/div/div/main/section[1]/div[3]/div[2]/div'
    CLOSE = '//*[@id="gatsby-focus-wrapper"]/main/div/div/main/section[1]/div[10]/header/button'
    BECOME_PARTNER = "//div[@class='list-wrapper']/ul/li[3]/a"
    CONTACTS = "//div[@class='list-wrapper']/ul/li[4]/a"

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Click on 'ALLSPORTS' page")
    def open(self):
        self.driver.get('https://www.allsports.fit/by/')

    @allure.step("Click on 'Objects' page")
    def click_on_objects_page(self):
        self.hard_click(self.OBJECTS)

    @allure.step("Click on 'Subscription Types' page")
    def click_on_subscription_types_page(self):
        self.hard_click(self.SUBSCRIPTION_TYPES)

    @allure.step("Click on 'View All' button")
    def click_on_view_oll_buttom(self):
        self.hard_click(self.VIEW_OLL)

    @allure.step("Click on 'Close' button")
    def click_on_close_buttom(self):
        self.hard_click(self.CLOSE)

    @allure.step("Click on 'Become Partner' page")
    def click_on_become_partner_page(self):
        self.hard_click(self.BECOME_PARTNER)

    @allure.step("Click on 'Contacts' page")
    def click_on_contacts_page(self):
        self.hard_click(self.CONTACTS)

    @allure.step("Select Armenian locale from the dropdown")
    def drop_click_local_am(self):
        self.hard_click(self.LOCAL)
        self.hard_click(self.LOCAL_AM)

    @allure.step("Select Armenian-English locale from the dropdown")
    def drop_click_local_am_en(self):
        self.hard_click(self.LOCAL)
        self.hard_click(self.LOCAL_AM_EN)

    @allure.step("Select Russian locale from the dropdown")
    def drop_click_local_ru(self):
        self.hard_click(self.LOCAL)
        self.hard_click(self.LOCAL_RU)

    @allure.step("Asserting no Russian words on Armenian locale")
    def assert_no_russian_words_on_am_locale(self):
        super().found_other_language_words('ru')

    @allure.step("Asserting no Armenian words on Russian locale")
    def assert_no_armenia_words_on_ru_locale(self):
        super().found_other_language_words('am')

    @allure.step("Asserting no Russian words on Armenian-English locale")
    def assert_no_russian_words_on_am_en_locale(self):
        super().found_other_language_words('ru')

    @allure.step("Asserting no Armenian words on Belarusian locale")
    def assert_no_armenia_words_on_by_locale(self):
        super().found_other_language_words('am')
