from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorPage(BasePage):
    FORCE_IN_PEOPLE_BLOCK = (By.XPATH, "//section[contains(text(), 'Сила в людях')]")
    DETAILS_LINK = (By.LINK_TEXT, "Подробнее")
    WORK_SECTION_IMAGES = (By.CSS_SELECTOR, ".work-section img")

    def verify_force_in_people_block(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.FORCE_IN_PEOPLE_BLOCK),
                message=f"Can't find element by locator {self.FORCE_IN_PEOPLE_BLOCK}"
            )
            print("Block 'Сила в людях' found")
        except Exception as e:
            print(f"Exception encountered: {e}")
            print(f"Current URL: {self.driver.current_url}")
            raise

    def click_details(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.DETAILS_LINK)
            ).click()
        except Exception as e:
            print(f"Exception encountered: {e}")
            print(f"Current URL: {self.driver.current_url}")
            raise

    def verify_images_dimensions(self):
        try:
            images = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(self.WORK_SECTION_IMAGES)
            )
            dimensions = [(img.get_attribute('naturalWidth'), img.get_attribute('naturalHeight')) for img in images]
            assert all(dim == dimensions[0] for dim in dimensions), "Images dimensions are not equal"
        except Exception as e:
            print(f"Exception encountered: {e}")
            print(f"Current URL: {self.driver.current_url}")
            raise
