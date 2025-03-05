import os 

class Teacher:
    def __init__(self, name,email,subject):
        self.name = name
        self.email = email
        self.subject = subject
        
    def info(self):
        print(self.name,end=" ")
        print(self.email,end=" ")
        print(self.subject,end=" ")
        
#if的用法避免了類別被呼叫時測試植被重複輸出
if __name__ == "__main__":
    teacher = Teacher("王")
    teacher.getName()