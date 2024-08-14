# import requests
#
# # YouTube video URL
# video_url = "https://www.youtube.com/watch?v=f9Vzx87S5ZY&ab_channel=AndroidCity"
#
# # Extract the Video ID from the URL
# video_id = video_url.split("v=")[1]
#
# # Construct the thumbnail URL
# thumbnail_url = f"https://img.youtube.com/vi/f9Vzx87S5ZY/maxresdefault.jpg"
#
# # Send a request to the thumbnail URL
# response = requests.get(thumbnail_url)
#
# # Save the image if the request is successful
# if response.status_code == 200:
#     with open("youtube_thumbnail.jpg", "wb") as file:
#         file.write(response.content)
#     print("Thumbnail saved successfully!")
# else:
#     print("Failed to retrieve thumbnail.")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import base64
from PIL import Image
from selenium.webdriver.chrome.options import Options
import io
import os

# Configure Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Set up ChromeDriver path
driver_path = '/usr/local/bin/chromedriver'
service = Service(driver_path)

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

# Create images directory if not exists
images_directory = 'static/images1'
if not os.path.exists(images_directory):
    os.makedirs(images_directory)


def save_image_from_div(div_class, drama_name, year):
    try:
        # Navigate to Google Images search page
        driver.get(f'https://www.google.com/search?q={drama_name}+{year}+drama&tbm=isch')

        # Wait until the div with the specified class is present
        image_div = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, div_class))
        )

        # Find the image tag within the div
        image_tag = image_div.find_element(By.TAG_NAME, 'img')

        # Get the base64 image data
        image_data = image_tag.get_attribute("src")
        if image_data.startswith("data:image/jpeg;base64,"):
            base64_str = image_data.split("data:image/jpeg;base64,")[1]

            # Decode the base64 string
            image_bytes = base64.b64decode(base64_str)

            # Convert bytes to an image
            image = Image.open(io.BytesIO(image_bytes))

            # Define the file path and save the image
            file_path = os.path.join(images_directory, f"{drama_name}_{year}.jpeg")
            image.save(file_path)
            print(f"Image saved as '{file_path}'")
        else:
            print("The image URL is not in base64 format.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Read the text file and process each drama
with open('IndexingOfDramas1.txt', 'r') as file:
    i=0
    for line in file:
        i+=1
        if i==5:
            break
        parts = line.strip().split('*')
        if len(parts) >= 3:
            index, drama_name, year, *_ = parts
            drama_name = drama_name.replace(" ", "_")  # Replace spaces with underscores in file name
            save_image_from_div('H8Rx8c', drama_name, year)

# Close the driver
driver.quit()
