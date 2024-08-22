# Speak Text

Speak Text is a Python-based text-to-speech application that allows users to input text and have it spoken aloud by a virtual voice. The application also allows users to adjust the speed, gender, and volume of the speech, and provides options to save the spoken text as an audio file. Additionally, the app maintains a history of the spoken texts for easy reference and management.

## Features

- Text-to-Speech: Convert any input text into speech.
- Adjustable Settings:
  - Speed: Choose between very slow, slow, normal, fast, and very fast speech rates.
  - Gender: Select between male and female voice options.
  - Volume: Set the volume from silent to very high.
- Downloadable Audio: Save the spoken text as an MP3 file.
- History Management: View and manage a history of previously spoken texts.

## Requirements

To install the required dependencies, make sure you have Python installed, then use:

pip install -r requirements.txt
The `requirements.txt file includes the following dependencies:

- tkinter: A built-in Python library used for creating graphical user interfaces.
- pyttsx3: A text-to-speech conversion library in Python.

## Usage

1. **Run the Application:**
   - Execute the Python script to open the Speak Text interface.
   
2. **Enter Your Text:**
   - Input the text you want to be spoken in the provided text box.
   
3. **Adjust Settings:**
   - Use the dropdown menus to select the desired speed, gender, and volume for the speech.
   
4. **Speak or Download:**
   - Click "Speak" to hear the text spoken aloud.
   - Click "Download" to save the spoken text as an MP3 file.
   
5. **View History:**
   - Click "History" to view previously spoken texts. You can also delete all history from this window.

## Project Structure

- main.py: The main script containing the application logic.
- requirements.txt: A file listing the dependencies required to run the application.
- voices/: A directory where saved MP3 files are stored.
- history.txt`: A file used to store the history of spoken texts.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. Contributions, such as bug fixes, feature enhancements, or documentation improvements, are welcome!
