#list can store multiple data ,data can be different int str 
#list can store the duplicate data
#list is an ordered data set - sorting asending decending 

#create list  and store the your friends name 
friendlist = ["ivan","saloni","kashish","mahi"]

#print the age of your friends into list
#append will add the data into end of the list
# friendlist.append (21)
# friendlist.append (17)
# friendlist.append (23)
# friendlist.append (10)

print(friendlist)
#add the data into list using index no
friendlist.append("ayush")
# print(friendlist)
print(friendlist)
# add the data into list using index no
friendlist.insert(3,"anjali")
# print(friendlist[3])
print(friendlist)

#pop will delete the data using index
friendlist.pop(1)
print(friendlist)

#add the  5 favt city name in list
#add my favt city kasol in index 0
#remove the last city in list - using pop
#sorting the list data
#print the list data 
favouritcity=["delhi","mumbai","goa","punjab","jaipur"]
favouritcity.append("kasol")
print(favouritcity)