import array as arr

a2 = arr.array("i", [34, 34, 56, 67, 78])

for t in range(0, 5):
    print("\n", a2[t], end=" ")

    print()

# counting the occurance of a particular  element bu count()

count = a2.count(34)

print("Thee occurance of number 34 is ", count)

# extends the array with extend()

temp = a2.extend([89, 90, 99, 100])

print("The extends version of array is ", a2)
