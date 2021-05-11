import random
data_list = random.sample(range(50), 10)


def binary_search(data, search):
  data.sort()
  print(data)

  if len(data) == 1 and search == data[0]:
    return True
  
  if len(data) == 1 and search != data[0]:
    return False
  
  if len(data) == 0:
    return False
  
  mid = len(data) // 2
  if search == data[mid]:
    return True
  else:
    if search > data[mid]:
      return binary_search(data[mid:], search)
    else:
      return binary_search(data[:mid], search)


print(binary_search(data_list, 18))
"""
[0, 2, 5, 8, 19, 22, 23, 27, 32, 34]
[0, 2, 5, 8, 19]
[5, 8, 19]
[8, 19]
[8]
False
"""