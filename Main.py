from typing import List

def insertionSort(array) -> List[int]:
    for y in range(len(array)):
       for x in range(1,len(array)):
          j=x-1
          while(array[x-1]>array[x] and j>=0):
             array[x],array[x-1]=array[x-1],array[x]
             j-=1
    return array

input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
