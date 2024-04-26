# Prompting the user to enter three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Task 1: Identifying the Greatest
max_num = max(num1, num2, num3)
print("The largest number is:", max_num)

# Task 2: Identify the Smallest
min_num = min(num1, num2, num3)
print("The smallest number is:", min_num)

# Task 3: Equality Check
if num1 == num2 == num3:
    print("All numbers are equal.")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Two numbers are equal.")
else:
    print("Numbers are not equal.")