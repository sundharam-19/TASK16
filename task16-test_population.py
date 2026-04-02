import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from population_page import PopulationPage

@pytest.fixture
def driver():
    # Setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    # Teardown
    driver.quit()

def test_extract_live_population(driver):
    page = PopulationPage(driver)
    page.load()
    print("\n--- Starting Live Population Extraction ---")
    print("Press CTRL+C in terminal to stop.")

    try:
        while True:
            population = page.get_population()
            # Print to terminal
            print(f"\rCurrent Population: {population}", end="", flush=True)
            time.sleep(1)  # Refresh rate
    except KeyboardInterrupt:
        print("\n--- Extraction Stopped by User ---")
