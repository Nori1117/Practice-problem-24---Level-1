#Given two positive integers. Write a python function to return the greatest common divisor of the given numbers.

#lex_auth_0127136213490565121191

def find_gcd(num1,num2):
    #start writing your code here
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(1, small + 1):
        if((num1 % i == 0) and (num2 % i == 0)):
            gcd = i 
    return gcd
    
    

num1=45
num2=9
print(find_gcd(num1,num2))
