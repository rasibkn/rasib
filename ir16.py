import random
while(n<=100):
    n=input("enter q to quit,and r to roll the dice")
    if (n=='r'):
        r=random.randint(1,6)
        print("u got",r)
        x=x+r
        if(x==8):
            x=37
            print("you climbed a ladder your score is",x)
        elif(x==11):
            x=2
            print("snake bite, your score is",x)
        elif(x==13):
            x=34
            print("you climbed a ladder your score is",x)
        elif(x==25):
            x=4
            print("snake bite,your score is,x")
        elif(x==38):
            x=9
            print("snake bite,your score is,x")
        elif(x==40):
            x=68
            print("you climbed a ladder,your score is,x")
        elif(x==52):
            x=81
            print("you climbed a ladder,your score is,x")
        elif(x==65):
            x=46
            print("snake bite,your score is,x")
        elif(x==76):
            x=97
            print("you climbed a ladder,your score is ,x")
        elif(x==89):
            x=70
            print("snake bite,your score is,x")
        elif(x==93):
            x=64
            print("snake bite,your score is,x")
        elif(x==100):
            x=100
            print("you win")

        
        
         


