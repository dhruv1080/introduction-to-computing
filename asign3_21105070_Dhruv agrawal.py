#-------------------------------assignment-1----------------------------------------------

#-------------------------------question-1------------------------------------------------
print("-------question-1--------")
string=input("enter something=")
string=string.lower().strip()
m=0
dict={}
if " " not in string:
    while m<len(string):
        count=0
        y=0
        while y<len(string):
            if string[m]==string[y]:
                count+=1
                y+=1
            else:
                y+=1
        dict[string[m]]=count
        m+=1

else:
    list = str.split(string)
    while m<len(list):
        count=0
        y=0
        while y<len(list):
            if list[m]==list[y]:
                count+=1
                y+=1
            else:
                y+=1
        dict[list[m]]=count
        m+=1
print("no. of occurances of each character are as follows:-")
for key,value in dict.items():
    print(key,"=",value)

#-------------------------------question-2------------------------------------------------
print("-------question-2--------")
#leap year function
def leapyear(x):
    #leap year condition
    if (x%400)==0 or ((x%100!=0) and (x%4==0)):
        return True
    else:
        return False

day=int(input("Enter Day [1-31]:"))
month=int(input("Enter Month [1-12]:"))
year=int(input("Enter Year [1800-2025]:"))
#condition1-for dates out of range
if day<1 or day>31 or month<1 or month>12 or year<1800 or year>2025:
    condition1=False
else:
    condition1=True

#condition2-when day entered does not present in that month
#List containing month with 31 days
month_31 = [1, 3, 5, 7, 9, 11]  
#List containing month with 30 days
month_30 = [4, 6, 8, 10, 12]    
#for day entered 31 does not present in that month
t1a= day==31 and (month in month_30)
#for day entered greater than 29 in month february i.e 2
t1b= day>29  and month==2
#for day entered greater than 28 in february in non leapyear
t1c= day==29 and (not leapyear(year)) and month==2
if t1a or t1b or t1c :
    condition2=False
else:
    condition2=True
#error for wrong date
if t1a:
    print(f"\nError\n{day} day can't be in month {month}")
elif t1b:
    print(f"\nError\n{day} day can't be in month {month}")
elif t1c:
    print(f"\nError\n{day} day can't be in month {month} as the year {year} in not leapyear")
elif condition1==False:
    print(f"\nError\nPlease enter date in range day[1-31], month[1-12], year[1800-2025] ")

#Code when date entered is correct
if condition1==True and condition2==True :
    month_31 = [1, 3, 5, 7, 9, 11]  #List containing month with 31 days
    month_30 = [4, 6, 8, 10, 12]    #List containing month with 30 days
    #For month with 31 days
    if (month in month_31) == True:
        if day == 31:
            day = 1
            month = month + 1
        elif 1 <= day <= 30:
            day = day + 1
    #For month with 30 days
    elif (month in month_30) == True:
        if day == 30 and month == 12:
            day = 1
            month = 1
            year = year + 1
        elif day == 30 and month != 12:
            day = 1
            month = month + 1
        elif 1 <= day <= 29:
            day = day + 1
    #for february month i.e. month 2
    elif month == 2:
        # If year is leap year
        if leapyear(year) == True:
            if day == 29:
                day = 1
                month = month + 1
            elif 1 <= day <= 28:
                day = day + 1
        # If year is not leap year
        elif leapyear(year) == False:
            if day == 28:
                day = 1
                month = month + 1
            elif 1 <= day <= 27:
                day = day + 1
    # Printing Next date
    print(f"\nNext Date (Day/Month/Year): {day}/{month}/{year}")

#-------------------------------question-3------------------------------------------------
print("-------question-3--------")

list1=[]
while input("\nPlz enter Y to enter data or N to stop-").lower().strip()=="y":
    list_elem=int(input("input a no.-"))
    list1.append(list_elem)
print("\nyour entered no.=",list1)

list2=[]
for a in list1:
    tup=(a,a**2)
    list2.append(tup)
print("required result=",list2)

