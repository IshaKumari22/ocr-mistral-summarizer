from PIL import Image, ImageOps
import pytesseract

# Step 1: Point to your tesseract.exe path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Step 2: Load and preprocess the image
image = Image.open("sample2.jpg")  # your image file
gray = ImageOps.grayscale(image)
bw_image = gray.point(lambda x: 0 if x < 128 else 255, '1')

# Step 3: Extract text using OCR with config
extracted_text = pytesseract.image_to_string(bw_image, config='--psm 6')

# Step 4: Print the result
print("=== Extracted OCR Text ===")
print(extracted_text)
