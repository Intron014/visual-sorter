import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# Toggle debug mode
debug_mode = True

# Bubble Sort algorithm
def bubble_sort(rects):
    n = len(rects)
    swaps = 0
    comparisons = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            comparisons += 1
            if rects[j].get_height() > rects[j + 1].get_height():
                # Swap heights of rectangles
                height_j = rects[j].get_height()
                height_j_plus_1 = rects[j + 1].get_height()
                rects[j].set_height(height_j_plus_1)
                rects[j + 1].set_height(height_j)
                swaps += 1
                yield rects, swaps, comparisons

# Generate a random shuffled list
def generate_list(size):
    lst = list(range(1, size + 1))
    random.shuffle(lst)
    return lst

# Initialize the plot
fig, ax = plt.subplots()
ax.set_title("Bubble Sort Visualization")

# Variables for user input
num_items = int(input("Enter the number of items to sort: "))
speed = int(input("Enter the speed of the animation (smaller number means faster speed): "))

bar_rects = ax.bar(range(len(generate_list(num_items))), generate_list(num_items), align="edge")

# Function to be called repeatedly to update the animation
def animate(frame_number):
    global bar_rects
    try:
        generator = bubble_sort(bar_rects)
        rects, swaps, comparisons = next(generator)
        if debug_mode:
            print(f"Swaps: {swaps}\tComparisons: {comparisons}")
    except StopIteration:
        if debug_mode:
            print("Sorting completed")
        # Regenerate a new list and reset the bar graph
        new_list = generate_list(num_items)
        for rect, height in zip(bar_rects, new_list):
            rect.set_height(height)

# Create the animation
anim = animation.FuncAnimation(fig, animate, interval=speed, repeat=True)

# Show the plot
plt.show()
