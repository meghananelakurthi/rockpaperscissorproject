n=int(input("enter how many times to be played?"))
if(n<0):
    print("please enter a valid number")
else:
    for i in range(n):
        print("press",0,"rock")
        print("press",1,"paper")
        print("press",2,"scissor")
        objects=["rock","paper","scissor"]
        meghana=int(input("enter player choice"))
        if(meghana>=len(objects)):
            print("Invalid choice")
        import random
        computer=random.randint(0,2)
        print(objects[meghana],"selected by meghana")
        
        print(objects[computer],"selected by computer")
        if meghana==0 and computer==1:
            print("computer is winner")
        elif meghana==1 and computer==0:
            print("player is winner") 
        elif meghana==1 and computer==2:
            print("computer is winner")
        elif meghana==2 and computer==1:
            print("player is winner")
        elif meghana==2 and computer==0:
            print("computer is winner")
        elif meghana==0 and computer==2:
            print("player is winner")
        else:
            print("computer and meghana both are winners")
