from Yandex import YandexT, YandexLocators
import os.path

def test_yandex_market(browser):
    yandex_market_page = YandexT(browser)
    yandex_market_page.go_to_site()
    assert yandex_market_page.driver.current_url == "https://market.yandex.ru/", \
                                                    "Мы не перешли на главуню страницу"
    yandex_market_page.enter()
    yandex_market_page.switch_window()
    yandex_market_page.logining()
    yandex_market_page.switch_window_to_parent()
    assert yandex_market_page.find_element(YandexLocators.LOCATOR_YANDEX_USER_PROFILE) is not None, "Вход не выполнен"
    yandex_market_page.open_category()
    assert yandex_market_page.current_categ == yandex_market_page.open_categ, "Открыта не та категория"
    yandex_market_page.go_to_site()
    yandex_market_page.check_all_category()
    assert os.path.exists("category.csv") is True, "Файл с категориями не был создан"
    assert yandex_market_page.check_category() is True, "Популярных категорий нет в списке всех категорий"
    yandex_market_page.exit()
    assert yandex_market_page.find_element(YandexLocators.LOCATOR_YANDEX_ENTER_BUTTON_WITHOUT_JS) is not None, "Выход не выполнен"








