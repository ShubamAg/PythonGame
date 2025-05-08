#=======================
#15th April 2025 Lecture
#=======================

#Same class function overloading. Compile time & Run time. Compile time function would be freez so it will be executed in run time. Fucntion name should be same.
#Has a relationship & Is a kind of relationship.(*) A C or C++ logic which has to be converted to python logic.
'''class test:
    def set (self, temp):
        self.num=temp

    def show(self):
            print("Num", self.num)

    def printfun(temp, x):
         print("x =", x)

tobj= test()
tobj.set(100) #explicit assignment
tobj.show()'''
#print(100)
#self.num, or any systax like this will make the later variable after '.' data member of the class. 
#But if we have only one in the function def(temp,x), x will never become a data member in the class and it will have no use beside in that function.


#=======================
#16th April 2025 Lecture
#=======================


'''class Account:
    bankname= "Axis"
    def __init__(self, name, accno,bal):
        self.aname=name
        self.accno=accno
        self.bal= bal
        
        def show(self):
            print("Bankname :", self.bankname)
            print("Name :", self.aname)
            print("Acc No :", self.accno)
            print("Balance :", self.bal)
            '''
#When the variable and the datatype of value is same then super.variable helps. It calls parent variable. 

#=======================
#29th April 2025 Lecture
#=======================

#the first 20 tokens in the file are for user's data and information 

#fp=open#(textfile we want to open)

#=======================
#30th April 2025 Lecture
#=======================
'''fout= open("C://Python//output.txt", "wt")
print("Name of the file :", fout.name)
print("Closed or not :", fout.closed)
print("Opening mode :", fout.mode)
fout.write("10000")
fout.close()'''

#copying the file

#combining two logics in one code in file handling 

#=======================
#2nd May 2025 Lecture
#=======================
