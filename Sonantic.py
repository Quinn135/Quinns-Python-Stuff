import matplotlib.pyplot as plt

# 3X + 1

s = 83447
x = s
t = 1
c = 1
n = []


while True:
    print(t, x)
    if x % 2 == 0:
        x = x / 2
        n.append(x)
    else:
        x = x * 3
        x = x + 1
        n.append(x)
    if n[-1] == 1.0:
        if t < c:
            t += 1
            x = s * t
        else:
            break

plt.plot(n)
plt.show()
