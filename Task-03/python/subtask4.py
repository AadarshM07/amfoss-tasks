#Sub-Task 4: Write a program that reads a number n from a file named input.txt and generates a diamond pattern of asterisks (*) in another file named output.txt.

File=open("input.txt","r")
File2=open("output.txt","w")  #Opening the files
data=File.read()
data=int(data)
for k in range(1, data+1, 2):
    File2.write(" " * ((data-k) // 2) + "*" * k + "\n")
 
for k in range(data-2, 0, -2):
    File2.write(" " * ((data-k) // 2) + "*" * k +"\n")
print("Task Completed")
File.close()
File2.close()   #closing files to avoid error
