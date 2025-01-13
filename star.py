print('----------------- squre box star pattern -------------------')
num=5
for val in range(num):
    for vv in range(num):
        print('*',end=' ')
    print()
print('-----------left triangle pattern----------------')
#triangle pattern
num=5
for val in range(num):
    for vv in range(val+1):
        print('*',end=' ')
    print()
print('--------- right triangle pattern ----------')
#print right triangle pattern
num=5
for val in range(1,num+1):
    for vv in range(num-val):
        print(' ',end=' ')
    for nn in range(val):
        print('*',end=' ')
    print()
#print half triangle
print('---------------- triangle pattern-------------------------')
num=5
space=num-1
stars=1
for val in range(num):
    for val in range(space):
        print(' ',end=' ')
    for val in range(stars):
        print('*',end=' ')
    print()
    space-=1
    stars+=2
print('----------------diamond patter----------------')
num=11
space=num//2
stars=1
for val in range(num):
    for vv in range(space):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    if val<num//2:
        space-=1
        stars+=2
    else:
        space+=1
        stars-=2
print('---------------hellow patterns in squre pattern-------------------')
num=5
for val in range(num):
    for vv in range(num):
        if val==0 or vv==0 or val==num-1 or vv==num-1:
            print('* ',end=' ')
        else:
            print('  ',end=' ')
    print()


