import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Configure Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Set up ChromeDriver path
driver_path = '/usr/local/bin/chromedriver'
service = Service(driver_path)

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)


def extract_first_youtube_link(search_query):
    search_url = f"https://www.google.com/search?q={search_query}"
    driver.get(search_url)
    time.sleep(2)  # Wait for the page to load

    # Parse page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the first <a> tag with jsname="UWckNb"
    a_tag = soup.find('a', jsname='UWckNb', href=True)
    if a_tag:
        return a_tag['href']
    return None


def update_dramas(file_path):
    # Read the original data from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []

    for line in lines:
        data = line.strip().split('*')
        if len(data) > 1:
            drama_name = data[1]
            year = data[2] if len(data) > 2 else ''
            search_query = f"{drama_name} {year} youtube"
            youtube_link = extract_first_youtube_link(search_query)
            if youtube_link:
                data[-1] = youtube_link  # Update the link
            updated_lines.append('*'.join(data))
        else:
            updated_lines.append(line.strip())

    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        file.write('\n'.join(updated_lines))


# Update the file with new links
update_dramas('IndexingOfDramas1.txt')

# Close the WebDriver
driver.quit()
