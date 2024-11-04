import pytesseract
from PIL import Image
import os
import re

# Define the function for OCR text extraction from images in a folder
def extract_text_from_folder(input_folder):
    # Automatically create an "output" folder in the input folder's directory
    output_folder = os.path.join(input_folder, "output")
    os.makedirs(output_folder, exist_ok=True)

    # Helper function to apply OCR on an image file
    def ocr_text_extraction(image_path):
        if image_path.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            img = Image.open(image_path)
            return pytesseract.image_to_string(img)
        else:
            raise ValueError("Unsupported file format. Use an image file.")

    # Helper function for text preprocessing
    def preprocess_text(text):
        text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
        text = text.strip()  # Remove leading/trailing spaces
        return text

    # Process each image file in the input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        
        # Check if it is an image file
        if os.path.isfile(file_path) and file_path.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            # Extract text using OCR
            raw_text = ocr_text_extraction(file_path)

            # Preprocess the text
            clean_text = preprocess_text(raw_text)

            # Define the output text file name based on the image name
            output_file_name = f"{os.path.splitext(filename)[0]}.txt"
            output_file_path = os.path.join(output_folder, output_file_name)

            # Save the extracted text to a .txt file
            with open(output_file_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(clean_text if clean_text else "No text found")

            print(f"Text extracted and saved to {output_file_path}")

# Define the input folder path
input_folder = 'E:\Career\X Space Internship\Task 4\Images'  # Replace with the path to your image folder

# Run the function
extract_text_from_folder(input_folder)
