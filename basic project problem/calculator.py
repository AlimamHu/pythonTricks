first=int(input('Enter your first : '))
operator=input('enter + - / * ** : ')
second=int(input('Enter your Second : '))

if operator=='+':
    print(first+second)
elif operator=='-':
    print(first-second)
elif operator=='*':
    print(first*second)
else:
    if operator=='/':
        print(first/second)
    else:
        print(first**second)