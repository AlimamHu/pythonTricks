from typing import MappingView


l1=[1,2,3,4]
def square(a):   # in this function u adding only on no.
    return a**2
print(square(1))
print(square(2))
print(square(3))
print(square(4))

# print(square(l1))   # not pass list

# for i in l1:     # we use list single chractor by charctor & call to the function
#     print(square(i))   
# insted use below code

print(list(map(square,l1)))   # but in the map function we add list and function without adding for loop to iterate values
sq=map(square,l1)
for i in sq:
    print(i,'-',end=' ')

for i in sq:
    print(i,'-',end=' ')
    # you see above code map is object which are iterable & one time but you have list you call many time 
print('\n',list(map(len,['ab','abc','abcd'])))