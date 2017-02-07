"""
 Create a function fizz_buzz to return 'Fizz', 'Buzz', 'FizzBuzz' or the argument it recieves all depending on the argument of the function, a number that is divisible by, 3, 5, or both 3 and 5, respectively.
 When the number is not divisible by 3 or 5, the number itself should be returned.
"""

def fizz_buzz(x):
    if x % 3 == 0 and x % 5 == 0: #checks if number divisible by both 3&5
        return 'FizzBuzz'
    elif x % 3 == 0:     #checks if number divisible by 3
       return 'Fizz'
    elif x % 5 == 0:   #checks if number divisible by 5
        return 'Buzz'
    elif x % 3 != 0 and x % 5 != 0: #checks if number divisible by 3 or 5
        return x


