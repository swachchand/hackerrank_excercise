'''
Given two int values, return their sum. 
Unless the two values are the same, 
then return double their sum.

sum_double(1, 2) -- 3
sum_double(3, 2)-- 5
sum_double(2, 2) -- 8

'''

def sum_double(a, b):    
    if a == b:
        c =  a + b
        c = c * 2
    else:
        c = a+b
            
    return c

in1 = int(input('Enter number 1: '))
in2 = int(input('Enter number 2: '))

print(sum_double(in1, in2))
  
  