import os, time, tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox


def get_temperature():
    #No changes needed if chrome driver is already installed with system variable already updated
    # Specify the path for Chrome driver.
    chromedriver_path = '../chromedriver'
    # Set the PATH environment variable to include the directory of the ChromeDriver executable
    os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)
    
    chrome_options = Options()
    #To run chrome browser window in Background
    chrome_options.add_argument('--headless')

    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get("http://www.weerindelft.nl/")
        iframe = driver.find_element(By.ID, 'ifrm_3')
        driver.switch_to.frame(iframe)
        time.sleep(4)

        wait = WebDriverWait(driver, 10)

        ajaxcounter_element = wait.until(EC.presence_of_element_located((By.ID, 'ajaxcounter')))
        wait.until(lambda driver: int(ajaxcounter_element.text) <= 4)

        temperature_value = wait.until(EC.presence_of_element_located((By.ID, 'ajaxfeelslike')))
        temperature = temperature_value.text

    return temperature

def show_temperature_popup(temperature):
    root = tk.Tk()
    root.withdraw()  # To Hide the main window
    if temperature:
        messagebox.showinfo("Current Temperature", f"Current Temperature: {temperature}")

if __name__ == "__main__":
    current_temperature = get_temperature()
    print(f"Current Temperature: {current_temperature}" if current_temperature else "Unable to retrieve the temperature.")
    value = int(''.join(filter(str.isdigit, current_temperature)))
    print(f"Current Temperature is {value} Degrees Celcius" if current_temperature else "Unable to retrieve the temperature.")
    show_temperature_popup(current_temperature)


