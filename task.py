from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def close_cookie_banner(driver):
    try:
        # Wait for the cookie banner to be present (increased the timeout)
        cookie_banner = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'cnpk5__x'))
        )

        # Check if the close button is visible and clickable
        close_button = cookie_banner.find_element(By.CLASS_NAME, 'cnpk5__x')
        if close_button.is_displayed() and close_button.is_enabled():
            # Click the close button to close the cookie banner
            close_button.click()

    except TimeoutException:
        # The cookie banner might not be present, and that's okay
        pass

def scrape_car_information(url):
    driver = webdriver.Chrome()

    try:
        driver.get(url)
        close_cookie_banner(driver)

        # Use JavaScript to click the title element
        title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.vehicle-card-title a'))
        )
        driver.execute_script("arguments[0].click();", title_element)

        # Wait for the VIN and price elements to be present
        vin_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//dt[text()='VIN']/following-sibling::dd/span"))
        )
        # Adjusted selector for the Conditional Final Price
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'dd.conditional-final-price span.price-value'))
        )

        # Extract VIN and price
        vin = vin_element.text.strip()
        price = price_element.text.strip()

        # Use BeautifulSoup to parse the page source
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Extract other information (title, images, URL)
        title_element = soup.select_one('.vehicle-card-title')
        title = title_element.text.strip() if title_element else "N/A"
        images = [img['src'] for img in soup.select('.vehicle-image')]
        car_url = driver.current_url

        cars = [{
            'Title': title,
            'Images': images,
            'URL': car_url,
            'VIN': vin,
            'Price': price
        }]

    except NoSuchElementException as e:
        print(f"Element not found: {e}")

    finally:
        driver.quit()

    return cars

# Test with a specific car inventory page
url = "https://www.coastlinecdjr.com/new-inventory/index.htm"
all_cars = scrape_car_information(url)

# Print the results for debugging
for car in all_cars:
    print("Title:", car['Title'])
    print("Images:", car['Images'])
    print("URL:", car['URL'])
    print("VIN:", car['VIN'])
    print("Price:", car['Price'])
    print("-" * 30)
