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
