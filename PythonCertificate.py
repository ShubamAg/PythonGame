#Python was made by Guido van Rossum in 1991
#Identifier: In python, Variables,functions,classes,modules and objects are identified using identifier. They are case sensitive. For Example: weight=10
#Keywords: They are reserved words in python. For example: if, else, elif,for,where,break, continue
'''num=65
print(num,type(num))
num="A"
print(num, type(num))'''
#================================
'''a="infy"
b=20.127
c=10
print(a,b,c) #Print the value
print(a,b,c,sep=":") #Print the value with ':' seperating them
print(a,b,c,end=" ") # Print the values 2x and seperate them by  space 
print(a,b,c)
print("b=%0.2f" %b) #Give the value as double digit after decimal i.e. 20.13
print("c=%8d" %c)  #Print the value with 8 reserved space before. Right Aligned
print("c=%-8d" %c) #Print the value and reserved 8 space to the right. Left Aligned'''
#================================
'''num1 = "12" Type casting
num2= 28
result= int(num1)+(num2)
print(result)'''
#================================
'''num1=5
num2=6
print(num1%num2)''' #output 1
#================================
'''def num_miltiple(num):
    if(num%3==0):
        print("Zip")
    if(num%5==0):
        print("Zap")
    if(num%3 and num%5==0):
        print("Zoom")
    else:
        print("Invalid")
num=int(input("Enter the number:"))'''
#================================
'''for number in range (5,0,-1):
    print("The current number is", number)'''
#================================
'''
Write a Python program to check whether the given year is leap year or not.

Write a Python program to find and display the maximum of three given numbers.

Write a Python program to check the given number is prime number or not.

Write a Python program to print first n Fibonacci numbers.

An organization has decided to provide salary hike to its employees based on their job level. Employees can be in job levels 3 , 4 or 5. Hike percentage based on job levels are given below:

Job level

Hike Percentage (applicable on current salary)

3 15

4 7

5 5

In case of invalid job level, consider hike percentage to be 0.

Given the current salary and job level, write a Python program to find and display the new salary of an employee.
'''
#================================
'''
#Creating a string
pancard_number="AABGT6715H"
#Length of the string
print("Length of the PAN card number:", len(pancard_number))
#Concatenating two strings
name1 ="PAN "
name2="card"
name=name1+name2
print(name)
print("Iterating the string using range()")
for index in range(0,len(pancard_number)):
    print(pancard_number[index])
    
print("Iterating the string using keyword in")
for value in pancard_number:
    print(value)
print("Searching for a character in string")
if "Z" in pancard_number:
    print("Character present")
else:
    print("Character is not present")
#Slicing a string
print("The numbers in the PAN card number:", pancard_number[5:9])
print("Last but one 3 characters in the PAN card:",pancard_number[-4:-1])
pancard_number[2]="A" #This line will result in an error, i.e., string is immutable
print(pancard_number)
'''
'''my_list= [0]*5
print(my_list)
for index in range(1,5):
	my_list[index]=(index-1)*10
print(my_list)'''

'''pancard_list=["AABGT6715H", "UFFAC4352T", "IFSBD9163K", "JOOEC1225H","RWXAFE187B"]
print(pancard_list[3][6], end=" ")
print(pancard_list[4][3:])'''

'''message="welcome to Mysore"
word=message[-7:]
if(word=="Mysore"):
    print("got it")
else:
    message=message[3:14]
    print(message)'''
#================================
'''
boarding_call="Good Evening, this is the final call to AL passengers for the flight AL 466 which is planned to take off at 8.40A.M."
if(boarding_call.startswith("Good Evening")):
    print(boarding_call.replace("Good Evening","Good Morning"))
if(boarding_call.find("AL"))>=0:
    print("Welcome to Air Lines.")
if(boarding_call.endswith("A.M.")):
    print("Passengers are requested to have their breakfast.")
a=boarding_call.split(" ")
for i in a:
    if(i.isdigit()):
        print("Flight Number is specified to the passengers.")
print("Total number of times flight service name is specified in the boarding call:",boarding_call.count("AL"))
message="Thank you all..Have a nice journey!"
print(message.upper())
print(message.lower())
'''

