import time

from selenium.webdriver.common.by import By

from base.base import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    URL = "https://www.fotosklad.ru/"

    _catalog_button = (By.XPATH, "//a[@href='/catalog/']")
    _change_city_button = (By.XPATH, "//div[@class='header']//button[contains(@class, 'city-popup__btn--cancel')]")
    _moscow = (By.XPATH, "//span[@data-id='547']")
    _selected_city = (By.XPATH, "//div[@id='user_location_block']/a")
    _mirrorless_cameras_link = (By.XPATH, "//a[text()='Беззеркальные фотоаппараты']")

    def click_change_city_button(self):
        print("\tКлик по кнопке изменить город")
        self.click(self._change_city_button)

    def select_moscow(self):
        print("\tКлик по городу Москва")
        self.click(self._moscow)

    def change_city_to_moscow(self):
        print("Меняю город на Москву:")
        self.click_change_city_button()
        self.select_moscow()
        print()

    def get_selected_city(self):
        return self.get_content(self._selected_city)

    def click_catalog_button(self):
        print("\tКлик по кнопке каталога")
        self.click(self._catalog_button)

    def click_mirrorless_cameras_link(self):
        print("\tВыбор раздела беззеркальных камер")
        self.click(self._mirrorless_cameras_link)

    def go_to_mirrorless_cameras(self):
        print("Переход в раздел беззеркальных камер:")
        self.click_catalog_button()
        self.click_mirrorless_cameras_link()
        print()



