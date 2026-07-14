            #enerators
        #A generator is a special function that uses yield instesd of return
def countdown(n):
    while n > 0:
        yield n
        n -= 1
for num in countdown(5):
    print(num)
    
    
    #return vs yield
    
    #return                     #yield
    #->Ends the function        #->pauses and resumes
    #->Returns one value        #Produces multiple values over time
    #->Uses more memory         #Memory efficient
    
    
        #Generation Expressions
    #Like list compressions,but use() instead of []
#List Compression

squares=[x * x for x in range(5)]
print(squares)

#Generator Expression

Squares = (x * x for x in range(5))
for value in squares:
    print(value)
    
    
    #Why generators Matter
#Imagine processing a 10 gb log file
#❌ Loading the entire file into memory:
#lines = file.readlines()

#✅ Processing one line at a time:
#for line in lines:
 #   print(line)
 
 #Generates allow efficient processing of large files and streams making them ideal for SOC log analysis
 