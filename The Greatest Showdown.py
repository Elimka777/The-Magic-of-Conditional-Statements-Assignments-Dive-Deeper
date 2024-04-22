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
elif num3 != num1 or num2 != num1 or num2 != num3:
    print("Numbers are not equal.")
else:
    print("Two numbers are equal.")