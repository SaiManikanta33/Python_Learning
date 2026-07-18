
            #reduce() function
"""reduce() repeatedly combines values into a single result."""
from functools import reduce
number = [1,2,3,4]
total = reduce(lambda a,b:a+b,number)
print(total)