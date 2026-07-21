        #Coplete OOP Example 
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass
class Developer(Employee):
    def work(self):
        print("Writing Python Code")
class Analyst(Employee):
    def work(self):
        print("Monitoring Security Logs")
employees = [Developer(),Analyst()]
for employee in employees:
    employee.work()