#!/usr/local/bin/python3
#Open the file name data.txt in Write Mode
file1 = open("data.txt","w") 
data = list()

#select the amount of data one need to write
#redis_key : You redis where you want to insert
#redis_subkey : Key name
#redis_subvalue : Value that belongs to the key
for i in range(100):
	data.append("HSET redis_key "+str(i)+"redis_subkey redis_subvalue \n")

file1.writelines(data) 
file1.close()
