import json
from pathlib import Path
import plotly.express as px

# Read the data from the file and convert it into the Python object
path = Path("eq_data/eq_data_30_day_m1.geojson")
contents = path.read_text(encoding="utf-8")
eq_data_30 = json.loads(contents)

# # Create a readable file and visualize the data
# path = Path("eq_data/readable_eq_data_30_day.geojson")
# readable_data = json.dumps(eq_data_30, indent=4)
# path.write_text(readable_data)

# Extract magnitude, longitiude and latitude info
eq_data_dict = eq_data_30["features"]
mags, longs, lats, eq_titles = (
    [each_eq["properties"]["mag"] for each_eq in eq_data_dict],
    [each_eq["geometry"]["coordinates"][0] for each_eq in eq_data_dict],
    [each_eq["geometry"]["coordinates"][1] for each_eq in eq_data_dict],
    [each_eq["properties"]["title"] for each_eq in eq_data_dict],
)
# create a geo map
title = "Global Earthquakes"
fig = px.scatter_geo(
    lat=lats,
    lon=longs,
    size=mags,
    title=title,
    color=mags,
    color_continuous_scale="viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    hover_name=eq_titles,
)

# fig.write_html("30_day.html")
fig.show()
