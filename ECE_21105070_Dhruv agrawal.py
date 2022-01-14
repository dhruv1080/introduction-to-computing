#-------------------------------assignment-1----------------------------------------------

#-------------------------------question-1------------------------------------------------
print("-------question 1--------")
num1=float(input("enter your first no.="))
num2=float(input("enter your second no.="))
num3=float(input("enter your third no.="))
avg=(num1+num2+num3)/3
print("average=",avg,"\nthank you")

#-------------------------------question-2------------------------------------------------
print("-------question 2--------")

#taking input from user
gross_income=round(float(input("enter your gross income=")))
num_dependent=int(input("enter number of dependents="))

standard_deduction=10000
deduc_per_depen=3000

taxable_income=gross_income-standard_deduction-(deduc_per_depen*num_dependent)
tax_rate=1/5
tax=taxable_income*tax_rate
print("amount of tax you have to pay=",tax)
print("thank you")

#-------------------------------question-3------------------------------------------------
print("-------question 3--------")
print("Student=[SID, Name, Gender, Course Name, CGPA]")
student=[21105070,"Dhruv agrawal","M","ECE",10.0]
print(student,"\nthank you")

#-------------------------------question-4------------------------------------------------
print("-------question 4--------")
print("marks of 5 students:-")
marks=[50,80,70,90,60]
print("marks before sorting=",marks)
marks.sort()
print("marks after sorting=",marks,"\nthank you")

#-------------------------------question-5------------------------------------------------
#-------------------------------part-a----------------------------------------------------
print("-------question 5--------")
print("---------part-a----------")
color=["Red", "Green", "White", "Black", "Pink", "Yellow"]
print("before removing 4th element")
print("color:-",color)
del color[3]
print("after removing 4th element")
print("color:-",color)
print("thank you")

#-------------------------------part-b-----------------------------------------------------
print("-------question 5--------")
print("---------part-b----------")
color=["Red", "Green", "White", "Black", "Pink", "Yellow"]
print("color:-",color)
color[3:5]=["purple"]
print("after replacing black and pink with purple")
print("color:-",color)
print("thank you")
