"""
Find maximum and minimum number
"""


def find_max_min(array):
    new_array = sorted(array)  #sorts the array from smallest to largest
    result = []
    
    for num in new_array:     
        if new_array[0] == new_array[-1]:  #checks if minimum is equal to maximum
            result.append(len(new_array))
            return result
        
    result.append(new_array[0])    #append results after the for loop
    result.append(new_array[-1])    
    return result
