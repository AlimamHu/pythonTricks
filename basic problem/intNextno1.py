from typing import Counter


def pri_date_time_seprate():
    from datetime import date, datetime, timedelta
    from time import time

    print("DAY  : ",datetime.now().day)
    print("month : ",datetime.now().month)
    print("year : ",datetime.now().year)
    print("hour : ",datetime.now().hour)
    print('minute : ',datetime.now().minute)
    print('second : ',datetime.now().second)
    print('microsecond : ',datetime.now().microsecond)
    print('weekday : ',datetime.now().weekday())
    print('tommoro : ',datetime.now()+timedelta(1))
    print('yesterday : ',datetime.now()-timedelta(1))
    print(datetime.now().time())
    if datetime.now().time().hour<=12:
        print(datetime.now().time(),'AM')
    else:
        print(f'{datetime.now().time().hour-12}:{datetime.now().time().minute}:{datetime.now().time().second}','PM')

# in two no. find miximux no.
def max_2(x,y):
    if x>y:
        print(x)
    else:
        print(y)
# max_2(-11,1)
# print(max(-11,1))

#  interest (p*t*r)
def interest(p,t,r):
    return (p*t*r)/100
    pass
# print(interest(10000,5,5))

# convert in time into second

def hou_sec(x=str):
    value= [ int(i) for i in x.split(':')]
    t=[]
    for i,v in enumerate(value):
        if i==0:
            t.append(v*60*60)
        elif i==1:
            t.append(v*60)
        else:
            t.append(v)
    return sum(t)


    pass
# print('--> total second',hou_sec('4:10:6'),)

# t=input('enter you nos. : ').split(',')
# print(t)


# print(os.listdir()) 
# finding the in directory all extension 
def findAll_extension():
    import os
    for value in os.listdir():
        t=value.split('.')
        print(t[-1])
# findAll_extension()

# swap methods below 
# [65, 4, 34, 5, 4, 5645, 32]
# [32, 34, 5, 4, 5645, 65]
def swap(x):   # list last element & first element swap or replace
    first=x.pop(0)
    last=x.pop()
    x[0]=last
    x.append(first)
    return x

def swaplist(x):
    x[0],x[-1]=x[-1],x[0]
    return x
def swapListTwo(x,p1,p2):   # list two element position swap or replace

    x[p1],x[p2]=x[p2],x[p1]
    return x

# counting len of list
def find_length_list(x):
    count=0
    for i in x:
        count+=1
    return count
# print(find_length_list([3,2,3,23,5,34,35,35]))
print(len().__annotations__)