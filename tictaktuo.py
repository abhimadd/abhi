tic=['1','2','3','4','5','6','7','8','9']

def printboard():
	print(tic[0]+'|'+tic[1]+'|'+tic[2])
	print("--------")
	print(tic[3]+'|'+tic[4]+'|'+tic[5])
	print("--------")
	print(tic[6]+'|'+tic[7]+'|'+tic[8])
printboard()

playeroneturn=True

for i in range(9):
	printboard()	
#player 1 plays
	if playeroneturn:
		p=input("player 1, choose your place:")
		if p in tic:
			tic[int(p)-1]='X'  
			playeroneturn= not playeroneturn
#player 2 plays
	else:	
		p=input("player 2,choose your place:")
		if p in tic:
			tic[int(p)-1]= 'O'
			playeroneturn= not playeroneturn

#check for winning combinations
for x in range(0,3):
	y= x*3
	if(tic[x]== tic[(y+1)] and tic[y]== tic[(y+2)])
	winner=True
	printboard()

	if(tic[x]==tic[(x+3)] and tic[x]== tic[(x+6)])
	winner=True
	printboard()

	if((tic[0]==tic[4] and tic[0]==tic[8])	or (tic[2] and tic[4]==tic[6]))
		winner=True

#check for a tie condition
print("its a tie")			