print('--------reverse string-----------')
def reverse(a):
    return a[::-1]
a='suresh'
print(reverse(a))
print('------check the given number is prime number or not----------')
def prime(num):
    if num>1:
        for val in range(2,num//2+1):
            if num%val==0:
                return 'not prime number'
        return 'prime number'
    return 'not prime number'
num=2
print(prime(num))
print('---------factorial of a number----------')
def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)
num=4
print(factorial(num))
print('----------to check the given string is palindrome or not ------------')
def palindrome(s):
    b=s[::-1]
    if s==b:
        return 'palindrome'
    return 'not palindrome'
s='vvnnvv'
print(palindrome(s))
print('-------fibonacci---------')
def fibonacci():
    l=[]
    a,b=0,1
    for val in range(5):
        l.append(a)
        a,b=b,a+b
    print(l)
print(fibonacci())
print('---------find out the largest element-----------')
def sample(num):
    print(max(num))
num=[1,2,3,4,5,80,6,99]
print(sample(num))
print('---------bubble sort----------')
l=[2,3,8,6,5,4,1,9]
def sample(l):
    for val in range(len(l)-1,0,-1):
        for vv in range(val):
            if l[vv]>l[vv+1]:
                l[vv],l[vv+1]=l[vv+1],l[vv]
    print(l)
print(sample(l))
print('---------anagrames-------------')
def anagrames(str1,str2):
    return sorted(str1)==sorted(str2)
str1='listen'
str2='silent'
print(anagrames(str1,str2))
print('------------------------------')
a='listen'
b='silent'
str1=sorted(a)
str2=sorted(b)
if str1==str2:
    print('anagrames')
else:
    print('not anagrames')
print('-------------------------------')
from itertools import permutations
def permutation(a):
    prm=permutations(a)
    print((prm))
a='abc'
print(permutation(a))