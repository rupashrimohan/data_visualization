import csv
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime


def _get_prcp_data(lines):
    """Extract the prcp data from the csv file and return a list"""
    reader = csv.reader(lines)
    header_row = next(reader)

    prcp_index = header_row.index("PRCP")
    prcp_list = []
    for row in reader:
        try:
            prcp = float(row[prcp_index])
        except ValueError:
            print("Missing value error")
        else:
            if prcp < 100.0:
                prcp_list.append(prcp)
    return prcp_list


# Comparing the precipition range for both sitka,Alaska and deathvalley, CA
path_sitka = Path("GHCND_sample.csv")
path_deathv = Path("weather_data_california/death_valley_2021_full.csv")
try:
    alaska_lines = path_sitka.read_text(encoding="utf-8").splitlines()
    ca_lines = path_deathv.read_text(encoding="utf-8").splitlines()
except FileNotFoundError:
    print("The file is not available.")
else:
    prcps_alaska = _get_prcp_data(alaska_lines)
    prcps_ca = _get_prcp_data(ca_lines)

    print(len(prcps_alaska))

    # Create a plot using matplotlib
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    ax.plot(prcps_alaska, color="red")
    ax.plot(prcps_ca, color="blue")

    # Name the title and labels
    ax.set_title(
        "Precipitation dataset of both Sitka, Alaska and Death Valley, CA", fontsize=20
    )
    ax.set_ylabel("Temperature (F)", fontsize=14)
    fig.autofmt_xdate()
    plt.tight_layout()
    ax.tick_params(labelsize=14)

    plt.show()
