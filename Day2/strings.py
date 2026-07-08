            #creating strings
name="Cyber Security"
college="Raghu Engineering college"

            #Accessing characters
print(name[0]) #prints first character
print(name[-1]) #prints last character

            #slicing 
print(name[0:6]) #prints first 6 characters
print(name[6:14]) #prints from 6th to 14th character
print(name[:6]) #prints first 6 characters
print(name[::-1]) #prints the string in reverse order


            #usefull string methods
msg="Cyber Security"
print(msg.upper()) #converts to uppercase
print(msg.lower()) #converts to lowercase
print(msg.title()) #converts to title case
print(msg.strip()) #removes whitespace from both ends
print(msg.replace("Cyber","Information")) #replaces substring
print(msg.count("e")) #counts occurrences of substring
print(len(msg))



            #f-strings
name="sai"
age=19
print(f"{name} is python developer at the age of {age}.") #f-string formatting