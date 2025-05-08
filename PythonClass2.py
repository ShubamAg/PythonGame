#print ("A is Greater") if a>b>c else print("B is greater") if b>c else print("C is greater") [Print this with the values of a=100,b=200,c=300]
'''
a=100
b=200
c=150    
print ("A is Greater") if a>b>c else print("B is greater") if b>c else print("C is greater") 
'''
# use CTRL+c to get out of running program (Kill the program)

                                                                #loop in python
#for and while are called entry controled loop where as do_while is a exit control loop. In for loop iterations are known and in while they are not. 
'''i=1
while i<=10:
    print(i)
    i+=1
    
    '''
'''i=2
while i < 50000 :
   print(i)
   i*=i   ''' 

# From here the code is running perfectly and printing A-Z and then Z-A

'''i= ord('A')        
while i<=ord('Z'):
 print (chr(i))
i+=1'''

'''i= ord('Z')
while i>=ord('A'):
 print (chr(i))
i-= 1'''
#ord is used for getting the value of characters A=65 and Z=90, chr is used for converting the value to character in loops so we get alphabets instead of int values.
#without using chr in print we would get output of 65-90 and then 90-65. But it will print first A-Z and then Z-A.






        #18th March 2025 Lecture
        #=======================
'''alist=["amit", 101, "MCA", "Pune", 101]
print("Before pop(4)", alist)
alist.pop(4)
print("After pop(4)", alist)'''
#Here the last element would be popped out of the list or removed from the list

'''alist=["amit", 101, "MCA", "Pune", 101]
alist.pop(5)'''
#Here since the index is out of the list, it will give us error 
#We can only pop a value form the list through indexs hence alist.pop(101) will also give us an error. And also alist.pop(amit) wil give us TypeError in output
#if we forget to give the parameter in pop then it will pop the last element from the list

'''
In Remove we remove the element by occurance
For example there's a list

["amit", "is", "the", "topper", "in", "his", "class", "is"]

1)Then using remove we can remove the elemetns in this list for example "is". Try removing an elemnt which is not in the list?
2)pop will be pop the index element from the list for example list.pop(2)
3)del will delete the 
'''
'''alist=["amit", 101, "MCA", "Pune", 101]
print(alist)
#del alist[-1]
#del alist[4]
#del alist[2:]
#del alist[:3]
#del alist[2:-1]
del alist
print("List elements:",alist)''' #Here the alist will be deleted and next step printing will show an error "NameError"
#del is pure index based as well just like pop

#(*)Lets say we have tewo lists with words. If there's a word  found in the main list show the output that the word is found and then delete the word from 1st list.
#(*)For example lets say that we found a word Shubham in both list so output will be how many times Shubham occured in the list and then delete the word Shubham from the list.

'''alist=["amit", 101, "MCA", "Pune", 101]
print(alist)
alist.clear()
print("list elements after clear", alist)'''
#Here the whole list will be cleared or empty

#(*) Read the file content form a file and append the elements of the file element to digit and word 2 different lists from the main file

'''alist=[25,65,84,2,69,95,87]
#alist.sort()
alist.sort(reverse=True)
#This will sort the list but in decending order. MEaning the largest number will be first and samllest number will be in last
print(alist)
#sort will sort the list
alist=["a", "c", "z", "b"]
alist.sort()
print(alist)
#there should only be numeric values in the list or alphabetic value. Otherwise it will show the error
'''
            #=======================
            #24th March 2025 Lecture
            #=======================
'''tvar= (101, "ajay", "MCA", "Pune", 89.90)
for val in tvar:
    print(val, end= " ")
for i in range(0, len(tvar)):
    print(tvar[i])
name="Amit"
tvar[1]=name
print(tvar)'''
#Here the program will give an error. TypeError: 'tuple' object does not support item assignment. Means we can not override the touple.
'''name= tvar[1]
print(name)'''
#refrences can be modified in the touple. So lets see it as an example
'''tvar1=(101, "ajay", "MIT-WPU")
tvar2= (101, 89.90)
tvar1= tvar1+tvar2
print(tvar1)'''
#print(tvar1+tvar2)
#Here the tvar1 and tvar2 and two refrences or "objects" which hold the values in touple. And so we are not overriding or updating the values in the touple but we are updating the refrence itself.
'''tvar= (101, "ajay", "MIT-WPU", "ajay", 101, "pune")
for var in tvar:
    print(var, " ", tvar.count(var))'''
#In this code there's an logical error. In the output the elements who already have been visted are being count. 
#==============================================================================================================
#(*IMP*)A set of values are there. So print the indexes of the values that are repeating.
#   For example tvar= (101, "ajay", "MIT-WPU", "ajay", 101, "pune") , so write the values that are repeating, how many times and there indexes.
#==============================================================================================================
'''tvar= (200, 99, 89, 56, 333, 41, 30)
print("Touple Items:" , tvar)
alist= list( tvar )
print("list Items:", alist)
alist.sort(reverse=True)
print("Sorted List:", alist)
tvar= tuple(alist)
print("Tuple is sorted:", tvar)'''
#==============================================================================================================