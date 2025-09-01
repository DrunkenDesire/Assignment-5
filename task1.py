student_name={"Ram":35,"Shyam":45,"Abhay":78,"Parul":67,"Kashish":79,"Bhavy":99,"Chirag":88}
x=input("Enter the student's name : ")
if x in student_name:
   y=student_name.get(x)
   print("{} marks:{}".format(x,y))
else:
    print("Student not found")
