import subprocess
from PIL import Image
import pytesseract

# Path to Tesseract executable (set it only if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Step 1: Load image and extract text
image = Image.open("sample2.jpg")  # Ensure sample.jpg is in the same folder
text = pytesseract.image_to_string(image, config='--psm 6')

if not text.strip():
    print("❌ No text detected in the image.")
    exit()

print("✅ OCR Extracted Text:\n")
print(text)

# ✅ Step 2: Clean repeated lines before summarization
lines = text.splitlines()
unique_lines = []
for line in lines:
    line = line.strip()
    if line and (not unique_lines or line != unique_lines[-1]):
        unique_lines.append(line)

cleaned_text = "\n".join(unique_lines)

# Step 3: Prepare prompt for Mistral
prompt = f"Summarize the following text:\n{cleaned_text}"


try:
    result = subprocess.run(
      ["C:\\Users\\91870\\AppData\\Local\\Programs\\Ollama\\ollama.exe", "run", "mistral"],
      input=prompt.encode("utf-8"),
      capture_output=True,
      timeout=180
    )

    print("✅ Summary by Mistral:\n")
    print(result.stdout.decode("utf-8"))

except Exception as e:
    print(f"❌ Error: {e}")
