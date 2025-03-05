import os 

class Subject:
    def __init__(self,name,code,place,Teacher,Elective):
        self.name = name
        self.code = code 
        self.place = place
        self.Teacher = Teacher
        self.Elective = Elective
        
    def info(self,num):
        print("課程代碼:",self.code[num])
        print("課程名稱:",self.name[num])
        print("課程地點:",self.place[num])
        print("課程老師:",self.Teacher[num])
        print("修別:",self.Elective[num])

        
#if的用法避免了類別被呼叫時測試植被重複輸出
if __name__ == "__main__":
    teacher = Teacher("王")
    teacher.getName()