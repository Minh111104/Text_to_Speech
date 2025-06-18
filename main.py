# this is a simple app that converts text to speech using pyttsx3 (offline TTS)
import PyPDF2
import pyttsx3

# Function to convert text to speech
def text_to_speech(text, output_file="output.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()

    print(f"Audio content written to {output_file}")

# Function to read PDF and extract text
def pdf_to_text(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""
    
    return text

# Main function to execute the PDF to speech conversion
if __name__ == "__main__":
    pdf_path = "./Files/QuangMinh_Nguyen_Resume - SWE.pdf"  # Change to your PDF file path
    
    try:
        text = pdf_to_text(pdf_path)
        text_to_speech(text)
    except Exception as e:
        print(f"An error occurred: {e}")

