from statistics import mean, median

# -------- DUMMY DATA (Last 10 Days) --------
# Temperature in °C
temps = [31, 32, 30, 33, 34, 35, 32, 31, 36, 33]

# AQI values
aqi_values = [70, 75, 80, 65, 90, 85, 78, 72, 88, 76]

# -------- CALCULATIONS --------
avg_temp = mean(temps)
median_temp = median(temps)

avg_aqi = mean(aqi_values)
median_aqi = median(aqi_values)

# -------- OUTPUT --------
print("Average Temp:", avg_temp)
print("Median Temp:", median_temp)

print("Average AQI:", avg_aqi)
print("Median AQI:", median_aqi)
