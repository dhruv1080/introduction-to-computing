#-------------------------------assignment-4----------------------------------------------

#-------------------------------question-1------------------------------------------------
print("-------question-1--------")
print("steps to solve the tower of hanoi problem are given below:-")
def tower(n,s,d,h):
#here n is number of disks,s is source rod,d is final rod and h is helper rod
    if n==0:
        return None
    else:
        tower(n-1,s,h,d)
        print("Move disk",n,"from",s,"to",d)
        tower(n-1,h,d,s)

#calling tower function
tower(3,'source rod','final rod','helper rod')

#-------------------------------question-2------------------------------------------------
print("-------question-2--------")
n=int(input("enter the number of rows of pascal's triangle="))

print("\nPascal's Triangle using recursion")
def pascaltriangle(n,m=n):
      if n==0:
            return None
      pascaltriangle(n-1,m)
      print(' '*(m-n),end='')
      c=1
      for i in range(1,n+1):
            print(c,end=' ')
            c=c*(n-i)//i
      print()
pascaltriangle(n)

print("\nPascal's Triangle using iteration")
for row in range(1,n+1):
      print(' '*(n-row),end='')
      b=1
      for i in range(1,row+1):
            print(b,end=' ')
            b=b*(row-i)//i
      print()

#-------------------------------question-3------------------------------------------------
print("-------question-3--------")
num1=int(input("enter the dividend="))
num2=int(input("enter the divisor="))

#denominator can't not be zero
while num2==0:
    num2=int(input("Denominator can't be zero,Please enter a non-zero number="))

r=num1%num2      #r=remainder
q=num1//num2     #q=quotient 
list1=[q,r]
print("remainder =",r)
print("quotient =",q)
call=callable(divmod(num1,num2))
if call==True:
    print("\m(a)fuction is callable")
if call==False:
    print("\n(a)fuction is not callable")
if q==0 and r==0:
    print("\n(b)Both the values are zero")
if q!=0 or r!=0:
      if q!=0 and r!=0:
            print("\n(b)Both the values are non zero")
      else:
            print("\n(b)One of the values is zero")

list1.extend([4, 5, 6])
print("\n(c)After adding [4,5,6] =",list1)
filtered = filter(lambda n: n > 4,list1)
print("   Values greater than 4 are",list(filtered))

set1=set(list1)
print("\n(d)set =",set1)

frozen_set=frozenset(set1)
print("\n(e)Immutable set =",frozen_set)

m = max(frozen_set)
print("\n(f) The hash value =",hash(str(m)))

#-------------------------------question-4------------------------------------------------
print("-------question-4--------")
class Student:
       def __init__(self,student,roll_no):
             self.name=student
             self.roll_no=roll_no
       def __del__(self):
             print("The object created has been destroyed.")
student1=Student("Dhruv Agrawal",21105070)
print(student1.name,",",student1.roll_no)
del student1

#-------------------------------question-5------------------------------------------------
print("-------question-5--------")
class Emp:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def detail(self):
        print("\t",self.name,"\t",self.salary)

e1=Emp("Mehak", 40000)
e2=Emp("Ashok", 50000)
e3=Emp("Viren", 60000)

print("Employee name | Salary")
e1.detail()
e2.detail()
e3.detail()
#a part
e1.salary=70000
print("\n(a)Updated salary of Mehak:")
e1.detail()
#b part
del e3
print("\n(b)Record of Vivek deleted")

#-------------------------------question-6------------------------------------------------
print("-------question-6--------")
word = input("Enter the word:")
new_word = input("Enter a new word:")
def letter(word):
    count={}
    list_1= list(word)
    n=len(list_1)
    for i in range(n):
        if list_1[i] in count:
            count[list_1[i]]=count[list_1[i]]+1
        else:
            count[list_1[i]] = 1
    return count
if letter(word)!=letter(new_word):
    print("\nletters used in both words are not same so friendship is fake")

else:
      def shopkeeper():
            Y_N = input("\nIs the new word meaningful?(Y/N):")
            if Y_N.lower() == 'y' or 'yes':
                  print("\nTheir friendship is true")
            elif Y_N.lower() == 'n' or 'no':
                  print("\nThe word has no sense so friendship is fake")
            else:
                  print("\nInvalid input,try again")
      shopkeeper()
