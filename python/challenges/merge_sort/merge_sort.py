def merge_sort(list):
  n = len(list)
  if n > 1:
    m = int(n/2)
    l = list[0:m]
    r = list[m:n]
    merge_sort(l)
    merge_sort(r)
    merge(l, r, list)
  return list

def merge(l, r, list):
  i = 0
  j = 0
  k = 0
  while i < len(l) and j < len(r):
    if l[i] <= r[j]:
        list[k] = l[i]
        i = i + 1
    else:
        list[k] = r[j]
        j = j + 1  
    k = k + 1
  if i == len(l):
    while j < len(r):
      list[k] = r[j]
      j += 1
      k += 1
  else:
    while i < len(l):
      list[k] = l[i]
      i += 1
      k += 1

if __name__ == "__main__":
  list = [55,2,0,1,53,35,22]
  merge_sort(list)