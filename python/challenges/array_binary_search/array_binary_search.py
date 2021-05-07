# First Way


# def BinarySearch(list,key):
#     x = key
#     if key in list:
#         print(2)
#         return 2
#     else:
#         print(-1)
#         return -1
#     # return key

# Second Way
# def BinarySearch(list, key):
#     for i in range(len(list)):
#         if list[i] == key:
#             print(2)
#             return 2
#     else:
#         print(-1)
#         return -1

# # Third way
def binary_search(list, key):
    list.sort()
    # print(list)
    low = 0
    high = len(list)-1

    # we want to check if the key is in the list or no
    while low <= high:
        mid = (low + high) // 2
        if key == list[mid]:
            print(2)
            return 2
        elif key < list[mid]:
            high = mid -1
        else:
            low = mid + 1
    print(-1)
    return -1




# binary_search([4, -10,8, 15, 16, 23, 42], -10)

# binary_search([11, 0,22, 33, 44, 55, 66, 77], 0)
# binary_search([4, 8, 15, 16, 23, 42], 1)

# binary_search([11, 22, 33, 44, 55, 66, 77], 0)

binary_search([111,3333,44444,100,11, 22, 33, 44, 55, 66, 77], 100)
# binary_search([4, 8, 15, 16, 23, 42], 900)
