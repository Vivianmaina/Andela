def find_missing(array1, array2):
  
  if len(array1) > 0 and len(array2) > 0:
    
    if array1 == array2:
      return 0
      
    else:
      combinedList = set(array1).union(set(array2))
      differenceList = set(array1).intersection(set(array2))
      result = set(combinedList - differenceList)
      for i in result:
        return i
      
  else:
        return 0