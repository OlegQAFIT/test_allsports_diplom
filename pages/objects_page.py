import time
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from helpers.base import BasePage


class ObjectPage(BasePage):
    button_object_tab = '//ul/li/a[text()="Объекты"]'
    expected_url = 'https://www.allsports.fit/by/objects/'
    text_on_object_page = '//h3[text()="Ваши вопросы и ответы"]'
    text_on_object_page_2 = '//h3[text()="Подписка в приложении Allsports выгоднее многих абонементов"]'
    text_on_object_page_3 = '//h3[text()="Начните заниматься спортом со своими коллегами!"]'
    text_on_object_page_4 = '//button[text()="Получить предложение"]'
    buttom_call_push = '//a[@class="button blue" and text()="Позвоните нам"]'

    name_company_locator = '//input[@name="company"]'

    number_employe_locator = '//div[@class="select"]//button'
    text_number_employe = '//button[text()="от 100 до 1000"]'

    phone_number_locator = '//input[@name="phone"]'
    city_locator = '//input[@name="city"]'
    name_employ_locator = '//section[2]/form/div[4]/input'
    email_locator = '//input[@name="email"]'

    subscription_locator = '//button[contains(text(), "Тип подписки")]'
    gold_level = '//*[@id="gatsby-focus-wrapper"]/main/div/div/div/main/section[1]/div[2]/div[1]/div[1]'
    impute_search = '//main/section[1]/form/div[2]/div[2]/input'
    supplier_locator = '//button[@class="result" and text()="Бассейн Гимназии 14"]'
    found_element = '//main/section[1]/section/section/h1'

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
        self.hard_click(self.button_object_tab)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//h3[text()="Ваши вопросы и ответы"]')))

    @allure.step("Assert Current Page URL")
    def assert_checking_current_page_url(self):
        self.assert_url_matches(self.expected_url)

    @allure.step("Assert Found Elements on Object Page")
    def assert_found_elements_on_object_page(self):
        elements_to_check = [
            (self.text_on_object_page, 'Ваши вопросы и ответы'),
            (self.text_on_object_page_2, 'Подписка в приложении Allsports выгоднее многих абонементов'),
            (self.text_on_object_page_3, 'Начните заниматься спортом со своими коллегами!'),
            (self.text_on_object_page_4, 'Получить предложение')
        ]

    @allure.step("Assert Active Element on Object Page")
    def assert_activ_element_on_object_page(self):
        self.assert_element_enabled(self.buttom_call_push)

    @allure.step("Fill Form")
    def fill_form(self, name_company_locator, phone_number_locator, city_locator,
                  name_employ_locator, email_locator):
        self.fill(name_company_locator, self.text_company_email)
        self.fill(phone_number_locator, self.text_phone_number)
        self.fill(city_locator, self.text_city)
        self.fill(name_employ_locator, self.text_name_employe)
        self.fill(email_locator, self.text_email)

    @allure.step("Click 'Get'")
    def click_get(self):
        self.hard_click(self.text_on_object_page_4)

    @allure.step("Assert Form")
    def assert_form(self):
        time.sleep(2)
        self.handle_alert("Спасибо! Мы скоро свяжемся с вами!")

    @allure.step("Click 'Drop'")
    def drop_click(self):
        self.hard_click(self.number_employe_locator)
        self.hard_click(self.text_number_employe)

    @allure.step("Select Gold Level")
    def select_gold_level(self):
        self.hard_click(self.subscription_locator)
        self.hard_click(self.gold_level)

    @allure.step("Click 'Search'")
    def found_search_click(self):
        self.fill(self.impute_search, self.text_impute)

    @allure.step("Click 'Supplier'")
    def click_supplier(self):
        self.hard_click(self.supplier_locator)

    @allure.step("Assert Element")
    def assert_element(self):
        self.wait_for_element_is_displayed(self.found_element)
