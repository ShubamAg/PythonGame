#=======================
#7st April 2025 Lecture
#=======================
#In the dicnary we use key name instead of index to specificaly get the value of or on sn appecific index.
dictvar= { "name":"Amit" ,
          "program":"MCA" ,
          "per" : 89.03 ,
          "city" : "pune"
          }
#print(dictvar) # print the whole dictionary

'''dictvar= {1: "Amit", 2: "MCA", 3: 89.30, "Address" : ["Pune", "Kothrud", "MIT"]} # inlcude the list in the dictionary
print(dictvar["Address"][0])# with this we will get the value of 0 index in the address
'''

'''dictvar= {1: "Amit", 2: "MCA", 3: 89.30, "Address" : ["Pune", "Kothrud", "MIT"]}
dictvar["name"] = "Rajesh"
dictvar["city"]= "Mumbai"
dictvar["div"] = "FY MCA-B"''' # since this is a new element is the dictionary it will append to the last in the dictionary automatically. The user can't control where it should go.
#print("After change :", dictvar)

'''for key in dictvar:
    print( key , ":" , dictvar[key])''' # Since the dictionary consist of two elements key and value here we are getting the key by for loop and once we got key in our hand we are printing the values automatically.

#print(dictvar.get("city")) # here we use the API to get the vlue of the key city.
#print(dictvar.get("Roll No.")) #If you use the the API and give the key that does not exist it won't give the error but instead it will return the value [None]
#print(dictvar("Roll No.") )# but using the print dictvar it will give the error

# <*> There is a file and we want to read the file content and find if the value is in the file and how many time the value has occured. Get the value and get the value in a dictionary.
 
'''for key in dictvar:
    print ( key , ":" , dictvar.get(key) )'''
    
'''print (dictvar.keys()) #it will just return a list but with dict_keys, which is a logical view of keys
tempkeys= dictvar.keys()
print(tempkeys)
dictvar["Roll No"] =101
print (tempkeys)'''
#Shadow copy and deep copy?

#=======================
#9th April 2025 Lecture
#=======================

'''dictvar= {"Name" : "Amit",
          "Program" : "MCA",
          "per" : 89.90
          #"City" : ["Pune", "Mumbai", "Delhi"]
          }
print(dictvar)
#dictvar.update ()
#pop with a valid key

popval= dictvar.pop("Name")
print(popval)
print(dictvar)'''

'''popval= dictvar.pop("Name")
print(popval)
print(dictvar)'''

'''topper= { 1: ["Amit", "MCA", 89.90,] , 3: "Rajesh", 5: "Ajay", 8: "Jadav"}
print(topper)
tlist= list(topper.keys())
tlist.sort()
print(topper[tlist[0]])''' #tlist[0] is the key for 1:

#popitem will start from the last element in the dictionary or list.
    #topper= { "name :"Amit", "program":"MCA","per": 89.90 }

#del dictvar #It will delete the who dictionary. 
#del dictvar["per"] #this will only delete the [per]
#dictvar.clear() #And this will clear the whole dictionary but we can still put data in the dictionary.
#dictvar["name" : "shubham"]
#print(dictvar)

