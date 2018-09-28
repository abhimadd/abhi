import random
count=0
while(count<=100):
	n=input("enter r to roll a dice")
	if(n=='r'):
		a=random.randint(1,6)
		count=count+a
		print("my posistion",count)
		print("your random value",a)
	if(count==11):
		count=2
		print("sorryy cobra bite")
	elif(count==13):
		count=34
		print("congo ladder")
	elif(count==25):
		count=4
		print("sorryy cobra bite")
	elif(count==38):
		count=8
		print("sorryy cobra bite")
	elif(count==40):
		count=68
		print("congo ladder")
	elif(count==52):
		count=81
		print("congo ladder")
	elif(count==65):
		count=46
		print("sorryy cobra bite")
	elif(count==76):
		count=97
		print("congo ladder")
	elif(count==89):
		count=70
		print("sorryy cobra bite")
	elif(count==93):
		count=64
		print("sorryy cobra bite")
	elif(count>100):
		count=count-a
		print("cant go beyond 100")
	elif(count==100):	
		print("won the king cobra")									
		break
		
		
		output
		
		enter r to roll a dicer
my posistion 1
your random value 1
enter r to roll a dicer
my posistion 3
your random value 2
enter r to roll a dicer
my posistion 6
your random value 3
enter r to roll a dicer
my posistion 8
your random value 2
enter r to roll a dicer
my posistion 12
your random value 4
enter r to roll a dicer
my posistion 14
your random value 2
enter r to roll a dicer
my posistion 18
your random value 4
enter r to roll a dicer
my posistion 22
your random value 4
enter r to roll a dicer
my posistion 28
your random value 6
enter r to roll a dicer
my posistion 33
your random value 5
enter r to roll a dicer
my posistion 38
your random value 5
sorryy cobra bite
enter r to roll a dicer
my posistion 9
your random value 1
enter r to roll a dicer
my posistion 11
your random value 2
sorryy cobra bite
enter r to roll a dicer
my posistion 7
your random value 5
enter r to roll a dicer
my posistion 13
your random value 6
congo ladder
enter r to roll a dicer
my posistion 39
your random value 5
enter r to roll a dicer
my posistion 42
your random value 3
enter r to roll a dicer
my posistion 46
your random value 4
enter r to roll a dicer
my posistion 48
your random value 2
enter r to roll a dicer
my posistion 54
your random value 6
enter r to roll a dicer
my posistion 57
your random value 3
enter r to roll a dicer
my posistion 58
your random value 1
enter r to roll a dicer
my posistion 61
your random value 3
enter r to roll a dicer
my posistion 66
your random value 5
enter r to roll a dicer
my posistion 68
your random value 2
enter r to roll a dicer
my posistion 69
your random value 1
enter r to roll a dicer 
my posistion 71
your random value 2
enter r to roll a dicer
my posistion 74
your random value 3
enter r to roll a dicer
my posistion 77
your random value 3
enter r to roll a dicer
my posistion 81
your random value 4
enter r to roll a dicer
my posistion 85
your random value 4
enter r to roll a dicer
my posistion 91
your random value 6
enter r to roll a dicer
my posistion 97
your random value 6
enter r to roll a dicer
my posistion 103
your random value 6
cant go beyond 100
enter r to roll a dicer
my posistion 102
your random value 5
cant go beyond 100
enter r to roll a dicer
my posistion 99
your random value 2
enter r to roll a dicer
my posistion 101
your random value 2
cant go beyond 100
enter r to roll a dicer
my posistion 104
your random value 5
cant go beyond 100
enter r to roll a dicer
my posistion 103
your random value 4
cant go beyond 100
enter r to roll a dicer
my posistion 100
your random value 1
won the king cobra

