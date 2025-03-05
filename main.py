#老師 學生 課程0 
import os 
from teacher import Teacher
from student import Student
from subject import Subject

student_Name = input("學生名字:")
student_Email = input("學生Email:")
student_ID = input("學生ID:")

student = Student("student_Name","student_Email","student_ID")

teacher1 = Teacher("朱邵威","EMAIL",["系統架構"])
teacher2 = Teacher("劉秉睿","EMAIL",["深度學習","數位影像"])

subject_List = Subject(["系統架構","深度學習","數位影像"],
                        ["4106","4137","4109"],
                        ["四 05-07 (國秀樓K216教室)","四 02-04 (國秀樓K216教室)","四 05-07 (工具機學院大樓四樓VA403教室)"],
                        ["朱邵威","劉秉睿","劉秉睿"],
                        ["選修","必修","選修"])

subject = input("想要科目(系統架構、深度學習、數位影像):")

for i in range (0,len(subject_List.name)-1):
    if subject_List.name[i] == subject:
        subject_List.info(i)
        break


for i in teacher1.subject: 
    if i==subject:
        teacher1.info()
for i in teacher2.subject: 
    if i==subject:
        teacher2.info()

