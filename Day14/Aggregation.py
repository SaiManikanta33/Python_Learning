        #Aggregation
    # Aggregation means one object uses another object , but both can exist independently.

class teacher:
    def __init__(self,name):
        self.name = name
class college:
    def __init__(self,Teacher):
        self.Teacher = Teacher
        
Teacher = teacher("Mr. Manikanta")
College = college(Teacher)
print(College.Teacher.name)

        # Teacher can exist even without the College