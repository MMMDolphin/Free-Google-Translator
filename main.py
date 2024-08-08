import time
from googletrans import Translator

def translate_file_to_bulgarian(file_path):
    # Create a Translator object
    translator = Translator()

    # Open the output file in append mode
    with open('translated_to_bulgarian.txt', 'a', encoding='utf-8') as translated_file:
        # Read the content of the input file line by line
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Translate the current line to Bulgarian
                    translated = translator.translate(line, dest='bg')
                    # Append the translated text to the output file
                    translated_file.write(translated.text + '\n')
                    # Print the translated text for reference
                    print(translated.text)
                    # Introduce a minor delay between requests
                    time.sleep(0.15)  # Adjust the interval as needed
                except Exception as e:
                    print(f"Error translating line: {line.strip()}. Error: {e}")

# Provide the path to your file here
file_path = 'file.txt'
translate_file_to_bulgarian(file_path)
