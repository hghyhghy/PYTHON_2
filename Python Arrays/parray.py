import array as arr

a = arr.array("i", [1, 2, 3])

print("After adding first integer elements to the array it becomes ", end=" ")

for i in range(0, 3):
    print(a[i], end=" ")


b = arr.array("d", [2.5, 3.5, 4.5])

print("After adding first double elements to the array it becomes ", end=" ")

for i in range(0, 3):
    print(b[i], end=" ")

    # print()
