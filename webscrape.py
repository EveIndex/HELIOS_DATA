from tqdm import tqdm
import requests
import csv
import json
from bs4 import BeautifulSoup

# Get the url from the user
url = input("Enter the url of the website: ")

# Make a request to the website
response = requests.get(url)

# Parse the html content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the paragraphs in the html
paragraphs = soup.find_all("p")

# Open a text file to write the data
file_number = 1 # Keep track of the file number
with open(f"HELIOS_DATA_{file_number}.jsonl", "w") as file:
    # Create a progress bar object
    progress = tqdm(paragraphs, desc="Scraping paragraphs")
    # Write each paragraph as a prompt-completion pair in the text file
    for paragraph in progress:
        # Create a dictionary with an empty prompt and the paragraph as the completion
        data = {"prompt": "", "completion": paragraph.get_text()}
        # Convert the dictionary to a JSON string and write it to the file
        file.write(json.dumps(data) + "\n")