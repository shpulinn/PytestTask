from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SbisContactsPage(BasePage):
    CONTACTS_MENU = (By.LINK_TEXT, "Контакты")
    TENSOR_BANNER = (By.XPATH, "//a[contains(@href, 'tensor.ru')]")

    def open_contacts(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.CONTACTS_MENU)
        ).click()

    def click_tensor_banner(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.TENSOR_BANNER)
        ).click()
