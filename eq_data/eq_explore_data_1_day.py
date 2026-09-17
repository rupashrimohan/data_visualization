from pathlib import Path
import json
import plotly.express as px

# Read data as a string and convert to a python object
path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

# # Create more reading version of json file
# path = Path("eq_data/readable_eq_data_1_day.geojson")
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

# Examine all earthquakes in the dataset
all_eq_dicts = all_eq_data["features"]

mags, longs, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    long = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    longs.append(long)
    lats.append(lat)

# print(mags[:10])
# print(longs[:5])
# print(lats[:5])
title = "Global Earthquakes"
fig = px.scatter_geo(lat=lats, lon=longs, title=title)

fig.show()
