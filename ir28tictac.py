def printBoard():
	
		print("|1|2|3|")	
		print("-------")   
		print("|4|5|6|")
		print("-------")
		print("|7|8|9|")		
		print("-------")
printBoard()

a=[1,2,3,4,5,6,7,8,9]
def printBoard():
	print(a[0],'|',a[1],"|",a[2])
	print("--------------------")
	print(a[3],'|',a[4],'|',a[5])
	print("--------------------")
	print(a[6],'|',a[7],'|',a[8])

printBoard()

playeroneturn=True

while True:
	printBoard()
	p=int(input("chose ur place >>>"))
	if(p in a):
		if playeroneturn:
			#p=input("choose your place,player1>>")
			print("player one choose")
			a[p-1]='x'
			playeroneturn=not playeroneturn
		else:	
		#p =input("choose ypur place ,player2>>")
		print("player 2 choose:",p)
		a[p-1] = 'O'
		playeroneturn= not playeroneturn 

		#check for winning conditions 
		for i in (0,3,6):
			if (a)



