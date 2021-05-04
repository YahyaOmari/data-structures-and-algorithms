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
def BinarySearch(list, key):
    for i in range(len(list)):
        if list[i] == key:
            print(2)
            return 2
    print(-1)
    return -1    

BinarySearch([4,8,15,16,23,42], 42)

BinarySearch([11,22,33,44,55,66,77], 90)