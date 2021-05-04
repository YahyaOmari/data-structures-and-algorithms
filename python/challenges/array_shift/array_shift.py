def insertShiftArray(list,extra_number):
  extra_list = []
  list.append(extra_number)
  while list:
    sorting = list[0]
    for x in list:
      if x < sorting: 
        sorting = x
    extra_list.append(sorting)
    list.remove(sorting)
  print(extra_list)
  return extra_list


# insertShiftArray([2,4,6,2,0,77,88,99,14,10,112,8], -555)
# insertShiftArray([3,2,1,0,4,58,55,10], 7)