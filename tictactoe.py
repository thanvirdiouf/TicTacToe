import copy
space=" "
cross="X"
circle="O"
data=[space,space,space,space,space,space,space,space,space]

def displayboard(data):
    datahehe=copy.copy(data)
    for i in range(0,9):
        if datahehe[i]==space:
            datahehe[i]=str(i+1)
    print(datahehe[0]+"|"+datahehe[1]+"|"+datahehe[2])
    print("-----")
    print(datahehe[3]+"|"+datahehe[4]+"|"+datahehe[5])
    print("-----")
    print(datahehe[6]+"|"+datahehe[7]+"|"+datahehe[8])

def updatedata(data,symbol,position,chance):
    if data[position-1]==space:
        data[position-1]=symbol
        chance+=1
    else:
        print("Already filled!!!!!!!!!")
    
    return data,chance

def wincheck(data):
    win_conditions=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for i,j,k in win_conditions:
        if data[i]==data[j]==data[k]!=space:
            return True
    return False

print("Welcome to TicTacToe\nSelect symbol of Player 1\n1) X\n2) O")
players={}
players["p1"]=input("Enter:")
if players["p1"]=="x" or players["p1"]=="X" or players["p1"]=="1":
    players["p1"]=cross
    players["p2"]=circle
elif players["p1"]=="o" or players["p1"]=="O" or players["p1"]=="2":
    players["p1"]=circle
    players["p2"]=cross
else:
    print("Invalid input.Game exiting.")
    exit()

print("\nGamestarted")
chance=0
win=False
while chance<9 and not win:
    print("\nCurrent board:")
    displayboard(data)
    print("player"+str(chance%2+1)+"'s chance\nEnter position of "+players["p"+str(chance%2+1)])
    while True:
        try:
            position=int(input("position:"))
            if 1 <= position <= 9:
                break  # Valid input, exit the loop
            else:
                print("Number not in range 1-9. Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    data,chance=updatedata(data,players["p"+str(chance%2+1)],position,chance)
    if chance>=5:
        win=wincheck(data)
if win:
    displayboard(data)
    print("!!!!!!!!!!winner is player"+str(chance%2)+"!!!!!!!!!!!!!!!")
else:
    print("\nIt is a draw!!!!!")
