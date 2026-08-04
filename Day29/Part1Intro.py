

    #1. What is an iterator?
#An iterator is an object that lets you access elements one at a time.

numbers = [10,20,30]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))       #Calling next() again after the last item raises a StopIteratation exception

    #2. What is a Generator?
#A generator is a special function that uses yield instead of return

def count():
    yield 1
    yield 2
    yield 3
for number in count():
    print(number)           #Unlike return , yield pauses the function and resumes where it left off.

    
    #3. Why use generators?
#Using a list:
numbers = [i for i in range(1_000_999)]     #This stores all one million numbers in memory.

#Using a generator:
numbers = (i for i in range(1_000_000))     #Number are created only when needed which uses much less memory.


