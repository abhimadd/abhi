#write program to take 2 numbers from the user,
#then take option to add/subtract/multiple/divide
#and perform that operation
a=int (input("enter a value"))
b=int (input("enter b value"))
c=a+b
print("addition of two numbers",c)
d=a-b
print("subtraction of two numbers",d)
e=a*b
print("multiplication of two numbers",e)
f=a/b
print("division of two numbers",f)
g=a%b
print("percentage of two numbers",g)

output
cl315@soetcse:~/abhishek$ python3 mathop.py
python3: can't open file 'mathop.py': [Errno 2] No such file or directory
cl315@soetcse:~/abhishek$ python3 mathopt.py
enter a value10
enter b value6 
addition of two numbers 16
subtraction of two numbers 4
multiplication of two numbers 60
division of two numbers 1.6666666666666667
percentage of two numbers 4
cl315@soetcse:~/abhishek$ 

