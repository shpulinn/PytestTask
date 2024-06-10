from pages.sbis_products_page import SbisProductsPage
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_page import TensorPage
from pages.sbis_services_page import SbisServicesPage

def test_first_scenario(driver):
    sbis_contacts_page = SbisContactsPage(driver)
    tensor_page = TensorPage(driver)
    
    # Step 1
    sbis_contacts_page.open()
    sbis_contacts_page.open_contacts()

    # Step 2
    sbis_contacts_page.click_tensor_banner()
    
    # Switch to new tab
    driver.switch_to.window(driver.window_handles[-1])

    # Verify the current URL
    print(f"Current URL after clicking banner: {driver.current_url}")
    assert "tensor.ru" in driver.current_url, "Failed to navigate to tensor.ru"
    
    # Add a wait to ensure the page loads
    driver.implicitly_wait(10)
    
    # Step 3
    tensor_page.verify_force_in_people_block()
    
    # Step 4
    tensor_page.click_details()
    
    # Verify we are on the right page
    print(f"Current URL after clicking details: {driver.current_url}")
    assert "about" in driver.current_url, "Failed to navigate to 'about' page"
    
    # Step 5
    tensor_page.verify_images_dimensions()

def test_second_scenario(driver):
    sbis_products_page = SbisProductsPage(driver)
    
    # Step 1
    sbis_products_page.open()

    # Step 2
    sbis_products_page.navigate_to_technologies()
    
    # Step 3
    sbis_products_page.verify_technology_blocks()

    # Step 4
    sbis_products_page.navigate_to_cloud_solutions()
    sbis_products_page.verify_buy_and_details_links()

    # Step 5
    sbis_products_page.click_buy_link()
    sbis_products_page.verify_cloud_solutions_section()

def test_third_scenario(driver):
    sbis_services_page = SbisServicesPage(driver)
    
    # Step 1
    sbis_services_page.open()

    # Step 2
    sbis_services_page.navigate_to_services()
    
    # Step 3
    sbis_services_page.verify_services_blocks()

    # Step 4
    sbis_services_page.verify_more_details_links()

    # Step 5
    sbis_services_page.click_first_more_details_link()
    sbis_services_page.verify_solution_page()
