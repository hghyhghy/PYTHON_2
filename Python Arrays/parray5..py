# searching element using index()

import array as arr

l1 = [2, 3, 4, 5, 6, 7, 8, 9, 10]

a1 = arr.array("i", l1)

for sb in range(0, 8):
    print("\n", a1[sb], end=" ")

    print()

print("The index of number 2 is ")

print(a1.index(3))

print("The index of 4 is ")

print(a1.index(4))

# append operation to add elements at the last

print(a1.append(11))

print(a1)
