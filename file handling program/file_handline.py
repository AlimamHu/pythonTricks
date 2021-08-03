from io import StringIO
import os
os.chdir('daily/file handling program/')


# read() --> give string, asscess charecter 3,4,3,34
# readline() --> give String
# readlines() --> give list

def one_word():
    with open('fil1.txt', 'r') as t:
        for line in (t.readlines()):
            t= line.split(' ')
            for w in t:
                print(w)

def sing_word():
    with open('fil1.txt','r') as t:
        for line in t.readlines():
            for single_word in line:
                print(single_word)

#  no. character, words, spaces & line in a file :)
with open('fil1.txt','r') as t:
    file_in_list=t.readlines()
    
    spaces=0
    for i in range(len(file_in_list)):
        spac_values=file_in_list[i].count(' ')  # spaces count
        # print(spac_values)
        spaces+=spac_values  # 
    string=','.join(file_in_list)
    for i in string:
        print(i)
        
    t.close()
print('no of lines in the file :  ',len(file_in_list))   # line count 
print('no. of spaces: ' ,spaces)        