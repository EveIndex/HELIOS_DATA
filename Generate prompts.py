import openai

# Set your OpenAI API key
openai.api_key = "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"

# Open your JSONL file that contains the completions
with open("HELIOS_DATA_1.jsonl", "r") as input_file:
    # Open a new JSONL file to write the prompts and completions
    with open("HELIOS_DATA_2.jsonl", "w") as output_file:
        # Loop through each line in the input file
        for line in input_file:
            # Parse the line as a JSON object
            data = json.loads(line)
            # Extract the completion from the data
            completion = data["completion"]
            # Use the OpenAI API to generate a prompt from the completion
            response = openai.Completion.create(
                model="davinci", # Use the davinci model for best results
                prompt=completion, # Use the completion as the prompt
                stop=["\n"], # Stop generating when encountering a newline
                max_tokens=10, # Limit the number of tokens to generate
                temperature=0.5, # Use a moderate temperature for creativity
                top_p=1.0, # Use a high probability for diversity
                frequency_penalty=0.0, # Do not penalize frequent words
                presence_penalty=0.0, # Do not penalize new words
            )
            # Get the generated text from the response
            prompt = response["choices"][0]["text"]
            # Create a new dictionary with the prompt and completion
            new_data = {"prompt": prompt, "completion": completion}
            # Convert the dictionary to a JSON string and write it to the output file
            output_file.write(json.dumps(new_data) + "\n")