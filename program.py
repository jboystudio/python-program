

#programme to find largest number of 3 numbers
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
num3 = int(input("enter the third number: "))

if (num1 > num2) and (num1 > num3):
  print("num1 is the largest")
elif(num2 > num1) and (num2 > num3):
  print("num2 is the largest")
else:
    print("num 3 is the largest")

#A company decided to give bonus to employee according to the following criteria
 #TIME PERIOD OF SERVICE          BONUS
  #More than 10 years            10%
  #>=6 and <=10                     8%
 # less than 6 years                5%
  #Ask user for their salary and years of service and print the net bonus amount.


salary = int(input("enter your salary: "))
years_of_service = int(input("Enter years of service: "))
    
if(years_of_service > 10):
    bonus1 = 0.10*salary
    print("your bonus amount is: ", bonus1)
    print("final salary is: ", bonus1 + salary)
    
elif(years_of_service >=6) and (years_of_service <=10):
    bonus2 = 0.08*salary
    print("your bonus amount is: ", bonus2)
    print("final salary is: ", bonus2 + salary)
elif(years_of_service < 6):
    bonus3 = 0.05*salary
    print("your bonus amount is: ", bonus3)
    print("final salary is: ", bonus3 + salary)
else:
    print("no bonus amount")


#create a grading system using the following conditions:
#SCORE            GRADE
#70 - 100           A
#60 - 69            B
#50 - 59            C
#40 - 49            D
#0 - 39             E

math = int(input("Enter your maths marks: "))
python = int(input("Enter your python marks: "))
geo = int(input("Enter your geo marks: "))
average = (math + python + geo)/3 

  
if(average > 70 and average < 100):
        print("your score is A")
elif(average > 60 and average < 69):
        print("your score is B")
elif(average > 50 and average < 59):
        print("your score is C")
elif(average > 40 and average < 49):
        print("your score is D")
elif(average < 39):
        print("YOU'VE FAILED")
else:
        print("Your marks are invalid")
