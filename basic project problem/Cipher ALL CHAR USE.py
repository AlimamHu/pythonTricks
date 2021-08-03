# encrept function mean -> text convert into cipher
def encrept_function(data,shift):
    '''
   What: normal text convert into encrepty text 
   EXAMPLE:-
   input : print(encrept_function('song is buityfull',3)) 
   output: vrqj#lv#exlw|ixoo
    '''
    reasult=''  
    for i in data:
        reasult+=chr(ord(i)+shift)
    return reasult



def decrept_function(data,shift):
    '''
    WHAT:  decrept_function was encrepty into normal text
    EXAMPLE:-
    input : print(decrept_function(vrqj#lv#exlw|ixoo,3))
    output: song is buityfull
    '''
    reasult=''  
    for i in data:
        reasult+=chr(ord(i)-shift)
    return reasult
