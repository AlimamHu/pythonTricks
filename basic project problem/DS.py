# Bineary Search tree
# [3,43,3,64,75,76,8]


def index_find(l,n):
    for i,valu in enumerate(l):
        if valu==n:
            return i

    pass
# print(index_find([3,43,3,64,75,76,8],64))

# Recursive
def index_recusiv(l,n):
    m=0
    high=len(l)-1
    mid=high+m//2
    if l[mid]>n:
        m=mid
        if l[m]>=n:
            return m 
    else:
        high=mid
        if l[high]>n:
            return high
        elif l[high]==n:
            return high
        

    pass
def node():
    class Node:
        def __init__(self,data): 
            self.left=None  #root.left=3 
            self.right=None  #  root.right=55
            self.data=data   #  root= Node(4)

    root=Node(4)
    #              4
    # root.left  /   \ root.right
    #          None  None

    root.left=Node(3)
    root.right=Node(55)


    root.right.right=Node(44)
    '''          4
    root.left  /    \ root.right  
            3     55
            /   \   /  \
        none none*2  none  -> root.right.right=Node(44) 
    '''
    print(root.right.right.data)    
    # print(list(root))


#  finding values location in list

import time
def linear_search():
    l=[1,2,3,4,5,6,7,8,9,10]
    t=[]
    searching_index=0
    for i in range(10):
        start_ti=time.process_time()
        for i , v in enumerate(l):
            if v==1:
                searching_index=i
                break;
        ent_ti=time.process_time()
        t.append(ent_ti-start_ti)
    print(f'{sum(t)/len(t)} 10 time average')

l=[1,2,3,4,5,6,7,8,9,10]
s=3
for i in range(len(l)):
    high=l[-1] 
    low=l[0]
    mid=(high+low)//2
    if l[mid]==s:
        print(l[mid])    
        break;
    else:
        print('sorry')
        break