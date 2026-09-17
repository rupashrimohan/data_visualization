from pathlib import Path
import csv
import plotly.express as px

path = Path("world_fires/world_fires_1_day.csv")
contents = path.read_text(encoding="utf-8").splitlines()


reader = csv.reader(contents)
header_row = next(reader)

# for index, row_name in enumerate(header_row):
#     print(index, row_name)
# 0 latitude
# 1 longitude
# 2 brightness
# 3 scan
# 4 track
# 5 acq_date
# 6 acq_time
# 7 satellite
# 8 confidence
# 9 version
# 10 bright_t31
# 11 frp
# 12 daynight

# Find index
longitude_inx = header_row.index("longitude")
latitude_inx = header_row.index("latitude")
bightness_inx = header_row.index("brightness")

# convert the reader to rows to iterate
rows = list(reader)
# find the latitude, longitude and brightness values and create a list
longs = [float(row[longitude_inx]) for row in rows]
lats = [float(row[latitude_inx]) for row in rows]
brightness = [float(row[bightness_inx]) for row in rows]


title = "World Fires of 1 Day"
fig = px.scatter_geo(
    lon=longs,
    lat=lats,
    size=brightness,
    title=title,
    color=brightness,
    color_continuous_scale="sunsetdark",
    labels={"color": "Brightness"},
    projection="natural earth",
)

fig.show()
