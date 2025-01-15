l=[1,2,3,4,5,6,7,8,9,55,66]
lower=0
high=len(l)-1
user=55
while lower<=high and l[lower]<=user<=l[high]:
    mid=int(lower+((high-lower)/(l[high]-l[lower]))*(user-l[lower]))
    if l[mid]<user:
        lower=mid+1
    elif l[mid]>user:
        high=mid-1
    elif l[mid]==user:
        print(mid)
        break
else:
    print(-1)
print('-------------bubble sort----------------')
l=[1,2,82,95,5,8,45,85]
for val in range(len(l)-1,0,-1):
    for vv in range(val):
        if l[vv]>l[vv+1]:
            l[vv],l[vv+1]=l[vv+1],l[vv]
print(l)
print('------selection sort-------------')
l=[1,5,2,6,3,8]
for ind1 in range(len(l)):
    li=ind1
    for ind2 in range(ind1+1,len(l)):
        if l[li]>l[ind2]:
            li=ind2
    l[ind1],l[li]=l[li],l[ind1]
print(l)
print('-------------quick sort------------')
l=[1,5,3,4,10,9,8,7,2]
def sample(l):
    if len(l)<1:
        return l
    pivot=l[0]
    left=[ele for ele in l[1:] if ele<pivot]
    right=[ele for ele in l[1:] if ele>=pivot]
    return sample(left)+[pivot]+sample(right)
l=[1,5,3,4,10,9,8,7,2]
print(sample(l))
print("-----------merge sort-----------------")
l=[5,6,7,1,2,3]
left=l[:len(l)//2]
right=l[len(l)//2:]
mind=0
lind=0
rind=0
while lind<len(left) and rind<len(right):
    if left[lind]<right[rind]:
        l[mind]=left[lind]
        lind+=1
    else:
        l[mind]=right[rind]
        rind+=1
    mind+=1
while lind<len(left):
    l[mind]=left[lind]
    lind+=1
    mind+=1
while rind<len(right):
    l[mind]=right[rind]
    rind+=1
    mind+=1
print(l)
print('---------------------merge sort --------------------')
def half(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        half(left),half(right)
        merge(l,left,right)
def merge(l,left,right):
    lind=0
    mind=0
    rind=0
    while lind<len(left) and rind<len(right):
        if left[lind]<right[rind]:
            l[mind]=left[lind]
            lind+=1
        else:
            l[mind]=right[rind]
            rind+=1
        mind+=1
    while lind<len(left):
        l[mind]=left[lind]
        lind+=1
        mind+=1
    while rind<len(right):
        l[mind]=right[rind]
        rind+=1
        mind+=1
print(l)
l=[5,6,7,1,2,3]
print(half(l))



