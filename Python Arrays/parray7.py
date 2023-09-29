# creating an empty array
import array as arr

a2 = arr.array("i", [34, 45, 56, 67, 78])

for t in range(0, 5):
    print("\n", a2[t], end=" ")

    print()

# reversin the array

a2.reverse()

print(a2)
