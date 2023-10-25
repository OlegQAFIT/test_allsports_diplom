import time
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from helpers.base import BasePage


class ObjectPage(BasePage):
    BUTTON_OBJECT_TAB = '//ul/li/a[text()="Объекты"]'
    EXPECTED_URL = 'https://www.allsports.fit/by/objects/'
    TEXT_ON_OBJECT_PAGE = '//h3[text()="Ваши вопросы и ответы"]'
    TEXT_ON_OBJECT_PAGE_2 = '//h3[text()="Подписка в приложении Allsports выгоднее многих абонементов"]'
    TEXT_ON_OBJECT_PAGE_3 = '//h3[text()="Начните заниматься спортом со своими коллегами!"]'
    TEXT_ON_OBJECT_PAGE_4 = '//button[text()="Получить предложение"]'
    BUTTON_CALL_PUSH = '//a[@class="button blue" and text()="Позвоните нам"]'

    NAME_COMPANY = '//input[@name="company"]'

    NUMBER_EMPLOYE_LOCATOR = '//div[@class="select"]//button'
    TEXT_NUMBER_EMPLOYE = '//button[text()="от 100 до 1000"]'

    PHONE_NUMBER = '//input[@name="phone"]'
    CITY = '//input[@name="city"]'
    NAME_EMPLOY = '//section[2]/form/div[4]/input'
    EMAIL = '//input[@name="email"]'

    SUBSCRIPTION_LOCATOR = '//button[contains(text(), "Тип подписки")]'
    GOLD_LEVEL = '//*[@id="gatsby-focus-wrapper"]/main/div/div/div/main/section[1]/div[2]/div[1]/div[1]'
    INPUT_SEARCH = '//main/section[1]/form/div[2]/div[2]/input'
    SUPPLIER_LOCATOR = '//button[@class="result" and text()="Бассейн Гимназии 14"]'
    FOUND_ELEMENT = '//main/section[1]/section/section/h1'

    def __init__(self, driver):
        self.text_company_email = 'test@gmail.com'
        self.text_phone_number = '375 29 111 22 33'
        self.text_city = 'Минск'
        self.text_name_employe = 'Олег'
        self.text_email = 'test@gmail.com'
        self.text_impute = 'Бассейн Гимназии'
        self.driver = driver

    def open(self):
        self.driver.get('https://www.allsports.fit/by/')

    @allure.step("Click on 'Objects' Tab")
    def click_on_tab_objects(self):
        self.hard_click(self.BUTTON_OBJECT_TAB)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//h3[text()="Ваши вопросы и ответы"]')))

    @allure.step("Assert Current Page URL")
    def assert_checking_current_page_url(self):
        self.assert_url_matches(self.EXPECTED_URL)

    @allure.step("Assert Found Elements on 'Object' Page")
    def assert_found_elements_on_object_page(self):
        elements_to_check = [
            (self.TEXT_ON_OBJECT_PAGE, 'Ваши вопросы и ответы'),
            (self.TEXT_ON_OBJECT_PAGE_2, 'Подписка в приложении Allsports выгоднее многих абонементов'),
            (self.TEXT_ON_OBJECT_PAGE_3, 'Начните заниматься спортом со своими коллегами!'),
            (self.TEXT_ON_OBJECT_PAGE_4, 'Получить предложение')
        ]
        for element, expected_text in elements_to_check:
            self.assert_element_text_equal(element, expected_text)

    @allure.step("Assert Active Element on 'Object' Page")
    def assert_activ_element_on_object_page(self):
        self.assert_element_enabled(self.BUTTON_CALL_PUSH)

    @allure.step("Fill Form")
    def fill_form(self, NAME_COMPANY, PHONE_NUMBER, CITY,
                  NAME_EMPLOY, EMAIL):
        self.fill(NAME_COMPANY, self.text_company_email)
        self.fill(PHONE_NUMBER, self.text_phone_number)
        self.fill(CITY, self.text_city)
        self.fill(NAME_EMPLOY, self.text_name_employe)
        self.fill(EMAIL, self.text_email)

    @allure.step("Click 'Get'")
    def click_get(self):
        self.hard_click(self.TEXT_ON_OBJECT_PAGE_4)

    @allure.step("Assert Form")
    def assert_form(self):
        time.sleep(2)
        self.handle_alert("Спасибо! Мы скоро свяжемся с вами!")

    @allure.step("Click 'Drop'")
    def drop_click(self):
        self.hard_click(self.NUMBER_EMPLOYE_LOCATOR)
        self.hard_click(self.TEXT_NUMBER_EMPLOYE)

    @allure.step("Select 'Gold' Level")
    def select_gold_level(self):
        self.hard_click(self.SUBSCRIPTION_LOCATOR)
        self.hard_click(self.GOLD_LEVEL)

    @allure.step("Click 'Search'")
    def found_search_click(self):
        self.fill(self.INPUT_SEARCH, self.text_impute)

    @allure.step("Click 'Supplier'")
    def click_supplier(self):
        self.hard_click(self.SUPPLIER_LOCATOR)

    @allure.step("Assert Element")
    def assert_element(self):
        self.wait_for_element_is_displayed(self.FOUND_ELEMENT)
