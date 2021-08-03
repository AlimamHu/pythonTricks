def velocity(s:'in km',t:'in hour')->int:   # -> return, : take in km etc.
    return s/t
print(velocity(30,4))
print(velocity.__annotations__)     # know about function what return & take 
# print(velocity.__format__())

def he(*name:'str',):    # *name pass many arrgument
    for i in name:
        print('hello ',i,)
# he('ali','hussain','ali',)
he()
