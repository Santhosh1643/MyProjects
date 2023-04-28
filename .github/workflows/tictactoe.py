#python program for tic tac toe
x=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player1=' '
player2=' '
#function for drawing boxes
def draw():
    global x
    for i in range(1,10):
        print('|',x[i],end='')
        if i==3 or i==6 or i==9:
            print('| \n')
#Function for welcoming and assigning x and o for players
def prompt():
    global player1,player2
    print("Welcome to tic tac toe!")
    player1=input("Player1 choose x or o:")
    if player1=='x' or player1=='X':
        player1='X'
        player2='O'
    else:
        player1='O'
        player2='X'
    pos()

#Function to get input from user and place it
def pos():
    global x
    c=''
    while True:
        print('---------------------------------------')
        draw()
        if c != 'error':
            a=int(input(f"Player1 Enter your position to place {player1}:"))
            if a<=10:
                if x[a]==' ':
                    x[a]=player1
                    draw()
                else:
                    print("oops! the position is not available")
                    continue
                if win()==1:
                    print("player1 won!")
                    break
                if win()==2:
                    print("player2 won!")
                    break
            else:
                print("Please enter value below 9")
                continue
       
            
        c=''
        b=int(input(f"Player2 Enter your position to place {player2}:"))
        if b<=10:
            if x[b]==' ':
                x[b]=player2
                draw()
            else:
                print("oops! the position is not available")
                continue

            if win()==1:
                print("player1 won!")
                break
            if win()==2:
                print("player2 won!")
                break
        else:
            print("Please enter value below 9")
            c='error'    

#function for checking winning condition
def win():
    if x[1]==x[2]==x[3]==player1  or x[1]==x[4]==x[7]==player1 or x[1]==x[5]==x[9]==player1 or x[2]==x[5]==x[8]==player1 or x[3]==x[6]==x[9]==player1 or x[3]==x[5]==x[7]==player1 or x[4]==x[5]==x[6]==player1 or x[7]==x[8]==x[9]==player1:
        return 1
    if x[1]==x[2]==x[3]==player2  or x[1]==x[4]==x[7]==player2 or x[1]==x[5]==x[9]==player2 or x[2]==x[5]==x[8]==player2 or x[3]==x[6]==x[9]==player2 or x[3]==x[5]==x[7]==player2 or x[4]==x[5]==x[6]==player2 or x[7]==x[8]==x[9]==player2:
        return 2

prompt()
