
# ******************************
# Make your Code
# ******************************

import random

numbers = []
for i in range(10):
    numbers.append(random.randint(0, 100))

print(numbers)
print(f"Min value: {min(numbers)}")
print(f"Index: {numbers.index(min(numbers))}")