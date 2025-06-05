from PIL import Image
import pytesseract

# Step 1: Point to your tesseract.exe path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Step 2: Load the image (must be in the same folder)
image = Image.open("sample.png")  # Make sure this image exists

# Step 3: Extract text using OCR
extracted_text = pytesseract.image_to_string(image)

# Step 4: Print the result
print("=== Extracted OCR Text ===")
print(extracted_text)
