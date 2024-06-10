from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SbisServicesPage(BasePage):
    SERVICES_TAB = (By.XPATH, "//a[contains(text(), 'Сервисы')]")
    SERVICES_BLOCK = (By.XPATH, "//h2[contains(text(), 'Сервисы')]")
    SOLUTIONS_BLOCK = (By.XPATH, "//h2[contains(text(), 'Решения')]")
    INFRASTRUCTURE_BLOCK = (By.XPATH, "//h2[contains(text(), 'Инфраструктура')]")
    MORE_DETAILS_LINKS = (By.XPATH, "//a[contains(text(), 'Подробнее')]")

    def navigate_to_services(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.SERVICES_TAB)
        ).click()

    def verify_services_blocks(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.SERVICES_BLOCK)
        )
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.SOLUTIONS_BLOCK)
        )
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.INFRASTRUCTURE_BLOCK)
        )

    def verify_more_details_links(self):
        links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(self.MORE_DETAILS_LINKS)
        )
        assert len(links) > 0, "No 'Подробнее' links found"

    def click_first_more_details_link(self):
        link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.MORE_DETAILS_LINKS)
        )
        link.click()

    def verify_solution_page(self):
        assert "solutions" in self.driver.current_url, "Failed to navigate to solutions page"
