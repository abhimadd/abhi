import random
d={1:'R',2:'P',3:'S'}
C=d[random.randint(1,3)]
while(True):
	P=input("enter the value 'R','P','S'")
	if(C==P):
		print("tie")
	elif(C=='R'and P=='S' or C=='P'and P=='R' or C=='S'and P=='P'):
		print("COMPUTER WON it")
	else:
		print("PLAYER  WON it")
		break