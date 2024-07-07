from selenium.webdriver.common.by import By

from base.base import Base


class CartPage(Base):
    _title = (By.XPATH, "//h1[@class='page__title']")
    _product_title = (By.XPATH, "//span[@data-entity='basket-item__name']")
    _product_price = (By.XPATH, "//div[@class='basket-items-list-item-price']//div[@class='basket-item__price']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.get_content(self._title)

    def get_product_title(self):
        return self.get_content(self._product_title)

    def get_product_price(self):
        source_price = self.get_content(self._product_price).replace(" ", "")
        price = ""
        for e in source_price:
            if e.isdigit():
                price += e
            else:
                break
        return price
