#-------------------------------assignment-2----------------------------------------------

#-------------------------------question-1------------------------------------------------
input_string="Python is a case sensitive language"

print("-------part-a--------")
print(len(input_string),"\n")

print("-------part-b--------")
print(input_string[::-1],"\n")

print("-------part-c--------")
new_string=input_string[10:26]
print(new_string,"\n")

print("-------part-d--------")
another_string=input_string.replace("a case sensitive","object oriented")
print(another_string,"\n")

print("-------part-e--------")
print(input_string.index("a"),"\n")

print("-------part-f--------")
print(input_string.replace(" ",""),"\n")

#-------------------------------question-2------------------------------------------------
print("-------question-2--------")
name="dhruv agrawal"
department="ECE"
cgpa=10.0
SID=21105070
print("Hey,",name,"Here!","\nMy SID is",SID,"\nI am from",department,"department and my CGPA is",cgpa,"\n")

#-------------------------------question-3------------------------------------------------
print("-------question-3--------")
a=56
b=10

print("-------part-a--------")
print("a&b:",a & b,"\n")

print("-------part-b--------")
print("a|b:",a | b,"\n")

print("-------part-c--------")
print("a^b:",a ^ b,"\n")

print("-------part-d--------")
print("a<<2:",a<<2,"\tb<<2:",b<<2,"\n")

print("-------part-e--------")
print("a>>2:",a>>2,"\tb>>2:",b>>4,"\n")

#-------------------------------question-4------------------------------------------------
print("-------question-4--------")
num1=float(input("enter the first no.-"))
num2=float(input("enter the second no.-"))
num3=float(input("enter the third no.-"))

if num1>num2 and num1>num3:
    greatest=num1
elif num2>num1 and num2>num3:
    greatest=num2    
else:
    greatest=num3
print("the greatest no.-",int(greatest),"\n")

#-------------------------------question-5------------------------------------------------
print("-------question-5--------")
string=input("enter something-")
if "name" in string:
    print("yes")
else:
    print("no")
print("\n")

#-------------------------------question-6------------------------------------------------
print("-------question-6--------")
len_1st=int(input("enter length of first side-"))
len_2nd=int(input("enter length of second side-"))
len_3rd=int(input("enter length of third side-"))

if len_1st+len_2nd<len_3rd or len_2nd+len_3rd<len_1st or len_3rd+len_1st<len_2nd:
    print("no")
else:
    print("yes")
print("\nthank you")




















