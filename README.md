# 🚗 Car Price Scraper

> A mini project designed to scrape and compare car prices from various websites efficiently.

---

## 🛠 Technologies
This project leverages the following stack:

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core programming language |
| **Playwright** | High-performance browser automation |
| **JSON** | Data storage and structured output |

## 🎯 Goal
The main objective of this project is to **learn web scraping techniques** while building a functional interface for simple price comparison.

---

## 🚀 How to Run It

Follow the step-by-step guide below to set up your environment:

### 1️⃣ Clone the Repository
```bash
git clone <your-repository-url>
cd <project-folder-name>
2️⃣ Install Dependencies
It is highly recommended to use a virtual environment (venv).

Bash
pip install -r requirements.txt
3️⃣ playwright install
This command downloads the necessary browser binaries (Chromium, Firefox, etc.):

Bash
4️⃣ Prepare the Environment
Create the JSON file where the results will be saved:

Bash
# Windows (PowerShell)
New-Item output_scraping.json

# Linux / macOS / Git Bash
touch output_scraping.json
5️⃣ Execute the Scraper
Run the main script to start collecting data:

Bash
python scraping.py
📝 Notes
Python Version: 3.8 or higher required.

Output: The data will be structured and saved in output_scraping.json.

Made with ❤️ for learning web scraping.