from random import randint
import matplotlib.pyplot as plt
import time

# Make n to plot
n = [1000]  # Makes a list that we will add n too and will plot

c = 150 * 1000  # How many times it will loop
ct = 125 * 1000
cm_up = 25
cm_down = 1
up_m = 1
down_m = 2

td = 0
words = 0

time_1 = time.time()
while td < c:
    if td >= ct:
        up_m = cm_up
        down_m = cm_down
    down = (n[-1] - 1 * down_m)
    up = (n[-1] + 1 * up_m)
    td += 1
    n.append(randint(down, up))  # Adds something to the list
    words += 1
    while 100 == words:
        print("Times done : ", td, "Times left : ", c - td)
        words = 0
time_2 = time.time()

print("Did", c, "calculations in", (time_2 - time_1))
plt.plot(n)
plt.show()
