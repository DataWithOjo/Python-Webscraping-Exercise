# NOAA Weather File Downloader 🌤️

This project demonstrates how to use Python to **scrape an HTML page**, **identify a specific file by timestamp**, **download the file**, and **analyze the contents** using `pandas`.

> 🚀 Part of a hands-on exercise series: Web Scraping & File Downloading with Python.

---

## 🧠 Problem Statement

You are tasked with downloading a file of weather data from the NOAA Local Climatological Data archive:

📁 https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/

However, instead of hardcoding the filename, your Python script must:

1. **Scrape the directory page**.
2. **Locate the file that was "Last Modified" on `2024-01-19 10:27`**.
3. **Build the download URL** and fetch the file.
4. **Load the file into pandas**.
5. **Find and print the record(s) with the highest `HourlyDryBulbTemperature`**.

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/noaa-weather-downloader.git
cd noaa-weather-downloader
docker build --tag=exercise-2 .
docker-compose up run
