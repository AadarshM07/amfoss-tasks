
#Write a program that reads a string from a file named input.txt and writes that string to another file named output.txt.
File=open("input.txt","r")
File2=open("output.txt","w")  #Opening the files
data=File.read()
File2.write(data)    #Adding the details
print("Task Completed")
File.close()
File2.close()   #closing files to avoid error


