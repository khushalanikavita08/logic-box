#pattern
print("welcome to the pattern generator and number analyzer!\n")
print("select an option:")
print("1.generate a pattern")
print("2.analyze a range of numbers")
print("3.exit")
chocie=int(input("enter you choice:"))
row=int(input("enter the number of row for the  pattern:"))
print("\npattern:")
for i in range (1,row+1):
    for j in range (i):
        print("*",end="")
    print("")
    
#2 numerical 
print("\n select an option:")
print("1.generate a pattern")
print("2.analyze a range of numbers")
print("3.exit")
Choice=int(input(" enter your choice:"))
num1=int(input("\n enter the  num1 of  range :"))
num2=int(input("enter the num2 of range:"))
total=0
for i in range(num1,num2+1):
    if i%2==0:
         print("number" ,i,"is even")
    else:
       print("number" ,i,"is odd")
    total=total+i
print("sum of all number is" ,total )
    

print("\nselect an option:")
print("1.generate a pattern:")
print("2.analyze a rangeof numbers")
print("3.exit")
choice=int(input(" enter your choice:"))

print("exiting the program.goodbye! have a nice day")