import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Generate new sets of random walk
while True:
    rw = RandomWalk(50_000)
    rw.fill_walks()
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    ax.plot(
        rw.x_values,
        rw.y_values,
        color="Pink",
        linewidth=10,
    )

    # Hide the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Do you want to run another random walk? (y/n): ")
    if keep_running.lower() == "n":
        break
