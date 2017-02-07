class Student(object):    #base class
    def __init__(self,name,student_code,age): #initializing the object student
        self.name = name                     #attributes of the object student
        self.student_code = student_code

    def talk(self):
       pass    

class Preunit(Student):   #Preunit(derived class) inherited from base class Student
    def __init__ (self,name,student_code, age, grade_level, parent_name ):
        Student.__init__(self)    #derived class must explicitly call the base class __init__method
        self.grade_level = grade_level
        self.parent_name = parent_name

    def whoAmI(self):   # a method essential in encapsulation
        print "My name is %s, my parent is %s and i am in grade %s" %(name,parent_name,grade_level)  

    def talk(self):
        print "poor speech"

Charles = Preunit()   # creating an instance
Charles.whoAmI() 
Charles.talk()    # a polymorphism case  

      
