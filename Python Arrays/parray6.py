import array as arr

a2 = arr.array("i", [34, 45, 56, 67, 78])

for t in range(0, 5):
    print("\n", a2[t], end=" ")

    print()

# updating the array


a2[3] = 9

print("After adding new elements to the list :")

for i in range(0, 5):
    print("\n", a2[i], end=" ")

    print()


a2[0] = 9


print("After adding new elements to the list :")

for i in range(0, 5):
    print("\n", a2[i], end=" ")

    print()


