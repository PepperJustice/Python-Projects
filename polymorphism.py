
# parent class student
class Student:
    name = "Jude"
    email = "jude@gmail.com"
    password = "123abcd"
# method for parent class "Student"
    def studentLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Hi, welcome back, {}!".format(entry_name))
        else:
            print("The password or email you entereed is not correct.")

# child class StudentAid 
class StudentAid(Student):
    hours_scheduled = 10
    department = "General"
    pin_number = "5467"
# method for child class "StudentAid" with entry_password replaced by entry_pin
    def studentLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your StudentAid pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome, {}!".format(entry_name))
        else:
            print("The pin or email you entered is not recognized")

# child class Tutor
class Tutor(Student):
    students_tutored = 4
    subjects = "General"
    tutor_code = "1345"
# method for child class Tutor with tutor_code instead of entry_password 
     def studentLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        tutor_code = input("Enter your Tutor code: ")
        if (entry_email == self.email and tutor_code == self.tutor_code):
            print("Welcome, {}!".format(entry_name))
        else:
            print("The code or email you entered is not recognized")
    
    



    
student = Student()
student.studentLoginInfo()

TA = StudentAid()
TA.studentLoginInfo()

tutor = Tutor()
Tutor.studentLoginInfo()

