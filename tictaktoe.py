import random

print("Welcome to your new tic tok toe game")
print("------------------------------------")

possiblenumber=[1,2,3,4,5,6,7,8,9]

gameboard=[[1,2,3],[4,5,6],[7,8,9]]

##This function prints out the gameboard\
def printGameboard():

    for i in range(3):
      print("\n+-----+-----+-----+")
      print("|",end="")
      for j in range(3):
          print("  ",gameboard[i][j],end=" |")
    print("\n+----+-----+-----+")
      


def modifyList(num,turn):
    num-=1

    if num==0:
      gameboard[0][0]=turn
    elif num==1:
           gameboard[0][1]=turn
    elif num==2:
           gameboard[0][2]=turn
    elif num==3:
           gameboard[1][0]=turn
    elif num==4:
           gameboard[1][1]=turn
    elif num==5:
           gameboard[1][2]=turn
    elif num==6:
           gameboard[2][0]=turn
    elif num==7:
           gameboard[2][1]=turn
    elif num==8:
           gameboard[2][2]=turn

def checkForWinner(gameboard):
    #x axis
    if gameboard[0][0]=='X' and gameboard[0][1]=='X' and gameboard[0][2]=='X':
       print("X has won")
       return"X"
    elif gameboard[1][0]=='X' and gameboard[1][1]=='X' and gameboard[1][2]=='X':
       print("X has won")
       return"X"
    elif gameboard[2][0]=='X' and gameboard[2][1]=='X' and gameboard[2][2]=='X':
       print("X has won")
       return"X"
    elif gameboard[0][0]=='O' and gameboard[0][1]=='O' and gameboard[0][2]=='O':
       print("O has won")
       return"O"
    elif gameboard[1][0]=='O' and gameboard[1][1]=='O' and gameboard[1][2]=='O':
       print("O has won")
       return"O"
    elif gameboard[2][0]=='O' and gameboard[2][1]=='O' and gameboard[2][2]=='O':
       print("O has won")
       return"O"
    ## y axis
    if gameboard[0][0]=='X' and gameboard[1][0]=='X' and gameboard[2][0]=='X':
       print("X has won")
       return"X"
    elif gameboard[0][1]=='X' and gameboard[1][1]=='X' and gameboard[2][1]=='X':
       print("X has won")
       return"X"
    elif gameboard[0][2]=='X' and gameboard[1][2]=='X' and gameboard[2][2]=='X':
       print("X has won")
       return"X"
    elif gameboard[0][0]=='O' and gameboard[1][0]=='O' and gameboard[2][0]=='O':
       print("O has won")
       return"O"
    elif gameboard[0][1]=='O' and gameboard[1][1]=='O' and gameboard[2][1]=='O':
       print("O has won")
       return"O"
    elif gameboard[2][0]=='O' and gameboard[2][1]=='O' and gameboard[2][2]=='O':
       print("O has won")
       return"O"
    #cross
    if gameboard[0][0]=='X' and gameboard[1][1]=='X' and gameboard[2][2]=='X':
       print("X has won")
       return"X"
    elif gameboard[0][2]=='X' and gameboard[1][1]=='X' and gameboard[2][0]=='X':
       print("X has won")
       return"X"
    elif gameboard[0][0]=='O' and gameboard[1][1]=='O' and gameboard[2][2]=='O':
       print("O has won")
       return"O"
    elif gameboard[0][2]=='X' and gameboard[1][1]=='O' and gameboard[2][0]==')':
       print("O has won")
       return"O"

    
           

leaveloop=False
turn_counter=0

while(leaveloop==False):
    if checkForWinner(gameboard) =='X':
        print(checkForWinner(gameboard))
        break
    elif checkForWinner(gameboard) =='O':
        print(checkForWinner(gameboard))
        break
    if(turn_counter%2==1):
        turn_counter+=1
        print(printGameboard())
        numberpicked=int(input("\nChoose a nume [1-9]: "))
        if(numberpicked >=1 or numberpicked <=9):
            modifyList(numberpicked,'X')
            possiblenumber.remove(numberpicked)
        else:
            print("Invalid input. try again ")
            turn_counter+=1
    else:
        while(True):
            cpu=random.choice(possiblenumber)
            print("\nCpu choice: ",cpu)
            if(cpu in possiblenumber):
                 modifyList(cpu,'O')
                 possiblenumber.remove(cpu)
                 turn_counter+=1
                 break
                 
        
  
  
  
  
