# 🛡️ Real-Time Brand Reputation Monitor

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30-FF4B4B?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

An AI-powered dashboard that monitors brand sentiment in real-time across Reddit. This project bypasses 2026 API restrictions by utilizing resilient RSS ingestion to provide instant market insights.

---

## 🚀 Key Features
* **Live Data Ingestion:** Bypasses manual API approval loops using a robust RSS scraping engine.
* **Vibe Analysis:** Utilizes `TextBlob` NLP to score polarity and subjectivity of public discourse.
* **Interactive Dashboard:** Built with Streamlit for real-time keyword tracking and data visualization.
* **Professional Logging:** Centralized logging system to track scraper health and data flow.



## 🏗️ System Architecture
The project follows a modular **Data Pipeline** design:
1.  **Scraper (Hands):** Ingests raw XML data from Reddit's search feeds.
2.  **Analyzer (Brain):** Cleans HTML noise and performs NLP sentiment scoring.
3.  **Interface (Face):** Streamlit dashboard for user interaction and metrics.

## 🛠️ Tech Stack
* **Language:** Python 3.10.11
* **Scraping:** `feedparser`
* **NLP:** `TextBlob`, `NLTK`
* **UI/Dashboard:** `Streamlit`
* **Data Handling:** `Pandas`

## 🚦 Getting Started

### Prerequisites
* Python 3.10+
* Virtual Environment (Recommended)

### Installation
1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/yourusername/brand-monitor.git](https://github.com/yourusername/brand-monitor.git)
    cd brand-monitor
    ```

2.  **Setup Environment:**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    python -m textblob.download_corpora
    ```

4.  **Launch the Dashboard:**
    ```bash
    streamlit run app.py
    ```

## 📈 Roadmap
- [ ] Implement a "Download Report" button for CSV exports.
- [ ] Add Word Cloud visualization for common keywords.
- [ ] Integrate Twitter (X) RSS feeds for multi-platform monitoring.

---
## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

**Built by Abdulfaatihi** - *Data Scientist & AI Engineer*