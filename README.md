# Automated-Book-Publication-Workflow
# 📘 Content Scraper & AI Editor (with Chat & Version Control)

A Flask web application that lets you:
- Extract content from web pages or images,
- Rewrite/improve it using Gemini AI (`gemini-1.5-flash`),
- Chat with AI about the content,
- Restore previous versions using **ChromaDB** (versioning + rollback).

---

## 🚀 Features

| Feature                         | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| 🌐 URL Scraping                  | Extract title and content from a given webpage using custom headers        |
| 🖼 OCR from Image                | Extract text from uploaded image using `pytesseract`                       |
| ✨ AI Rewrite (Spin)            | Gemini-powered rewriting for clarity, fluency, and engagement              |
| 💬 Chat with Contextual AI      | Gemini-based chat interface tailored to your scraped content               |
| ♻️ Version Control & Rollback   | Automatically save content before rewriting using `ChromaDB`               |
| 📄 Download .txt File           | Get cleaned version of the content in `.txt` format                        |

---

## 🏗️ Folder Structure

```bash
webscraper/
├── app.py                    # Main Flask app
├── scraper.py               # URL content extraction logic
├── .env                     # API key for Gemini
├── chroma_store/            # ChromaDB persistent data
├── uploads/                 # Uploaded images
├── temp_docs/               # Generated .txt files
├── templates/
│   └── index.html           # Main HTML interface
└── requirements.txt         # All Python dependencies
```

## libraries to be installed

```bash
pip install flask python-dotenv pytesseract pillow google-generativeai chromadb requests
```

##libraries

| Dependency          | Command to Install                | Purpose                                   |
| ------------------- | --------------------------------- | ----------------------------------------- |
| Flask               | `pip install flask`               | Web framework for routing and forms       |
| python-dotenv       | `pip install python-dotenv`       | Load API key securely from `.env`         |
| pytesseract         | `pip install pytesseract`         | Optical character recognition (OCR)       |
| Pillow              | `pip install pillow`              | Image handling (used with OCR)            |
| google-generativeai | `pip install google-generativeai` | Access Gemini API for rewriting + chat    |
| chromadb            | `pip install chromadb`            | Version control & rollback with vector DB |
| requests            | `pip install requests`            | Making HTTP requests in `scraper.py`      |

---
