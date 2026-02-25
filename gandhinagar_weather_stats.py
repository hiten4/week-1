"""
gandhinagar_weather_aqi_stats.py

This script fetches the last 10 days of:
- Mean Temperature
- AQI (using US AQI from Open-Meteo Air Quality API)

It calculates average and median for both.
"""

import requests
from statistics import mean, median
from datetime import datetime, timedelta

# Gandhinagar coordinates
LATITUDE = 23.2156
LONGITUDE = 72.6369

# Date range (last 10 days)
end_date = datetime.today().date()
start_date = end_date - timedelta(days=10)

# ---------------- WEATHER DATA ----------------
weather_url = (
    f"https://archive-api.open-meteo.com/v1/archive?"
    f"latitude={LATITUDE}&longitude={LONGITUDE}"
    f"&start_date={start_date}&end_date={end_date}"
    f"&daily=temperature_2m_mean&timezone=Asia%2FKolkata"
)

weather_response = requests.get(weather_url)
weather_data = weather_response.json()

temps = weather_data["daily"]["temperature_2m_mean"]

# ---------------- AQI DATA ----------------
aqi_url = (
    f"https://air-quality-api.open-meteo.com/v1/air-quality?"
    f"latitude={LATITUDE}&longitude={LONGITUDE}"
    f"&start_date={start_date}&end_date={end_date}"
    f"&daily=us_aqi&timezone=Asia%2FKolkata"
)

aqi_response = requests.get(aqi_url)
aqi_data = aqi_response.json()

aqi_values = aqi_data["daily"]["us_aqi"]

# ---------------- CALCULATIONS ----------------
avg_temp = mean(temps)
median_temp = median(temps)

avg_aqi = mean(aqi_values)
median_aqi = median(aqi_values)

# ---------------- OUTPUT ----------------
print("Gandhinagar Weather + AQI Stats (Last 10 Days)")
print("------------------------------------------------")
print("Temperatures:", temps)
print("AQI Values:", aqi_values)

print("\nTemperature Average:", round(avg_temp, 2))
print("Temperature Median:", round(median_temp, 2))

print("\nAQI Average:", round(avg_aqi, 2))
print("AQI Median:", round(median_aqi, 2))
