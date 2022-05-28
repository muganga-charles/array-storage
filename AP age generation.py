from array import *
sum=0
age=array('i',[])#creating an array
people=int(input("enter the number of people"))#asking the user to enter the number of people
age_one=int(input("enter the age for the first person"))#asking the user to enter the age for the first person
diffrence=int(input("enter the common diffrence"))
for i in range(0,people):#for loop to ask the user to enter the age for the other people
    next=age_one+i*diffrence
    print("the age for person",i+1,"is",next)
    age.append(next)#appending the ages to the array
    sum+=next

print(age,"\n Average=",sum/people)#printing the age and the average
