import plotly.express as px

from die import Die

# Create two D6 dice

die_1 = Die()
die_2 = Die(10)

# Make some rolls and store the results
results = []
for num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyse the results
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_results + 1)
frequencies = [results.count(value) for value in poss_results]


# Visualize the results
title = "Results of Rolling a D6 and D10 Dice 50,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further afjust the chart layout
fig.update_layout(xaxis_dtick=1)
fig.write_html("dice_visual_d6d10.html")
fig.show()
