import array as arr

a = arr.array("i", [67, 68, 69])

for k in range(0, 3):
    print("\n", a[k], end=" ")

    print()

# accessing elements from the array


print("The first  element of the array is ")

print(a[0])

print("The first  second  of the array is ")

print(a[1])

print("The first  third  of the array is ")

print(a[2])

# creating array of float type

b = arr.array("d", [1.6, 2.6, 3.6, 4.6, 5.6, 6.6])

for k in range(0, 6):
    print("\n", b[k], end=" ")

    print()


# accessing the elements from array


print("The first  element of the array is ")

print(b[0])

print("The second   element of the array is ")

print(b[1])
