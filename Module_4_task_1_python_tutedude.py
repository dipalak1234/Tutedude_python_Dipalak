def fact(a):
    if(a<2):
        return 1
    else:
       return a*fact(a-1)
Num1=int(input('Enter a number: '))
print('Factorial of',Num1,'is:',fact(Num1))
