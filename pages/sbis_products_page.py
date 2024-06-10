from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SbisProductsPage(BasePage):
    TECHNOLOGIES_TAB = (By.XPATH, "//a[contains(text(), 'Технологии')]")
    UNIFIED_PLATFORM_BLOCK = (By.XPATH, "//h2[contains(text(), 'Единая платформа')]")
    CLOUD_SOLUTIONS_BLOCK = (By.XPATH, "//h2[contains(text(), 'Облачные решения')]")
    SERVICES_BLOCK = (By.XPATH, "//h2[contains(text(), 'Сервисы')]")
    BUY_LINK = (By.XPATH, "//a[contains(text(), 'Купить')]")
    DETAILS_LINK = (By.XPATH, "//a[contains(text(), 'Подробнее')]")

    def navigate_to_technologies(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.TECHNOLOGIES_TAB)
        ).click()

    def verify_technology_blocks(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.UNIFIED_PLATFORM_BLOCK)
        )
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.CLOUD_SOLUTIONS_BLOCK)
        )
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.SERVICES_BLOCK)
        )

    def navigate_to_cloud_solutions(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.CLOUD_SOLUTIONS_BLOCK)
        ).click()

    def verify_buy_and_details_links(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.BUY_LINK)
        )
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.DETAILS_LINK)
        )

    def click_buy_link(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.BUY_LINK)
        ).click()

    def verify_cloud_solutions_section(self):
        assert "cloud-solutions" in self.driver.current_url, "Failed to navigate to 'Облачные решения' section"
