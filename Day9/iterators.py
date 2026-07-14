            #Iterables vs iterators
        #iterable
    #An iterable is any object you can loop over
    
    #Examples
    #-->List
    #-->Tuple
    #-->String
    #-->Dictionaries
    #-->Set
    
#iterable
numbers = [10,20,30]
for num in numbers:
    print(num)
    
    #Iterator
    #An iterator keeps track of its current position
    #Create an iterator using iter().
numbers=[10,20,30]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
"""
#try one more next() raise StopIteration exception
print(next(iterator))
"""


    #Creating a custom iterator
class counter:
    def __init__(self,limit):
        self.limit = limit
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value
        raise StopIteration
counter = counter(5)
for number in counter:
    print(number)