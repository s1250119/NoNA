from random import Random

print("Rolling the dice...")
r = Random()
x = r.randint(1,6)
y = r.randint(1,6)
print("Die 1: ") + str(x)
print("Die 2: ") + str(y)
print("Total value: ") + str(x+y)

