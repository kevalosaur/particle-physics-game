# Helper file that plots a histogram

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        numbers = [float(line.strip()) for line in file.readlines()]
    plt.hist(numbers, bins=100)
    plt.show()