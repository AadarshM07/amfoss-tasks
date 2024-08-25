# Sub-Task 3: Write a program that takes a number n from user and generates a diamond pattern of asterisks (*) and prints it to the console.

count = int(input("Enter n value: "))

for k in range(1, count+1, 2):
    print(" " * ((count-k) // 2) + "*" * k)
 
for k in range(count-2, 0, -2):
    print(" " * ((count -k) // 2) + "*" * k)

