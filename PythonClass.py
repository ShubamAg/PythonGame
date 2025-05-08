                                                                                        #Match statement(Case) 
'''def convet_number(binary_str, decimal_str, octal_str, hexadecimal_str,n):
    
    match n:
        case 1:
            def convert_binary(binary_str):
                decimal = int(binary_str,2)
                octal = oct(decimal)
                hexadecimal = hex(decimal)
                binary_input = input("Enter the Binary Number:")
              
                decimal,octal,hexadecimal = convert_binary(binary_input)
                 print("Decimal" , decimal)
                 print("Octal" , octal)
                 print("Hexadecimal" , hexadecimal)
                
                
        case 2:
            def convert_decimal(decimal_str):
                binary = int(decimal_str)
                
        case 3:
            def convert_octal(octal_str):
                binary = int(octal_str)
                
        case 4:
            def convert_hexadecimal( hexadecimal_str):
                binary = int(hexadecimal_str) '''
                
                 
#There are many mistakes in the code including incorrect funtion prameters, function definition and variable assignment, missing return statement,incorrect binary conversion in other cases and some spelling mistakes too. 
#LEARN IT YOU FUCKING RETARD!!


'''def convert_binary(binary_str):
    
    decimal = int(binary_str, 2)
    octal = oct(decimal)
    hexadecimal = hex(decimal)
    return decimal, octal, hexadecimal

def convert_decimal(decimal_str):
   
    decimal = int(decimal_str)
    binary = bin(decimal)
    octal = oct(decimal)
    hexadecimal = hex(decimal)
    return binary, octal, hexadecimal

def convert_octal(octal_str):
  
    decimal = int(octal_str, 8)
    binary = bin(decimal)
    hexadecimal = hex(decimal)
    return binary, decimal, hexadecimal

def convert_hexadecimal(hexadecimal_str):
  
    decimal = int(hexadecimal_str, 16)
    binary = bin(decimal)
    octal = oct(decimal)
    return binary, decimal, octal

def convert_number(n):
    match n:
        case 1:
            binary_input = input("Enter the Binary Number: ")
            decimal, octal, hexadecimal = convert_binary(binary_input)
            print("Decimal:", decimal)
            print("Octal:", octal)
            print("Hexadecimal:", hexadecimal)

        case 2:
            decimal_input = input("Enter the Decimal Number: ")
            binary, octal, hexadecimal = convert_decimal(decimal_input)
            print("Binary:", binary)
            print("Octal:", octal)
            print("Hexadecimal:", hexadecimal)

        case 3:
            octal_input = input("Enter the Octal Number: ")
            binary, decimal, hexadecimal = convert_octal(octal_input)
            print("Binary:", binary)
            print("Decimal:", decimal)
            print("Hexadecimal:", hexadecimal)

        case 4:
            hexadecimal_input = input("Enter the Hexadecimal Number: ")
            binary, decimal, octal = convert_hexadecimal(hexadecimal_input)
            print("Binary:", binary)
            print("Decimal:", decimal)
            print("Octal:", octal)

        case _:
            print("Invalid choice! Please enter a valid number.")

# Ask user for input type
try:
    n = int(input("Choose Conversion Type:\n1. Binary to Decimal, Octal, Hex\n2. Decimal to Binary, Octal, Hex\n3. Octal to Binary, Decimal, Hex\n4. Hexadecimal to Binary, Decimal, Octal\nEnter your choice (1-4): "))
    convert_number(n)
except ValueError:
    print("Invalid input! Please enter a  valid number.")
'''
#Here after running the code the user would be asked for input and then based on the number inputed we will get the output.

