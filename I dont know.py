import time
import matplotlib.pyplot as plt

cycles = 0
numbers = [0]

while cycles < 1000:
    cycles += 1
    print(cycles)
    while cycles < 500:
        # Does calculations
        temp = numbers[-1]
        numbers.append(temp + 5)

        # Adds cycle number and prints it
        cycles += 1
        print(cycles)

    while cycles > 500 and cycles < 1000:
        # Does calculations
        temp = numbers[-1]
        numbers.append(temp + 20)

        # Adds cycle number and prints it
        cycles += 1
        print(cycles)

plt.plot(numbers)
plt.show()
