print('--------print the below  all number in  using recursion-----------------')
def sample(num,val=2):
    if num<1:
        return 
    if val==num//2+1:
        return 'prime number'
    if num%val==0:
        return 'not prime number'
    sample(num,val+1)
num=2
print(sample(num))
print('-------composite number---------')
def composite(num,val=2):
    if num<3:
        return 'not composite number'
    if val==num//2+1:
        return 'not composite number'
    if num%val==0:
        return 'composite number'
    sample(num,val+1)
num=4
print(composite(num))
print('---------armstrong number or not--------')
def armstrong(num,pos):
    if num==0:
        return 0
    return (num%10)**pos+armstrong(num//10,pos) 
num=153
pos=len(str(num))
if num==armstrong(num,pos):
    print('armstrong number')
else:
    print('not armstrong number')
print('-----------disarm number----------')
num=136
def disarmnumber(num,pos):
    if num==0:
        return 0
    return (num%10)**pos+disarmnumber(num//10,pos-1)
pos=len(str(num))
if num==disarmnumber(num,pos):
    print('diarm number')
else:
    print('not disarm number')
print('---------strong number------------')

def strong(num):
    if num==0 or num==1:
        return 1
    return num*strong(num-1)
def number(num):
    if num==0:
        return 0
    return strong(num%10)+number(num//10)
num=145
if num==number(num):
    print('strong number')
else:
    print('not arm strong number')
print('-------reverse a number---------')
def reverse(num,pos):
    if num==0:
        return 0
    return (num%10)*pos+reverse(num//10,pos//10)
num=121
pos=10**(len(str(num))-1)
if num==reverse(num,pos):
    print('palindrome')
else:
    print('not palindrome')
print('----------- convert the integer to binary----------')
def binary(num,pos=1):
    if num==0:
        return 0
    return (num%2)*pos+binary(num//2,pos*10)
num=13
print(binary(num))
print('--------------binary to integer--------')
def integer(num,pos=0):
    if num==0:
        return 0
    return ((num%10)*2**pos)+integer(num//10,pos+1)
num=1101
print(integer(num))
print('------------special number--------')
def special(num,val=1):
    if val==num//2+1:
        return 0
    if num%val==0:
        return val+special(num,val+1)
    return special(num,val+1)
num=6
if num==special(num):
    print('special number')
else:
    print('not psecisl number')









