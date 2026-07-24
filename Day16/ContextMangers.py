        #Context Managers

    #we don't have text file because i am creating text file
"""    
with open("Day16/Notes.txt","w")as file:
    print(file.write("Hello, Python"))
    print(file.write("\nLearning Python"))    
    file.close()"""

    
 
with open("Day16/Notes.txt","r") as file:
    print(file.read())
    
"""   #The 'with' statement automatically closes resources   """
    
    #Creating your own Context Manager
    
class DBConnection:
    def __enter__(sai):
        print("Connected to DataBase")
        return sai

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Database connection closed")

with DBConnection():
    print("Running queries...")
    
    
    