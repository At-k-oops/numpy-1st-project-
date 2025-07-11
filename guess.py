import numpy as np 

total_point=0
def game():
    global total_point
    print("Choose any three number between 0 to 10:")   
    A=[]
    for i in range (0,3):
        a=int(input("Enter your numbers :"))
        A.append(a)
    
    x=np.array(A)
    y=np.random.randint(0,10,size=3)
    
    point=0
    if np.array_equal(x,y):
        print("Jackpot")
        point=100
    elif (x[0]==y[0]) or (x[1]==y[1]) or (x[2]==y[2]):
        print("keep going have a wonderful luck today")
        point=45
    elif (x[0]==y[0] and x[1]==y[1]) or (x[1]==y[1] and x[2]==y[2]) or (x[2]==y[2] and x[0]==y[0]):
        print("got some harden luck buddy")
        point=25
    else:
        print("You lose")
        point=(-20)
    
    total_point = total_point + point   

    print("Game over")
    print("Your score =",total_point)

game()
while True:
        
    print("Will u want to play game :YES/NO:")
    c=int(input("Enter 1 for Yes and 2 for No :")  )
    if c==1:
        game()
    else :
        print(".......................")
        print("final score:",total_point)
        break
