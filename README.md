<<<<<<< HEAD
# Text to Speech PDF Converter

This is a simple Python app that extracts text from a PDF file and converts it to speech using the offline `pyttsx3` library.

## Features

- **Extracts text from PDF files**
- **Converts extracted text to speech (MP3)**
- **Works offline (no API key or internet required)**
- **Easy to use and modify**

## Requirements

- Python 3.x
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)

## Installation

1. Clone or download this repository.
2. Install dependencies:

    ```bash
    pip install pyttsx3 PyPDF2
    ```

## Usage

1. Place your PDF file in the `Files` folder.
2. Update the `pdf_path` variable in `main.py` to match your PDF filename:

    ```bash
    pdf_path = "./Files/your_file.pdf"
    ```

3. Run the script:

    ```bash
    python main.py
    ```

4. The output audio will be saved as `output.mp3` in the project folder.

## Notes

- The quality of text extraction depends on the PDF file's formatting.
- The output voice depends on your operating system's available voices.

## License

This project is for educational purpose.
=======
Text_to_Speech App
>>>>>>> c9206ecfe8069289064a95e0cf69fed84e743ee5
