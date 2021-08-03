# 12-july-2021
# integer next number.
'''
EXAMPLE :-
input: intNextno(3) 
output:4 
'''
def intNextno(x):
    return x+1


# minutes convert into second
'''
EXAMPLE :-
input: minCONsec(4) 
output: 240
'''
def minCONsec(x):
    return x*60


# Boolean flags convert into string
'''
EXAMPLE :-
input:  bolStr(True)
output: 'True'
'''
def bolStr(x):
    if type(x)==bool:
        pass
    else:
        return 'only boolen values'
    return str(x)

# return rectangle parameter formula ->  2(length+width)
'''
EXAMPLE:-
>>>  recPara(4,6)
20
'''
def recPara(l,w):
    return 2*(l+w)

# 13-july-2021
# sum of interior angles of a polygon (n-2)/180 , n -> n-side of polygon
'''
Example:-
>>> angle_polygon(3)
180
'''
def angle_polygon(n):
    return (n-2)*180

# no. of digonal of polygon (n(n-3))/2
'''
Example:-
>>> digPoly(8)
20               
'''
def digPoly(n):
    return (n*(n-3))/2


#  number on power calculator basicaly
'''
Example:-
>>> noPOcal(2,6)
36
'''
def noPOcal(n,p): 
    return n**p

# default mood
'''
Example:-
>>>def_mood('happy')
Today I'm feel happy
'''
def def_mood(m='neutral'):
    return f'Today I\'m feel {m}'

# 14-july-2021
#  basic calculation
'''
Example:-
>>>square_(2,5)     # bind 2*2*2*2*2
32
'''
def square_(x,p):
    t=1 
    for i in range(p):
        t=t*x
    return t

# Return Factorial
'''
Example:-
>>>Factorial(5)   # bind process 1*2*3*4*5
120
'''
def Factorial(r):
    t=1
    for i in range(1,r+1):
       t=t*i 
    return t

# date of birth to count age
'''
Example:-
>>>birth_ageg(2002,11,2)
19
'''
def birth_ageg(y,m,d):
    from datetime import datetime
    return datetime.now().year-y


                    
# multiply inside the list  all element
'''
Example:-
>>>list_inside_multiply([3,4,5,])    # numpy.prod([3,4,5])
60
'''
def list_inside_multiply(l):
    t=1
    for i in l:
        t=t*i
    return t
 
#print ASCII Value of a character
def all_ASCII():
    return [chr(i) for i in range(0,400)] # 0 to 1,1141,111 ASCII character


#find the Armstrong number
'''
Example:- len of no. like 120, 1*1*1+2*2*2+0*0*0=9
153=1**3+ 5**3 +3**3=153
>>>Armstrong_no(120)
120 is not Armstrong Number
'''
def Armstrong_no(n):

    p=0
    lenght =len(str(n))
    for i in str(n):
        p=p+square_(int(i),lenght)
    if n== p:
        return (f'{n} is Armstrong number')
    else:
        return (f'{n} is not Armstrong Number')

# Finding Prime Number is no Prime or NOT 
'''Example:-
>>>prime_no(44)
[1, 2, 4, 11, 22, 44] sorry this is not Prime number
'''
def prime_no(x):
    t=[]
    for i in range(1,x+1):
        if x%i==0:
            t.append(i)
    if len(t)==2:
        return f'{t} yes this Prime Number'
    else:
        return f'{t} sorry this is not Prime number'


# Enter radio from user & get area of circle
# print(radios_cir(1.1))
def radios_cir(r):
    import math
    return math.pi*r**2

#  reverse user first name & last name
'''Example:-
>>>rever_fir_las('gopal','sing')
gopal sing into revearse form lapog gnis
'''
def rever_fir_las(f,l):
    return f'{f} {l} into revearse form {f[::-1]} {l[::-1]}'

# list first & last color display
'''Example:-
>>>list_f_l(['black','white','red','blue'])
['black','blue']
'''
def list_f_l(l):
    return l[0],l[-1]

# find second maximum score, which is called runner-up score.
'''Example:-
>>>second_max_l([3,3,2,33,43,4,5,43])
Your maximum no. 43, 33 runner-up score
'''
def second_max_l(l):
    l.sort()
    set_sorted_values=set(l)
    list_set_sorted_values=list(set_sorted_values)
    list_set_sorted_values.sort()
    # return list_set_sorted_values[-1]
    return f'Your maximum no. {list_set_sorted_values[-1]}, {list_set_sorted_values[-2]} runner-up score' 

'''
print below line 
Example:-
>>>no_patern()
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
def no_patern():
    for i in range(1,6):
        for t in range(1,i+1):
            print(t,end=' ')    # print(i,end=' ') & print(1+i-t,end=' ') so get diffrent pattern
        print(end='\n')

# find the maximum values in list
'''Example:-
>>>max_no([2,3,243,238,2])
243
'''

def max_no(l):
    m=0
    for i in l:   # no iteration = o(n)
        if i>=m:
            m=i
    return m
'''
O(1) no iteration
O(n)  iteration use 
O(n**2)  two for loops stement  use 
'''
# values search have True & False
def values_search_O_1(l):  # O(1)  --> only data one use    
    values=43 in l
    return values

# print(values_search_O_1([2,3,243,238,2,3,2,43,453,53,4]))
def values_search_O_n(l,search_values):    # O(n) --> no data in iteration
    for i in l:
        if i==search_values:
            return True
        else:
            return False

# print(values_search_O_n([2,3,243,238,2,3,2,43,453,53,4],431))

def two_list_print(l1,l2):
    for i,z in zip(l1,l2[::-1]):
        print(i,z,end='\n')
# two_list_print([10, 20, 30, 40],[100, 200, 300, 400])

def pass_con_break():
    '''
    continuous:- leave remaining code & next loop
    break :- loop break
    pass :- just pass remaing code  '''
    print('^^^^pass^^^^^')
    for i in range(5):
        if i==3:
            pass    # just pass remaining code
        print(i)
    print('-----continue-----')
    for i in range(5):
        if i==3:
            continue;   # call next iteration
        print(i)
    print('*****break****')
    for i in range(5):
        if i==3:
            break;    # stop iteration
        print(i)
 # if user not enter name that give suggestion (please enter name) 
def enter_print(): 
    n=input('enter : ')
    if n:    # not enter any values condition not run        (True)
        print(n)
    else:
        print('please enter name')

# in list remove blank values
'''
>>>list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
>>>blank_remove(list1)
['Mike', 'Emma', 'Kelly', 'Brad']
'''
def blank_remove(l):
    t=[]
    for i in l:
        if i:
            t.append(i)
    return t 

    