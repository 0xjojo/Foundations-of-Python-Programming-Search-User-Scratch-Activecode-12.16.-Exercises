#Write a function named num_test that takes a number as input. 
#If the number is greater than 10, the function should return “Greater than 10.”
# If the number is less than 10, the function should return “Less than 10.” 
#If the number is equal to 10, the function should return “Equal to 10.”
def num_test (x):
    y = "Greater than 10."
    n = "Less than 10."
    r = "Equal to 10."
    if (x > 10 ):
        return y
    if (x == 10):
        return r 
    else :
        return n


#Write a function that will return the number of digits in an integer.
def numDigits(n):
    string = str (n)
    length = len (string)
    return length 
    # your code here
	
#Write a function that reverses its string argument.
def reverse(astring):
    reversed = ''
    n = len (astring) - 1 #to avoide the problem of index
    for r in astring :
        reversed = reversed + astring[n]
        n = n-1
    return reversed
    
    # your code here

	
#Write a function that mirrors its string argument, generating a string containing the original string and the string backwards.
def mirror(mystr):
    copy = mystr
    mirror = ''
    n = len (mystr) - 1
    for r in mystr :
        mirror = mirror + mystr[n]
        n = n-1
    collect = copy + mirror
    return collect 
    # your code here

	
#Write a function that removes all occurrences of a given letter from a string.
def remove_letter(theLetter, theString):
    #n = len(theString) - 1
    n = 0
    without = ''
    
    for r in theString :
        if r == theLetter :
            n = n + 1
            continue 
        else :
            without = without + theString[n]
            n = n + 1
    return without
    # your code here

	
	
#Write a function replace(s, old, new) that replaces all occurences of old with new in a string s:
def replace(s, old, new):
    y = ''
    s.split()
    for r in s :
        if r == old :
            r = new
        y = y+r
    return y
    # your code here


#Write a Python function that will take a the list of 100 random integers between 0 and 1000 
#and return the maximum value. (Note: there is a builtin function named max but pretend you cannot use it.)
def maximum (lst) :
    ref = 0 
    for x in lst :
        if (x > ref ):
            ref = x
    return ref
	
#Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs. For example, 
#sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:
def sum_of_squares(xs):
    sum = 0
    for i in xs :
        i = i*i
        sum = sum + i
    return sum 
    # your code here

#Write a function to count how many odd numbers are in a list.
def countOdd(lst):
    count = 0
    for i in lst :
        remainder = i % 2
        if remainder == 1 :
            count = count + 1
        else : 
            continue 
    return count
    # your code here

#Sum up all the even numbers in a list.
import random

def sumEven(lst):
    sumEv  = 0 
    for n in lst :
        r = n % 2
        if (r == 0):
            sumEv  = sumEv  + n 
        else :
            continue
            
    return sumEv 
    # your code here

#Sum up all the negative numbers in a list.
def sumNegatives(lst):
    ref = 0
    sumNeg = 0
    for r in lst :
        if r < 0 :
            sumNeg = sumNeg + r
        else :
            continue 
    return sumNeg
    # your code here

#Write a function findHypot. The function will be given the length of two sides
# of a right-angled triangle and it should return the length of the hypotenuse. 
#(Hint: x ** 0.5 will return the square root, or use sqrt from the math module)
def findHypot(a,b):
    Hypot = (a**2+b**2)**0.5
    return Hypot
    # your code here


#Write a function called is_even(n) that takes an integer as an argument and returns 
#True if the argument is an even number and False if it is odd.
def is_even(n):
    r = n % 2
    if r == 0:
        return True
    if r == 1:
        return False
    #your code here

#Now write the function is_odd(n) that returns True when n is odd and False otherwise.
def is_odd(n):
    r = n % 2
    if r == 1:
        return True
    else :
        return False 
    # your code here


#Write a function is_rightangled which, given the length of three sides of a triangle,
# will determine whether the triangle is right-angled. Assume that the third argument
# to the function is always the longest side. It will return True#
# if the triangle is right-angled, or False otherwise.
#Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test 
#floating point numbers for equality. If a good programmer wants to know whether x is equal or close enough to y, 
#they would probably code it up as
def is_rightangled(a, b, c):
    #if the triangle is sqrt(a^2 + b^2)=c
    r = (a**2+b**2)**0.5
    if (c == r) :
        return True
    elif ((c-r) < 0.001):
        return True
    elif ((r-c) < 0.001):
        return True
        
    else :
        return False
    # your code here