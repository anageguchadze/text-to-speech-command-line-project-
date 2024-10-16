from gtts import gTTS
import os
import pypdf
import requests


def truncate_text(text, max_length=500):
    if len(text) > max_length:
        return text[:max_length] + '...'
    return text


def display_info():
    print("Welcome to the Text-to-Speech program!")
    print("1. Convert input text to speech.")
    print("2. Convert PDF file to speech.")


def choose_language():
    languages = {
        'English': 'en',
        'French': 'fr',
        'Spanish': 'es',
        'Portuguese': 'pt'
    }

    print("Please choose your language:")
    for i, (language, code) in enumerate(languages.items(), start=1):
        print(f"{i}. {language} - {code}")

    choice = input("Enter the number of your choice: ")

    try:
        choice = int(choice)
        if 1 <= choice <= len(languages):
            selected_language_code = list(languages.values())[choice - 1]
            print(f"You have selected: {list(languages.keys())[choice - 1]} ({selected_language_code})")
            return selected_language_code
        else:
            print("Invalid choice. Please select a valid number.")
            return choose_language()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return choose_language()


def text_to_speech(text, lang_code):
    text = truncate_text(text)
    tts = gTTS(text=text, lang=lang_code)
    audio_file = "speech.mp3"
    tts.save(audio_file)
    print(f"Audio saved as {audio_file}")
    if os.path.exists(audio_file):
        print(f"File {audio_file} exists and is ready to play.")
    else:
        print(f"Error: File {audio_file} was not created.")


def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text


def download_pdf(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"PDF downloaded as {file_path}")


def main():
    display_info()
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        selected_language_code = choose_language()
        print("Text should not exceed 500 symbols.")
        text = input("Enter text to speak: ")
        text_to_speech(text, selected_language_code)
    elif choice == '2':
        selected_language_code = choose_language()
        pdf_url = input("Enter PDF file URL: ")
        pdf_file_path = "lorem-ipsum.pdf"
        download_pdf(pdf_url, pdf_file_path)
        if os.path.exists(pdf_file_path):
            # selected_language_code = choose_language()
            pdf_text = read_pdf(pdf_file_path)
            text_to_speech(pdf_text, selected_language_code)
        else:
            print(f"File {pdf_file_path} not found.")
    else:
        print("Invalid choice. Please select 1 or 2.")
        main()


if __name__ == "__main__":
    main()