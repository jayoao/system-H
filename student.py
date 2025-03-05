import os 

class Student:
    def __init__(self,name,email,studentID):
        self.name = name
        self.email = email
        self.studentID = studentID
        
    def info(self):
        print(self.name)
        print(self.email)
        print(self.studentID)
        
#if的用法避免了類別被呼叫時測試植被重複輸出
if __name__ == "__main__":
    student = Student("王")
    student.getName()