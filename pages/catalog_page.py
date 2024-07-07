import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base import Base


class CatalogPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    _mirrorless_cameras_link = (By.XPATH,
                                "//div[@class='catalog-index']//a[contains(text(), 'Беззеркальные фотоаппараты')]")
    _filter_sony_manufacturer = (By.XPATH,
                            "//ul[@class='checkbox__list']//span[@class='check__text' and text()='Sony']")
    _filter_min_price_input = (By.XPATH, "//input[@name='price[min]']")
    _filter_submit_button = (By.XPATH, "//a[contains(@class, 'filter__submit')][1]")
    _filter_popup_link = (By.XPATH, "//a[@class='filter__popup-link']")
    _title = (By.XPATH, "//h1[@class='page__title']")
    _sorting_select = (By.XPATH, "//div[contains(@class, 'sorting__current')]")
    _sorting_desc = (By.XPATH, "//a[@data-name='price_desc']")
    _first_product = "//ul[@class='product-tiles']/li[1]"
    _first_product_price = (By.XPATH, _first_product + "//div[@class ='product-tile__price']")
    _first_product_title = (By.XPATH, _first_product + "//div[@class ='product-tile__title']")
    _add_to_cart_button = (By.XPATH, _first_product + "//button")
    _cart_icon = (By.XPATH, "//a[@href='/personal/cart/']")

    def select_sony_manufacurer_in_filter(self):
        print("\tВыбор производителя Sony")
        self.click(self._filter_sony_manufacturer)

    def input_min_price(self, price):
        print("\tУстановки минимальной цены в 200000 рублей")
        self.input_(self._filter_min_price_input, price)
        self.input_(self._filter_min_price_input, Keys.ENTER)

    def apply_filter(self):
        print("\tКлик по кнопке применить фильтр")
        self.wait_for_element(self._filter_popup_link)
        self.click(self._filter_submit_button)

    def setting_filter(self, min_price):
        print("Настройка параметров фильтра:")
        self.select_sony_manufacurer_in_filter()
        self.input_min_price(min_price)
        self.apply_filter()
        print()

    def get_title(self):
        return self.get_content(self._title)

    def click_sorting(self):
        self.click(self._sorting_select)

    def click_sort_by_price_desc(self):
        self.click(self._sorting_desc)

    def sort_by_price_desc(self):
        print("Сортировка цены по убыванию")
        self.click_sorting()
        self.click_sort_by_price_desc()
        self.wait_for_url_contains("sort=price_desc")
        print()

    def click_add_to_cart_button(self):
        print("Клик по кнопке В корзину у самого дорогого товара")
        self.click(self._add_to_cart_button)
        print()

    def click_cart_icon(self):
        print("Клик по иконке корзины")
        self.click(self._cart_icon)

    def get_first_product_price(self):
        source_price = self.get_content(self._first_product_price).replace(" ", "")
        price = ""
        for e in source_price:
            if e.isdigit():
                price += e
            else:
                break
        return price

    def get_first_product_title(self):
        return self.get_content(self._first_product_title)

    def get_add_to_cart_button_text(self):
        self.wait_for_text_change(self._add_to_cart_button, "В корзине")
        return self.get_content(self._add_to_cart_button)
