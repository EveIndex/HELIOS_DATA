from tqdm import tqdm
import requests
import csv
from bs4 import BeautifulSoup

# Get the url from the user
url = input("Enter the url of the website: ")

# Make a request to the website
response = requests.get(url)

# Parse the html content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the paragraphs in the html
paragraphs = soup.find_all("p")

# Open a csv file to write the data
file_number = 1 # Keep track of the file number
with open(f"HELIOS_DATA_{file_number}.csv", "w") as file:
    # Create a csv writer object
    writer = csv.writer(file)
    # Create a progress bar object
    progress = tqdm(paragraphs, desc="Scraping paragraphs")
    # Write each paragraph as a row in the csv file
    for paragraph in progress:
        writer.writerow([paragraph.get_text()])