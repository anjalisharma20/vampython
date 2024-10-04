myname = open("myname.txt","w")
myname.write("macbook")
# newpassword = input("enter new password please:")
# myname.write(input("enter new password please:"))
#overwrite the new password using userinput

#read the password from file 
myname = open("myname.txt","r")
mydata = myname.read()
if "macbook" in mydata:
    print("yes")
else:
     print("no") 


#delete the file 
myname.close()
import os
os.remove("myname.txt")  