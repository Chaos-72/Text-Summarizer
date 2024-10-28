# 📄 Text Summarizer

This project utilizes the Hugging Face Transformers library to create a web-based text summarization tool. It fetches content from a provided URL, processes it, and returns a concise summary.

---

## 🚀 Features
- Summarization of text content from any URL.
- Adjustable minimum and maximum lengths for summaries.
- User-friendly web interface built with Flask and Bootstrap.

---

## 📋 Table of Contents
1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Contributing](#contributing)
7. [License](#license)

---

## 📌 Introduction
The Text Summarizer leverages the Hugging Face `summarization` pipeline to condense articles or text from URLs into shorter summaries. This helps users quickly grasp the main ideas without reading lengthy articles.

---

## 🛠️ Technologies Used
- **Python**
- **Flask**: For web framework
- **Hugging Face Transformers**: For summarization
- **BeautifulSoup**: For web scraping
- **Bootstrap**: For front-end styling

---

## 📥 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-summarizer.git
   cd text-summarizer

2. Install required libraries:

    pip install -r requirements.txt