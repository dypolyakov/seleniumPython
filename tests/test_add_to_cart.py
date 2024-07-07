from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Chrome()
driver.maximize_window()

main_page = MainPage(driver)
catalog_page = CatalogPage(driver)
cart_page = CartPage(driver)


def test_(setup):
    driver.get(main_page.URL)
    main_page.change_city_to_moscow()

    # Проверка, что выбрался город Москва
    assert main_page.get_selected_city() == "Москва"
    main_page.go_to_mirrorless_cameras()

    # Проверка, что заголовок страницы Беззеркальные фотоаппараты
    assert catalog_page.get_title() == "Беззеркальные фотоаппараты"
    catalog_page.setting_filter("200000")
    catalog_page.sort_by_price_desc()

    # Проверка, что после применения сортировки в url страницы появился параметр sort=price_desc
    assert catalog_page.driver.current_url.endswith("sort=price_desc")
    selected_product_title = catalog_page.get_first_product_title()
    selected_product_price = catalog_page.get_first_product_price()
    catalog_page.click_add_to_cart_button()

    # Проверка, что после добавления товара в корзину кнопка изменила название
    assert catalog_page.get_add_to_cart_button_text() == "В корзине"
    catalog_page.click_cart_icon()

    # Проверка, что происходит переход на страницу корзины
    assert cart_page.get_current_url() == "https://www.fotosklad.ru/personal/cart/"
    # Проверка, заголовка страницы корзины
    assert cart_page.get_title() == "Корзина"
    # Проверка, заголовка выбранного в каталоге товара и добавленного в корзину
    assert selected_product_title == cart_page.get_product_title()
    # Проверка, цены выбранного в каталоге товара и добавленного в корзину
    assert selected_product_price == cart_page.get_product_price()
    driver.quit()

