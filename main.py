import requests
import pandas as pd
from bs4 import BeautifulSoup

# Scraping the webpage
base_url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the file with Last Modified = 2024-01-19 15:00
target_timestamp = "2024-01-19 15:00"


def main():

    filename = None

    for row in soup.find_all("tr"):
        cols = row.find_all("td")
        if len(cols) >= 2:
            modified_time = cols[1].text.strip()
            if modified_time == target_timestamp:
                filename = cols[0].find("a")["href"]
                break

    if not filename:
        print("File with last modified time 2024-01-19 15:00 not found.")
        exit()

    print(f"Found file: {filename}")

    # Download the file
    file_url = base_url + filename
    csv_response = requests.get(file_url)

    local_filename = "weather_data.csv"
    with open(local_filename, "wb") as f:
        f.write(csv_response.content)

    print(f"File downloaded and saved as {local_filename}")

    # Load with pandas
    df = pd.read_csv(local_filename)

    # Find records with highest HourlyDryBulbTemperature
    if "HourlyDryBulbTemperature" not in df.columns:
        print("Column 'HourlyDryBulbTemperature' not found in data.")
        exit()

    # Clean and convert column to numeric
    df["HourlyDryBulbTemperature"] = pd.to_numeric(
        df["HourlyDryBulbTemperature"], errors="coerce"
    )
    max_temp = df["HourlyDryBulbTemperature"].max()
    max_records = df[df["HourlyDryBulbTemperature"] == max_temp]

    print("\n Records with highest HourlyDryBulbTemperature:")
    print(max_records)


if __name__ == "__main__":
    main()