'''
crew_details={
    "Pilot":"Kumar",
    "Co-pilot":"Raghav",
    "Head-Strewardess":"Malini",
    "Stewardess":"Mala"
}
print("Before update:")
print("Co-pilot:",crew_details.get("Co-pilot"))
crew_details.update({"Flight Attendant":"Jane", "Co-pilot":"Henry"})
print("\nAfter update:")
print("Co-pilot:",crew_details.get("Co-pilot"))
print("Flight Attendant:",crew_details["Flight Attendant"])
'''

'''song="JINGLE Bells jingle Bells Jingle All The Way"
song.upper()
song_words=song.split()
count=0
for word in song_words:
    if(word.startswith("jingle")):
        count=count+1
print(count)'''

'''import math
num_list=[100.5,30.465,-1.22,20.15]
num_list.insert(1, -100.5)
num_list.pop(0)
num_list.sort()
print(math.ceil(math.fabs(num_list[0])))'''

'''sample_dict={'a':1,'b':2}
sample_dict.update({'a':2 , 'b':5, 'c':10 })
sample_dict.update({'b':6, 'c':11 }) #if the element is not mentioned in the update list ie 'a' here. It will not be updated but a will be in list still shithead!

print(sample_dict)
print(sample_dict.get('a'),sample_dict.get('b'),sample_dict.get('c'))'''
#================================

#Line by line.//Python provides readline() function to read the single line from the file at a time. When the end of the file reached it returns an empty string.
'''fhr=open("data.txt","r")
line1=fhr.readline()    
print(line1,end="")
line2=fhr.readline()    
print(line2,end="")
line3=fhr.readline()    
print(line3,end="")'''

#Whole file.//Python provides readlines() function to read entire content of file into a variable where each line will present as an element of the list.
'''fhr=open("data.txt","r")
list_var=fhr.readlines()
for line in list_var:
    print(line,end="") 
fhr.close()'''

#after 10 words the file reading will stop
'''fhr=open("data.txt","r")
data =fhr.read(10)
print(data)
fhr.close()'''

#Writing into file
'''
fhr=open("data.txt","r")
data =fhr.read()
print("Before writing:")
print(data)
fhr.close()
fhw=open("data.txt","w")
num=fhw.write("this new first line written\n")
num1=fhw.write("this new second line written\n")
print("num:",num)
print("num1:",num1)
fhw.close()
fhr=open("data.txt","r")
data =fhr.read()
print("After writing:")
print(data)
fhr.close()
'''#output====
'''
Before writing:
this is first line
you are reading the second line
now you are dealing with third line
num: 28
num1: 29
After writing:
this new first line written
this new second line written
'''
#Another Example of Writing into file
'''
fhr=open("data.txt","r")
data =fhr.read()
print("Before writing:")
print(data)
fhr.close()
fhw=open("data.txt","a")
num=fhw.write("this new first line written\n")
num1=fhw.write("this new second line written\n")
print("num:",num)
print("num1:",num1)
fhw.close()
fhr=open("data.txt","r")
data =fhr.read()
print("After writing:")
print(data)
fhr.close()
'''

#Getting current position of the file object pointer
'''
fhr=open("data.txt","r")
cur_pos=fhr.tell()
print(cur_pos)
data =fhr.readline()
print(data)
cur_pos=fhr.tell()
print(cur_pos)
data =fhr.readline()
print(data)
fhr.close()
'''

#Navigating the file object pointer
'''
fhr=open("data.txt","rb+")
print(fhr.tell())
fhr.seek(12) #navigates to 12th position from beginning of the file
print(fhr.tell())
fhr.seek(3,1) #navigates to 3rd position from current position of the file object position
print(fhr.tell())
fhr.seek(-3,2)#navigates to 3rd position from end of the file in backward direction
print(fhr.tell())
fhr.close()
'''

#File object attributes
'''
fhr=open("data.txt","rb+")
print("file name:",fhr.name)
print("access mode:",fhr.mode)
print("closed?",fhr.closed)
fhr.close()
print("after closing the file closed?",fhr.closed)
'''
'''def division(a,b):
    try:
        return int(a)/b
    except TypeError:
        print("Type error")
    except ValueError:
        print("Value error")
    finally:
        print("Finally")
    print("Done")
division('A',10)'''
'''def find_sum(a,b):
    try:
        print(a+c)
    except NameError:
        print("Function name error")
    finally:
        print("Sum finally")
try:
    find_sum(12,13)
except NameError:
    print("Invocation name error")
finally:
    print("Invocation finally")'''
