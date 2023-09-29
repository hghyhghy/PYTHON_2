# creating an empty array

import array as arr

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = arr.array("i", l)

print("The initial array")

for i in a:
    print("\n", i, end=" ")

    print()


sliced_array = a[3:9]

print("The sliced arrays are ")

print(sliced_array)

# slicing an array from index 5

sliced_array1 = a[5:]

print("The sliced array")

print(sliced_array1)
