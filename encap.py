class Student:
    school="shsc"
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def details(self):
        print("Name=",self.__name)
        print("Age=",self.__age)
        print("School=",Student.school)





class Marks(Student):
    def marks(self,hindi,math):
        self.hindi=hindi
        self.math=math
    def Complete_details(self):
        print("Name=",self.__name)
        print("Age=",self.__age)
        print("School=",Student.school)
        print("Hindi=",self.hindi)
        print("Math=",self.math)
obj= Marks("sanchita",22)
obj.__name = "sanchu"
obj.details()
obj.marks(88,89)
Student.school="martand 1"
obj.complete_details()












