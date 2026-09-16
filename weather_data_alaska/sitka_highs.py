from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Plot daily high temperatures from Sitka CSV data

# Read and parse 2021 weather data from CSV using csv.reader
# Extract dates and daily highs
# Plot temperature trends and shade the range using Matplotlib

path = Path("weather_data_alaska/sitka_weather_2021_simple.csv")
try:
    lines = path.read_text(encoding="utf-8").splitlines()
except FileNotFoundError:
    print("The file is not found in the mentioned path.")
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
    # Extract high temperatures and dates
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
        except ValueError:
            print(f"Missing high temperature for {current_date}")
        else:
            highs.append(high)
            dates.append(current_date)

    # Plot the high temperatures
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    ax.plot(dates, highs, color="red")

    # Format the plot
    ax.set_title("Daily High Temperatures, 2021", fontsize=24)
    ax.set_xlabel("", fontsize=14)
    fig.autofmt_xdate()
    plt.tight_layout()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=16)

    plt.show()
