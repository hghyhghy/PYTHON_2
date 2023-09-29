import array as arr

a = arr.array("i", [1, 2, 3])

print("Elements of array before  inserting new elements to the array")

for i in range(0, 3):
    print("\n", a[i], end=" ")

    print()


# adding new elements to the array

print("Elements of array after inserting new elements to the array")


a.insert(1, 4)

for i in a:
    print("\n", i, end=" ")


# adding new float or double datatype to the type


print("Elements of array before r inserting double  elements to the array")


b = arr.array("d", [2.3, 4.3, 5.3])

for k in range(0, 3):
    print("\n", b[k], end=" ")

    print()

print("Elements of array after inserting  double elements to the array")

b.insert(0, 1.3)

for k in b:
    print("\n", k, end=" ")

    print()
