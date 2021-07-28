# Classic Search and Sort Algorithms

# Searches: Linear Search and Binary Search

def linearSearch(values: list, target: int) -> int:
  """ Search a list and return the index if found. 
  Returns -1 if target is not found.
  """
  for i in range(len(values)):
    if target == values[i]:
      return i
  
  return -1  

def binarySearch(values: list, target: int) -> int:
  """ Search a list and return the index if found. 
  Returns -1 if target is not found.
  """
  lower: int = 0
  upper: int = len(values) - 1

  while lower <= upper: 
    mid: int = (lower + upper) // 2

    if target == values[mid]:
      return mid
    elif values[mid] > target:
      upper = mid - 1
    else:
      lower = mid + 1

  return -1 

# Sorts: Bubble Sort, Merge Sort, Selection Sort, Insertion Sort

def bubbleSort(unsortedValues: list) -> None:
  """ Sorts a list of unsorted values. """
  
  done: bool = False      # initialize to false 
  sortedCount: int = 0

  while not done: 
    done = True
    index: int = 0

    while index < len(unsortedValues) - 1 - sortedCount:
      if unsortedValues[index] > unsortedValues[index + 1]:
        swap(unsortedValues, index, index + 1)
        done = False
      index += 1
    sortedCount += 1

def mergeSort(values: list) -> list:
  if len(values) <= 1: 
    return values
  
  sortedValues: list = []
  mid: int = len(values) // 2
  lowerHalf: list = mergeSort(values[:mid])
  upperHalf: list = mergeSort(values[mid:])

  while len(lowerHalf) > 0 and len(upperHalf) > 0:
    if lowerHalf[0] < upperHalf[0]:
      sortedValues.append(lowerHalf.pop(0))
    else:
      sortedValues.append(upperHalf.pop(0))

  if len(lowerHalf) > 0: 
    sortedValues.extend(lowerHalf)
  elif len(upperHalf) > 0:
    sortedValues.extend(upperHalf)

  return sortedValues

def insertion_sort(values: list) -> None:
    for i in range(1, len(values)):
        temp: int = values[i]
        j: int = i - 1
        while j >= 0 and values[j] > temp:
            values[j + 1] = values[j]
            j = j - 1
        values[j + 1] = temp
    
def selection_sort(values: list) -> None:
    for i in range(len(values)):
        best: int = i
        for j in range(i + 1, len(values)):
            if values[j] < values[best]:
                best = j
        swap(values, i, best)

# Helper Functions

def swap(values: list, i = int, j = int) -> None:
  """ Swap values[i] with values[j] inside of list values. """
  
  temp: int = values[i]
  values[i] = values[j]
  values[j] = temp


    