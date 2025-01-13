num=5
for val in range(num,0,-1):
    for st in range(val):
        print('*',end=' ')
    print()
print('-------------------------')
num=5
for val in range(num):
    for sp in range(num-val-1):
        print(' ',end=' ')
    for st in range(val+1):
        print('*',end=' ')
    print()
print('----------------------------------')
num=5
for val in range(num,0,-1):
    for vv in range(num-val):
        print(' ',end=' ')
    for ss in range(val):
        print('*',end=' ')
    print()
print('-----------------------------------------------')
num=5
space=0
stars=num*2-1
for val in range(num):
    for vv in range(space):
        print(' ',end=' ')
    for nn in range(stars):
        print('*',end=' ')
    print()
    space+=1
    stars-=2
print('--------------------------------')
num=5
stars=1
for val in range(num):
    for vl in range(stars):
        print('*',end=' ')
    print()
    if val<num//2:
        stars+=1
    else:
        stars-=1
print('----------------------------------------')
num=5
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
        stars+=1
    else:
        space+=1
        stars-=1
    

        

    