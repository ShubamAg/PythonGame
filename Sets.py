 #25th March 2025 Lecture
 #======================
'''#sobj= {5,3,6,7,9,90,20,40} 
sobj={"amit", 6,"ajay", 8,"Rajesh", 7, "Omkar", 10}
#sobj= {9,8,7,6,2,4,5,1,0}
print("Set:" ,sobj )'''

'''sobj= {"amit", 101, "Amit", 101,89.90, "Pune"}
print("Set : ", sobj)
for val in sobj:
    print(val, end=" ")'''
    
'''sobj= {"amit"}
sobj.add(101)
sobj.add("Pune")
sobj.add("MCA")
print(sobj)'''

'''sobj= {"amit", 101 ,89.90, "Pune", "MCA"}
print("Before Set :",sobj)
#sobj.remove("amit") #if value is not present then it will give Keyerror.
#sobj.discard("ajay") #Even if the value is not present it will not give nay error
print("After Set :",sobj)'''
#=======================
#26th March 2025 Lecture
#=======================
'''sobj= {"amit", 101, "MCA", "Pune", 89.99, 101}
print("Set :" , sobj)
val= sobj.pop()
print("Set after pop :", sobj)
print("Value popped :", val)
del sobj
print("Set after del :", sobj) # AS we use delete operator on sobj the set will be deleted and it will give the NameError: name 'sobj' is not defined'''

set1= {1,2,3,4}
print ( "set 1 :", set1, "Len :", len(set1) )
set2= {"a", "b", "c", "d", 3,4}
print("set 2 :", set2 ,"len :", len(set2))
set1.update(set2)
print("Set 1 after update :", set1 , "len :" ,len(set1))


