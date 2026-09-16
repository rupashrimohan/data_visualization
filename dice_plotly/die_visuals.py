from die import Die

import plotly.express as px

die = Die()

# Store the results in the list []
results = []
for roll_num in range(1000):
    num = die.roll()
    results.append(num)

# Find the frequency of each side
frequencies = []
die_sides = range(1, die.num_sides + 1)
for value in die_sides:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = "Results of Rolling One D6 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=die_sides, y=frequencies, title=title, labels=labels)
fig.show()
