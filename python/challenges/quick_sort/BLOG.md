# Code 

def quick_sort(numbers):

    length = len(numbers)
    if length <= 1:
        return numbers
    else:
        pivot = numbers.pop()

    numbers_lower = []
    numbers_greater = []

    for item in numbers:
        if item > pivot:
            numbers_greater.append(item)

        else:
            numbers_lower.append(item)

    return quick_sort(numbers_lower) + [pivot] + quick_sort(numbers_greater)

"print(quick_sort([7,6]))"


# Tracing the code

1. Numbers => list[7,6]
2. Length = 2
3. Pivot = 6
4. numbers_lower = []
5. numbers_greater= []
6. Looping in the numbers with item, so now item = 7
7. Check if item greater then pivot, if yes it will be append in the numbers_greater list.
8. Now the numbers is empty list, and the length is is zero
9. Now we are checking if the length is less or equal than 1 then return the numbers
10. Now going back to the beggining of the function, numbers contains only 7 and the length is 1
11. it will return the numbers now again, because the length is less or equal than 1
12. At the end it wil return quick_sort(numbers_lower) + [pivot] + quick_sort(numbers_greater)


# Test


from challenges.quick_sort.quick_sort import quick_sort

def test_quick_sort():

    actual = quick_sort([5,2,6,0])
    excpected = [0, 2, 5, 6]
    assert excpected == actual

def test_quick_sort2():

    actual = quick_sort([20,18,12,8,5,-2])
    excpected = [-2, 5, 8, 12, 18, 20]
    assert excpected == actual

def test_quick_sort3():

    actual = quick_sort([5,12,7,5,5,7])
    excpected = [5, 5, 5, 7, 7, 12]
    assert excpected == actual

def test_quick_sort4():

    actual = quick_sort([2,3,5,7,13,11])
    excpected = [2, 3, 5, 7, 11, 13]
    assert excpected == actual


![Insertion_sort](../assets/quick_sort.PNG)