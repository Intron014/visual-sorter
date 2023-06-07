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
num_iterations = int(input("Enter the number of iterations: "))
speed = int(input("Enter the speed of the animation (smaller number means faster speed): "))

total_swaps = 0
total_comparisons = 0

for _ in range(num_iterations):
    bar_rects = ax.bar(range(len(generate_list(num_items))), generate_list(num_items), align="edge")

    # Function to be called repeatedly to update the animation
    def animate(frame_number):
        global bar_rects, total_swaps, total_comparisons
        try:
            generator = bubble_sort(bar_rects)
            rects, swaps, comparisons = next(generator)
            total_swaps += swaps
            total_comparisons += comparisons
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
    anim = animation.FuncAnimation(fig, animate, interval=speed, repeat=False)

    # Show the plot
    plt.show()

# Calculate average swaps and comparisons
avg_swaps = total_swaps / num_iterations
avg_comparisons = total_comparisons / num_iterations
print(f"Average Swaps: {avg_swaps}")
print(f"Average Comparisons: {avg_comparisons}")