#-------------------------------question-4------------------------------------------------
print("-------question-4--------")
grade=int(input("enter your grade="))

if grade==10:
    print("Your Grade is 'A+' and Outstanding Performance")
elif grade==9:
    print("Your Grade is 'A' and Excellent Performance")
elif grade==8:
    print("Your Grade is 'B+' and Very Good Performance")
elif grade==7:
    print("Your Grade is 'B' and Good Performance")
elif grade==6:
    print("Your Grade is 'C+' and Average Performance")
elif grade==5:
    print("Your Grade is 'C' and Below Average Performance")
elif 0<=grade<=4:
    print("Your Grade is 'D' and Poor Performance")
else:
    print("please enter correct grade")

#-------------------------------question-5------------------------------------------------
print("-------question-5--------")
words="ABCDEFGHIJK"
f=0
while len(words)-f*2>=1:
    print(" "*f+words[0:len(words)-f*2])
    f+=1

#-------------------------------question-6------------------------------------------------
print("-------question-6--------")
condition=True
dict={}
enter="y"
while condition:
    if enter.lower()=="y":
        sid=int(input("\nenter the SID of the student= "))
        name=input("enter the name of the student= ")
        dict[sid]=name
        enter=input("\nto add more details- \npress Y(yes)\npress N(no)=")
        condition=True
    else:
        condition=False

#-------------------------------part-a----------------------------------------------------
print("\n---------part-a----------")
print("details of the students-")
for key,value in dict.items():
    print(key,":",value)

#-------------------------------part-b----------------------------------------------------
print("\n---------part-b----------")
sort1=sorted(dict.values())
print("dictionary after sorting by names= ",sort1)

#-------------------------------part-c----------------------------------------------------
print("\n---------part-c----------")
sort2=sorted(dict.keys())
print("dictionary after sorting by SID= ",sort2)

#-------------------------------part-d----------------------------------------------------
print("\n---------part-d----------")
search=int(input("enter the SID to get details= "))
if search in dict.keys():
    print("name of the student with SID-",sid,"is",dict[search])
else:
    print("SID not found")

#-------------------------------question-7------------------------------------------------
print("-------question-7--------")
number=int(input("enter no. of elements of fibonacci sequence-"))
a_n1=1
a_n2=0
n=0
sum=a_n1+a_n2

print(f"fibonnaci sequence with {number} elements are as follows:-")
print(a_n2)
print(a_n1)

while n<number-2:
    a_n=a_n2+a_n1
    a_n2=a_n1
    a_n1=a_n
    print(a_n)
    n=n+1
    sum+=a_n
average=sum/number
print(f"average of total {number} elements of sequence={average}")

#-------------------------------question-8------------------------------------------------
print("-------question-8--------")
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}
print(f"Set1={set1}\nSet2={set2}\nSet3={set3}")
      
#-------------------------------part-a----------------------------------------------------
print("\n---------part-a----------")
set_sym_dif=set1.symmetric_difference(set2)
print(set_sym_dif)

#-------------------------------part-b----------------------------------------------------
print("\n---------part-b----------")
set_u1=set1.union(set2)

set_uf=set_u1.union(set3)

set_i1=set1.intersection(set2)

set_if=set_i1.intersection(set3)

set_12=set1.intersection(set2)

set_23=set2.intersection(set3)

set_13=set1.intersection(set3)

#final required set
set_f1=set_uf-set_12-set_23-set_13
print(set_f1)

#-------------------------------part-c----------------------------------------------------
print("\n---------part-c----------")
set_c1=set_12.union(set_23)
set_c2=set_c1.union(set_13)
set_final=set_c2-set_if
print(set_final)

#-------------------------------part-d----------------------------------------------------
print("\n---------part-d----------")
set_d={1,2}
set_d.clear()
for i in range(1,11):
    set_d.add(i)
set_new=set_d-set1
#final required set
print(set_new)

#-------------------------------part-e----------------------------------------------------
print("\n---------part-e----------")
set_e=set_d-set_uf
print(set_e)
