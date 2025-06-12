num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
add = num1 + num2
diff = num1 - num2
prod = num1 * num2
# Handle division by zero
if num2 != 0:
    div = num1 / num2
else:
    div = "undefined (division by zero)"
user = input("Enter the Operation You Want (sum/difference/product/division): ").lower()
if user == "sum":
    print("The Sum is:", add)
elif user == "difference":
    print("The Difference is:", diff)
elif user == "product":
    print("The Product is:", prod)
elif user == "division":
    print("The Division is:", div)
else:
    print("Invalid option!")
