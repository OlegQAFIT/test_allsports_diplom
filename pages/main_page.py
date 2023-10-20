import time
import allure
from selenium.common import WebDriverException
from helpers.base import BasePage


class MainPage(BasePage):
    level = '//form/div[2]/div[3]/div/label[2]/div'
    type_subscription_locator = '//form/div[2]/div[3]/button'
    city_select = '//button[contains(text(), "Город/Район")]'
    activ_select = '//button[contains(text(), "Активности")]'
    possibilities_select = '//button[@class="empty" and contains(., "Доп. возможности")]'
    email_locator = '//main/section[1]/form/div/input'
    email_locator_2 = '//div[@class="input"]/input[@name="email"]'
    get_locator = '//section[1]/form/button'
    name_locator = '//section[7]/form/div[1]/input'
    phone_locator = '//section[7]/form/div[5]/input'
    city_locator = '//section[7]/form/div[2]/input'
    employe_locator = '//section[7]/form/div[4]/input'
    value_locator = '//form/div[3]/button'
    option_locator = '//section[7]/form/div[3]/div/button[1]'
    get_2_locator = '//main/section[7]/form/button'
    locator_on_main_page = '//h1[@class="top_title"][text()="Сервис Allsports"]'
    locator_on_main_page_2 = '//h1[@class="title"]'
    locator_on_main_page_3 = '//h3[text()="Делаем спорт частью корпоративной жизни"]'
    locator_on_main_page_4 = '//div[@class="title"][text()="Отзывы наших клиентов"]'
    platinum_level = '//label[text()="Платиновая"]'
    region_level_1 = '//label[text()="Региональная"]'
    grodno_city = '//*[@id="gatsby-focus-wrapper"]/main/div/div/div/main/section[2]/form/div[2]/div[4]/div/label[1]/div/label'
    gomel_city_1 = '//label[text()="Гомель"]'
    pool = '//label[text()="Сауна"]'
    pool_1 = '//label[text()="Бассейн"]'
    reservation_required_1 = '//label[text()="Требуется бронирование"]'
    reservation_required = '//label[text()="Требуется бронирование"]'
    supplier = '//button[contains(text(), "Школа плавания (Дворец творчества детей и молодёжи)")]'
    sipplier_2 = '//button[contains(text(), "Бассейн “Волна”")]'

    def __init__(self, driver):
        self.text_employe = 'Олег'
        self.text_city = 'Минск'
        self.text_phone = '375 29 111 22 33'
        self.text_name = 'ОАО Проверка'
        self.text_email = 'test@gmail.com'
        self.driver = driver

    def open(self):
        self.driver.get('https://www.allsports.fit/by/')

    @allure.step("Select Platinum Level")
    def select_platinum_level(self):
        self.click_and_select_option_in_dropdown(self.type_subscription_locator, self.platinum_level)

    @allure.step("Select Regional Level")
    def select_region_level(self):
        self.click_and_select_option_in_dropdown(self.type_subscription_locator, self.region_level_1)

    @allure.step("Select Gomel City")
    def select_gomel_city_1(self):
        self.click_and_select_option_in_dropdown(self.city_select, self.gomel_city_1)

    @allure.step("Select Grodno City")
    def select_grodno_city_1(self):
        self.click_and_select_option_in_dropdown(self.city_select, self.grodno_city)

    @allure.step("Select Activity")
    def select_activ(self):
        self.click_and_select_option_in_dropdown(self.activ_select, self.pool_1)

    @allure.step("Select Activity")
    def select_activ_1(self):
        self.click_and_select_option_in_dropdown(self.activ_select, self.pool)

    @allure.step("Select Possibilities")
    def select_possibilities(self):
        self.click_and_select_option_in_dropdown(self.possibilities_select, self.reservation_required_1)

    @allure.step("Select Possibilities")
    def select_possibilities_1(self):
        self.click_and_select_option_in_dropdown(self.possibilities_select, self.reservation_required)

    @allure.step("Click on Subscription")
    def clc(self):
        self.hard_click(self.type_subscription_locator)

    @allure.step("Click on Type Subscription")
    def click_on_type_subscription(self):
        self.hard_click(self.type_subscription_locator)

    @allure.step("Assert Supplier Found")
    def assert_found_supplier_1(self):
        self.assert_element_present(self.sipplier_2)

    @allure.step("Assert Supplier Found")
    def assert_found_supplier(self):
        self.assert_element_present(self.supplier)

    @allure.step("Assert Reservation Found")
    def assert_found_reservation(self):
        self.hard_click(self.reservation_required)

    @allure.step("Assert visible element")
    def assert_main(self):
        self.wait_for_visible(self.level)

    @allure.step("Enter Email")
    def enter_email(self):
        self.fill(self.email_locator, self.text_email)

    @allure.step("Enter Email")
    def enter_email_2(self):
        self.fill(self.email_locator_2, self.text_email)

    @allure.step("Click on locator")
    def clc_get_1(self):
        self.hard_click(self.get_locator)

    @allure.step("Click on Dropdown")
    def drop_clc(self):
        self.hard_click(self.value_locator)
        self.hard_click(self.option_locator)

    @allure.step("Fill Form")
    def fill_form(self, email_locator, name_locator, phone_locator, city_locator, employe_locator):
        self.fill(email_locator, self.text_email)
        self.fill(name_locator, self.text_name)
        self.fill(phone_locator, self.text_phone)
        self.fill(city_locator, self.text_city)
        self.fill(employe_locator, self.text_employe)

    @allure.step("Click Get")
    def clc_get_2(self):
        self.hard_click(self.get_2_locator)

    @allure.step("Assert Form")
    def assert_form(self):
        time.sleep(2)
        self.handle_alert("Спасибо! Мы скоро свяжемся с вами!")

    @allure.step("Assert Found Elements on Main Page")
    def assert_found_elements_on_main_page(self):
        elements_to_check = [
            (self.locator_on_main_page, 'Сервис Allsports'),
            (self.locator_on_main_page_2, 'Заголовок 2'),
            (self.locator_on_main_page_3, 'Делаем спорт частью корпоративной жизни'),
            (self.locator_on_main_page_4, 'Отзывы наших клиентов')
        ]

        found_elements = []

        for locator, expected_text in elements_to_check:
            try:
                element = self.wait_for_visible(locator)
                found_text = element.text
                found_elements.append((locator, found_text))
            except WebDriverException:
                assert False, f"Элемент с локатором '{locator}' и текстом '{expected_text}' отсутствует на странице."

        for locator, found_text in found_elements:
            print(f"Найден элемент с локатором '{locator}' и текстом '{found_text}'")
