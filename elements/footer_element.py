import allure

from helpers.base import BasePage


class FooterElement(BasePage):
    CONTACT_NUMBER = '//*[@href="tel:+375-44-525-38-92"]'
    CONTACT_EMAIL = '//*[@href="mailto:contact@allsports.by"]'
    INSTAGRAM = '//a[@href="https://www.instagram.com/allsports.fit/"]'
    LINKEDIN = '//a[@href="https://www.linkedin.com/company/allsportsby"]'
    BUTTON_EMPLOYEE = '//ul[@class="links"]/li[1]/a'
    BUTTON_FOR_PARTNERS = '//li/a[text()="Партнерам"]'
    BUTTON_CONTACTS = '//ul[@class="links"]/li[5]/a'
    BUTTON_DOCUMENTS_FOR_LEGAL_ENTITIES = '//li/a[text()="Документы для юр.лиц"]'
    BUTTON_COMPANY = '//li/a[text()="Компаниям"]'
    BUTTON_OBJECTS = '//ul[@class="links"]/li[4]/a'
    BUTTON_BLOG = '//li/a[text()="Блог"]'
    USER_AGREEMENTS = '//li/a[text()="Пользовательские соглашения"]'
    SUBSCRIPTION_TYPES = '//h1[text()="Типы подписки"]'
    FOUND_ELEMENTS_DELETE = '//button[@class="reset" and @title="Очистить фильтр"]'
    PARTNER = "//h3[text()='Что Allsports дает вашему фитнес-клубу?']"
    ELEMENT_IN_BLOG_PAGE = '//div[h1[text()="Оллспортс Статьи"]]/article'
    ACT_RESULT = '//div/div/main/section[1]/p[7]/a'
    COMPANIES_PAGE = '//h1[@class="top_title"]'
    DOCUMENTS_FOR_LEGAL_ENTITIES = "//h2[text()='Документы для юридических лиц']"
    EXPECTED_RESULT_TEXT = '+375 (44) 502-36-13'
    FILE_NAME = "Индивидуальные лицензии"
    PHONE_NUMBER = '+375 (44) 525-38-92'
    EXPECTED_ALERT_TEXT = "Открыть приложение 'Выбор приложения'"

    def __init__(self, driver):
        self.driver = driver
        self.main_window_handle = None

    @allure.step("Open the website")
    def open(self):
        self.driver.get('https://www.allsports.fit/by/')

    @allure.step("Click on 'Instagram' link")
    def click_on_instagram(self):
        self.click_on(self.INSTAGRAM)

    @allure.step("Click on 'Docs' link")
    def click_on_docs(self):
        self.click_on(self.USER_AGREEMENTS)

    @allure.step("Click on 'LinkedIn' link")
    def click_on_linkedin(self):
        self.click_on(self.LINKEDIN)

    @allure.step("Click on 'Employees' page")
    def click_on_employees_page(self):
        self.click_on(self.BUTTON_EMPLOYEE)

    @allure.step("Click on 'Partners' page")
    def click_on_partners_page(self):
        self.click_on(self.BUTTON_FOR_PARTNERS)

    @allure.step("Click on 'Contacts' page")
    def click_on_contacts_page(self):
        self.click_on(self.BUTTON_CONTACTS)

    @allure.step("Click on 'Agreements' page")
    def click_on_agreements_page(self):
        self.click_on(self.USER_AGREEMENTS)

    @allure.step("Click on 'Legal Documents' page")
    def click_on_legal_documents_page(self):
        self.click_on(self.DOCUMENTS_FOR_LEGAL_ENTITIES)

    @allure.step("Click on 'Company' page")
    def click_on_company_page(self):
        self.click_on(self.BUTTON_COMPANY)

    @allure.step("Click on 'Objects' page")
    def click_on_objects_page(self):
        self.click_on(self.BUTTON_OBJECTS)

    @allure.step("Click on 'Blog' page")
    def click_on_blog_page(self):
        self.click_on(self.BUTTON_BLOG)

    @allure.step("Assert dok")
    def assert_dok(self, file):
        if file in self.driver.page_source:
            print(f"Текст '{file}' найден на странице.")
        else:
            print(f"Текст '{file}' не найден на странице.")
        assert file in self.driver.page_source

    @allure.step("Assert Instagram")
    def assert_instagram(self):
        self.wait_for_visible(self.INSTAGRAM)
        current_url = self.get_current_url()
        print("Текущий URL (instagram):", current_url)
        assert self.get_current_url() == 'https://www.instagram.com/allsports.fit/'

    @allure.step("Assert LinkedIn")
    def assert_linkedin(self):
        self.wait_for_visible(self.LINKEDIN)
        current_url = self.get_current_url()
        print("Текущий URL (LinkedIn):", current_url)
        assert current_url == 'https://www.linkedin.com/company/allsportsby'

    @allure.step("Assert phone numbers and email")
    def assert_phone_numbers_email(self):
        self.assert_element_text_equal(self.CONTACT_NUMBER, '+375 (44) 525-38-92')
        self.assert_element_text_equal(self.CONTACT_EMAIL, 'contact@allsports.by')

    @allure.step("Assert text in 'Employees' page")
    def assert_text_in_page_employees(self):
        self.assert_element_text_equal(self.SUBSCRIPTION_TYPES, 'Типы подписки')

    @allure.step("Assert text in 'Partners' page")
    def assert_text_in_page_partners(self):
        self.assert_element_text_equal(self.PARTNER, 'Что Allsports дает вашему фитнес-клубу?')

    @allure.step("Assert phone")
    def assert_phone(self):
        self.assert_text_in_element(self.ACT_RESULT, self.EXPECTED_RESULT_TEXT)

    @allure.step("Assert text in Legal 'Documents' page")
    def assert_text_in_page_documents(self):
        self.assert_element_text_equal(self.DOCUMENTS_FOR_LEGAL_ENTITIES, 'Документы для юридических лиц')

    @allure.step("Assert element")
    def assert_element(self):
        self.wait_for_element_is_displayed(self.FOUND_ELEMENTS_DELETE)

    @allure.step("Assert element in 'Blog' page")
    def assert_element_blog(self):
        self.wait_for_element_is_displayed(self.ELEMENT_IN_BLOG_PAGE)

    @allure.step("Check the 'Companies' page")
    def assert_companies_page(self):
        self.wait_for_element_is_displayed(self.COMPANIES_PAGE)
