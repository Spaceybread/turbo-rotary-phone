import random
import matplotlib.pyplot as plt

startX = random.randint(-100, 100)
startY = random.randint(-100, 100)

x = []
y = []

x.append(startX)
y.append(startY)

init = [startX, startY]

addX = 0
addY = 0

n = 0

while n != 100000:
    addX = random.randint(-100, 100)
    addY = random.randint(-100, 100)

    startX = startX + addX
    #startX = startX + 1
    startY = startY + addY

    x.append(startX)
    y.append(startY)

    n = n + 1

#print(x)
#print(y)

d = ((init[0] - startX)**2 + (init[1] - startY)**2)**0.5

print(init[0])
print(init[1])
print(d)

plt.plot(x, y)
plt.show()
