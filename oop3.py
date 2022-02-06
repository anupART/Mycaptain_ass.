class student :
    college_name="IIT Bombay" #class attribute
    #instance attributes
    def _init_(self, name, age , dob) :
        print("Constructor is Initilize")
        self._name=name
        self._age=age
        self._dob=dob
        
        
    def print_name(self):
        print("Student name "+self._name)
         
        
    def increment_age(self):
        self._age=self._age+1
        print("Age of Student "+self._name+"is" +str(self._age))   
        
student_1=student("Raj",23,"09/05/1994") 
student_2=student("Ujjwal",23, "19/03/2002")

# print(student_1._name, student_1._age, student_1._dob,student_1.college_name)
# print(student_2._name, student_2._age, student_2._dob,student_2.college_name)



student_1.print_name()
student_2.print_name()