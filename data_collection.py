import openai
from tqdm import tqdm
import requests
import csv
import json
from bs4 import BeautifulSoup


openai.api_key = "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"

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
    progress = tqdm(paragraphs, desc="Scraping and generating paragraphs")
    # Write each paragraph as a prompt-completion pair in the text file
    for paragraph in progress:
        # Get the paragraph text as the completion
        completion = paragraph.get_text()
        # Use the OpenAI API to generate a prompt from the completion
        response = openai.Completion.create(
            model="curie", # Use the davinci model for best results
            prompt=completion, # Use the completion as the prompt
            stop=["\n"], # Stop generating when encountering a newline
            max_tokens=25, # Limit the number of tokens to generate
            temperature=0.5, # Use a moderate temperature for creativity
            top_p=1.0, # Use a high probability for diversity
            frequency_penalty=0.0, # Do not penalize frequent words
            presence_penalty=0.0, # Do not penalize new words
        )
        # Get the generated text from the response
        prompt = response["choices"][0]["text"]
        # Create a dictionary with the prompt and completion
        data = {"prompt": prompt, "completion": completion}
        # Convert the dictionary to a JSON string and write it to the file
        file.write(json.dumps(data) + "\n")