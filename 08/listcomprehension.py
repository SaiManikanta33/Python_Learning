
            #List comprehensions
    #create lists in a compact way.
#Without list comprehension 
square=[]
for i in range(1,6):
    square.append(i*i)
print(square)

#With list comprehension 

square=[i*i for i in range(1,6)]
print(square)

#With a condition
even = [x for x in range (1,11) if x %2==0]
print(even)