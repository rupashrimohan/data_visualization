from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path("weather_data_california/death_valley_2021_full.csv")
try:
    lines = path.read_text(encoding="utf-8").splitlines()
except FileNotFoundError:
    print("The file is not available.")
else:
    reader = csv.reader(lines)
    header_row = next(reader)

    #     for index, column_name in enumerate(header_row):
    #         print(index, column_name)
    # 0 STATION
    # 1 NAME
    # 2 DATE
    # 3 PRCP
    # 4 SNOW
    # 5 SNWD
    # 6 TMAX
    # 7 TMIN
    # 8 TOBS

    # create a list for dates, highs and lows temperature values
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[6])
            low = int(row[7])
        except ValueError:
            print(f"Missing values for the {current_date}.")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

    # Create a plot using matplotlib
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    ax.plot(dates, highs, color="red")
    ax.plot(dates, lows, color="blue")
    ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    # Name the title and labels
    ax.set_title("Daily High and Low Temperatures,2021 Death Valley, CA", fontsize=20)
    ax.set_ylabel("Temperature (F)", fontsize=14)
    fig.autofmt_xdate()
    plt.tight_layout()
    ax.tick_params(labelsize=14)

    plt.show()
