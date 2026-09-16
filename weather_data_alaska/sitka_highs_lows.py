from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Plot daily high and low temperatures from Sitka CSV data

# Read and parse 2021 weather data from CSV using csv.reader
# Extract dates, daily highs, and daily lows
# Plot temperature trends and shade the range using Matplotlib

path = Path("weather_data_alaska/sitka_weather_2021_simple.csv")
try:
    lines = path.read_text(encoding="utf-8").splitlines()
except FileNotFoundError:
    print("Please check the specified path.")
else:
    reader = csv.reader(lines)
    header_row = next(reader)
    #     for index, row_name in enumerate(header_row):
    #         print(index, row_name)
    #     1 NAME
    #     2 DATE
    #     3 TAVG
    #     4 TMAX
    #     5 TMIN
    # Read the high, low and date date from the csv reader
    highs, lows, dates = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

    # Plot the high, low and dates
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    ax.plot(dates, highs, color="red")
    ax.plot(dates, lows, color="blue")
    ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    # Name the axes
    ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
    ax.set_xlabel("Dates", fontsize=14)
    ax.set_ylabel("Temperature (F)", fontsize=14)
    fig.autofmt_xdate()
    plt.tight_layout()
    ax.tick_params(labelsize=16)

    plt.show()
