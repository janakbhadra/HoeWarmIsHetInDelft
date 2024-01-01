import os, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from chromedriver_py import binary_path  # Import chromedriver-py

def get_temperature():
    chrome_options = Options()
    # To run Chrome in headless mode
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')

    # Use chromedriver-py binary path
    os.environ["webdriver.chrome.driver"] = binary_path

    # Create a Chrome driver instance without specifying executable_path
    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get("http://www.weerindelft.nl/")
        iframe = driver.find_element(By.ID, 'ifrm_3')
        driver.switch_to.frame(iframe)
        time.sleep(4)

        wait = WebDriverWait(driver, 10)

        ajaxcounter_element = wait.until(lambda driver: EC.presence_of_element_located((By.ID, 'ajaxcounter'))(driver) and int(driver.find_element(By.ID, 'ajaxcounter').text) > 0)
        temperature_value = wait.until(EC.presence_of_element_located((By.ID, 'ajaxfeelslike')))
        temperature = temperature_value.text

    return temperature

if __name__ == "__main__":
    current_temperature = get_temperature()
    print(f"Current Temperature: {current_temperature}")
    value = int(''.join(filter(str.isdigit, current_temperature)))
    print(f"Current Temperature is {value} Degrees Celsius")
 
