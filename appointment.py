from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# URL of the appointment booking page
url = "https://service2.diplo.de/rktermin/extern/appointment_showMonth.do?locationCode=kara&realmId=967&categoryId=2801&dateStr=26.09.2023"

# Open the URL in the browser
driver.get(url)

# Wait for the page to load (adjust the time as needed)
time.sleep(5)

# Perform actions to select the earliest available appointment
# You'll need to inspect the webpage and adapt the code below to interact with the specific elements on the page

# Example: Click on a specific day in the calendar
day_element = driver.find_element(By.XPATH, "//td[@data-handler='selectDay'][text()='1']")
day_element.click()

# Example: Select a specific time slot
time_slot_element = driver.find_element(By.XPATH, "//div[@class='row-fluid timeSlot'][1]/div")
time_slot_element.click()

# Example: Fill in user information
name_input = driver.find_element(By.ID, "name")
name_input.send_keys("Your Name")

# Example: Fill in other required fields

# Submit the form
submit_button = driver.find_element(By.ID, "submitBtn")
submit_button.click()

# Close the browser
driver.quit()
