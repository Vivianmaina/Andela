"""
Define a function called data_type to take one argument.
Compare and return results based on the argument supplied to the function.
Compete the test to produce the perfect function that accounts all expectations.
"""
def data_type(x):
    if x == None:    #Checks if value is null
        return 'no value'  
    elif type(x) == str: #checks if value is of string type
        if len(x)>0:
            return len(x)
        elif x == "":
            return 'No value'
    elif type(x) == bool: #checks if value is of boolean type
            return x
    elif type(x) == int: #checks if value is of integer type
        if x < 100:
            return 'less than 100'
        elif x > 100:
            return 'more than 100'
        elif x == 100:
            return 'equal to 100'
    elif type(x) == list: #checks if value is a list
        if len(x)>=3:
            return x[2]
        elif len(x)<3:
            return None
