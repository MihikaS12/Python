num1= int(input("Enter 1st Number:"))
num2= int(input("Enter 2nd Number:"))
add= num1+num2
diff=num1-num2
prod=num1*num2
div= num1/num2
user=input("Enter the Operation You Want")
if user=="sum":
  print("The Sum is : ",sum)
elif user=="difference":
  print("The Difference is: ",diff)
elif user=="product":
  print("The Product is: ",prod)
elif user=="division":
  print("The Division is: ",div)

else:
  print("invalid option!")



