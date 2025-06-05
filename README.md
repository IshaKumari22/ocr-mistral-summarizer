# OCR + AI Summarizer using Mistral (Offline)

## 🔍 Project Overview
A Python project that extracts text from images using Tesseract OCR and summarizes it using the Mistral language model running offline via Ollama.

## 🚀 Features
- OCR using Tesseract
- Summarization using Mistral
- Runs 100% offline
- Easy to set up and beginner-friendly

## 🛠️ Tech Stack
- Python
- Tesseract OCR
- Ollama (for LLMs)
- Mistral Model
- Git, GitHub

## 📸 How It Works
1. Extracts text from an image using `pytesseract`
2. Sends extracted text to Mistral using a subprocess call to `ollama`
3. Outputs the summarized content

## 🧪 Sample Output
**OCR Output:**
![OCR and Mistral Output](https://raw.githubusercontent.com/IshaKumari22/ocr-mistral-summarizer/main/ocr_output.png)
![OCR Summary Output](https://raw.githubusercontent.com/IshaKumari22/ocr-mistral-summarizer/main/ocr_summary_output.png)





## 📂 How to Run
1. Install Tesseract and add to PATH
2. Install Python packages: `pip install pytesseract pillow`
3. Run Ollama: `ollama run mistral`
4. Run the Python script:
5.
 ```markdown
```bash
python summarize_from_image.py




