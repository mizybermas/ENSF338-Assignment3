import sys

my_list = []
size = sys.getsizeof(my_list)
print(
    f"length of array is {len(my_list)}: initial size of empty array is {sys.getsizeof(my_list)} bytes")
for i in range(64):
    my_list.append(i)
    # print new size of the array when reallocation happens
    if sys.getsizeof(my_list) != size:
        print(
            f"length of array is {len(my_list)}: new array size is {sys.getsizeof(my_list)} bytes")
        size = sys.getsizeof(my_list)
