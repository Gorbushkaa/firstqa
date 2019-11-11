from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import csv


class YandexLocators:
    LOGIN = "FirstSelenium"
    PASSWORD = "a1qaa1qa"
    LOCATOR_YANDEX_ENTER_BUTTON_WITHOUT_JS = (By.XPATH, "//a[(contains(@class,'user__login'))"
                                                        " and not (contains(@class,'button2_js_inited'))]")
    LOCATOR_YANDEX_ENTER_BUTTON_WITH_JS = (By.XPATH, "//a[(contains(@class,'user__login')) "
                                                     "and (contains(@class,'button2_js_inited'))]")
    LOCATOR_YANDEX_LOGIN = (By.XPATH, "//*[@id='passp-field-login']")
    LOCATOR_YANDEX_PASSWORD = (By.XPATH, "//*[@id='passp-field-passwd']")
    LOCATOR_YANDEX_ENTER_BUTTON_LP = (By.XPATH, "//button[@type='submit']")
    LOCATOR_YANDEX_POPULAR_CATEGORY = (By.XPATH, "//a[contains(@class,'link n-w-tab__control b-zone b-spy-events')]")
    LOCATOR_YANDEX_OPENED_CATEGORY = (By.XPATH, "//h1[@class='_39qdPorEKz']")
    LOCATOR_YANDEX_BUTTON_ALL_CATEGORY = (By.XPATH, "//div[@class='n-w-tab__control-hamburger']")
    LOCATOR_YANDEX_ALL_CATEGORY = (By.XPATH, "//div[contains(@class,'n-w-tab n-w-tab_interaction_"
                                             "hover-navigation-menu n-w-tab_type_navigation-menu-vertical')]")
    LOCATOR_YANDEX_USER_PROFILE = (By.XPATH, "//a[contains(@class,'header2-user user i-bem user_js_inited')]")
    LOCATOR_YANDEX_USER_LOGOUT = (By.XPATH, "//a[contains(@class,'link user user__logout i-bem user_js_inited')]")
    LOCATOR_YANDEX_CURRENT_CATEGORY = (By.XPATH, "//h1[@class='_39qdPorEKz']")


class YandexT(BasePage):
    parent_window = ""
    category = []
    category_pop = []
    open_categ = ""
    current_categ = ""

    def enter(self):
        elem = self.find_element(YandexLocators.LOCATOR_YANDEX_ENTER_BUTTON_WITHOUT_JS)
        ActionChains(self.driver).move_to_element(elem).perform()
        self.find_element(YandexLocators.LOCATOR_YANDEX_ENTER_BUTTON_WITH_JS).click()

    def switch_window(self):
        self.parent_window = self.driver.current_window_handle
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_window_to_parent(self):
        self.driver.switch_to.window(self.parent_window)

    def logining(self):
        login = self.find_element(YandexLocators.LOCATOR_YANDEX_LOGIN)
        login.clear()
        login.send_keys(YandexLocators.LOGIN)
        self.find_element(YandexLocators.LOCATOR_YANDEX_ENTER_BUTTON_LP).click()
        self.driver.implicitly_wait(5)
        password = self.find_element(YandexLocators.LOCATOR_YANDEX_PASSWORD)
        password.send_keys(YandexLocators.PASSWORD)
        self.find_element(YandexLocators.LOCATOR_YANDEX_ENTER_BUTTON_LP).click()

    def open_category(self):
        a = self.random_category()
        self.find_elements(YandexLocators.LOCATOR_YANDEX_POPULAR_CATEGORY)[a].click()
        self.open_categ = self.find_element(YandexLocators.LOCATOR_YANDEX_CURRENT_CATEGORY).text

    def random_category(self):
        elems = self.find_elements(YandexLocators.LOCATOR_YANDEX_POPULAR_CATEGORY)
        a = 0
        for elem in elems:
            if elem.is_displayed():
                self.category_pop.append(elem.text)
                a += 1
        a = random.randint(0, a-2)
        self.current_categ = elems[a].text
        self.category_pop.pop(0)
        self.category_pop.remove("Журнал Маркета")
        return a

    def check_all_category(self):
        self.find_element(YandexLocators.LOCATOR_YANDEX_BUTTON_ALL_CATEGORY).click()
        category = self.find_elements(YandexLocators.LOCATOR_YANDEX_ALL_CATEGORY)
        with open("category.csv", "a+") as f:
            writer = csv.writer(f)
            for cat in category:
                self.category.append(cat.text)
                writer.writerow([str(cat.text)])

    def exit(self):
        button = self.find_elements(YandexLocators.LOCATOR_YANDEX_USER_PROFILE)[1]
        ActionChains(self.driver).move_to_element(button)
        self.driver.implicitly_wait(5)
        button.click()
        self.find_element(YandexLocators.LOCATOR_YANDEX_USER_LOGOUT).click()

    def check_category(self):
        a = True
        for i in self.category_pop:
            if i not in self.category:
                a = False
        return a






