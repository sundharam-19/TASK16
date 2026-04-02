from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PopulationPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://worldometers.info"
        # Using XPath as instructed
        self.population_xpath = "//div[@class='main-counter-number']/span[@class='rts-counter']"
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get(self.url)

    def get_population(self):
        # Explicit wait to ensure the element is visible
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.population_xpath))
        )
        return element.text
