import random
a={1:'rock',2:'paper',3:'scissors'}
a=0
b=0
while a<3 and b<3:
	p=input("Your choice rock/paper/scissors:")
	r=a[random.randint(1,3)]
	print("You chose:",p,"Computer chose::",c)
	if(p==c):
		print("draw")
	elif(p=='rock'):
		if(c=='scissors'):
			print("u win")
			b=b+1
	elif(p=='paper'):
		if(c=='rock'):
			print("computer win")
			a=a+1
	elif(p=="scissors"):
		if(c=='rock'):
			print("computer win")
			a=a+1
	elif(p=='rock'):
		if(c=='paper'):
			print("computer win")
			a=a+1
	elif(p=='scissors'):
		if(c=='paper'):
			print("u win")
			b=b+1
			print("my score:",b,"computer score:",a)
	elif(p=='rock'):
		if(c=='scissors'):
			print("u win")	
			b=b+1
	else:
		break

