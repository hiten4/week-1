"""
gandhinagar_weather_stats.py

This script fetches the last 10 days of temperature data for Gandhinagar
using the Open-Meteo API and calculates the average and median temperature.
"""

import requests
from statistics import mean, median
from datetime import datetime, timedelta

# Gandhinagar coordinates
LATITUDE = 23.2156
LONGITUDE = 72.6369

# Calculate date range (last 10 days)
end_date = datetime.today().date()
start_date = end_date - timedelta(days=10)

# Open-Meteo API URL (no API key required)
url = (
    f"https://archive-api.open-meteo.com/v1/archive?"
    f"latitude={LATITUDE}&longitude={LONGITUDE}"
    f"&start_date={start_date}&end_date={end_date}"
    f"&daily=temperature_2m_mean&timezone=Asia%2FKolkata"
)

# Fetch data
response = requests.get(url)
data = response.json()

# Extract temperatures
temps = data["daily"]["temperature_2m_mean"]

# Calculate statistics
avg_temp = mean(temps)
median_temp = median(temps)

# Print results
print("Gandhinagar Weather Stats (Last 10 Days)")
print("---------------------------------------")
print("Temperatures:", temps)
print("Average Temperature:", round(avg_temp, 2))
print("Median Temperature:", round(median_temp, 2))
