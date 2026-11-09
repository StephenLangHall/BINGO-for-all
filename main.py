import random
from colorama import Fore, Back, Style, ansi, init

INVERT=Fore.GREEN
RESET=Style.RESET_ALL
CLEAR=ansi.clear_screen() + ansi.Cursor.POS(1, 1)

print(CLEAR)


#################### FUNCTIONS ###################


def Random(offset):
    return random.randint(1+offset*15,15+offset*15)

def NewBoard():
    b=[[0 for _ in range(5)] for _ in range(5)]
    u=[]
    for y in range(5):
        for x in range(5):
            while (n:=Random(x)) in u: continue
            b[y][x]=n
            u.append(n)
    b[2][2]-=1000
    return b

def DrawBoard(BINGO,b):
    print(CLEAR)
    for y in range(5):
        for x in range(5):
            number=b[y][x]+1000 if b[y][x]<0 else b[y][x]
            color=Fore.BLUE if b[y][x]<0 else ""
            for win in BINGO:
                color=Fore.GREEN if [y,x] in win else color
            print(f"{color}{number:>3}{Style.RESET_ALL}",end="")
        print()

def CheckBoard(wc,b):
    # Check for BINGO
    wins=[]
    possible=[]
    if wc==0 or wc==3:
        possible+=[[[0,0],[1,1],[2,2],[3,3],[4,4]],
                   [[0,4],[1,3],[2,2],[3,1],[4,0]]]
    if wc==0 or wc==1:
        possible+=[[[0,0],[0,1],[0,2],[0,3],[0,4]],
                   [[1,0],[1,1],[1,2],[1,3],[1,4]],
                   [[2,0],[2,1],[2,2],[2,3],[2,4]],
                   [[3,0],[3,1],[3,2],[3,3],[3,4]],
                   [[4,0],[4,1],[4,2],[4,3],[4,4]]]
    if wc==0 or wc==2:
        possible+=[[[0,0],[1,0],[2,0],[3,0],[4,0]],
                   [[0,1],[1,1],[2,1],[3,1],[4,1]],
                   [[0,2],[1,2],[2,2],[3,2],[4,2]],
                   [[0,3],[1,3],[2,3],[3,3],[4,3]],
                   [[0,4],[1,4],[2,4],[3,4],[4,4]]]

    # Append wins to BINGO
    for win in possible:
        if all(b[y][x]<0 for [y,x] in win):
            wins.append(win)
    return wins


###################### MAIN ######################


#Mode Selection
while True:
    print(CLEAR)
    print('Welcome to Bingo!\n1: Bingo Board\n2: Bingo Number Caller\n0: Exit')
    Mode = input("\nPlease select a mode: ")


    if Mode=="1":
        b=NewBoard()
        
        BINGO=[]
        print(CLEAR)
        wc=int(input("Enter num for Win Condition\n0=any\n1=horizontal\n2=vertical\n3=angular\n: "))
        while not BINGO:
            DrawBoard(BINGO,b)
            n=int(input("Input number only ('31' not 'B-31')\nWhat num was called?\n: "))
            b=[[c-1000 if c==n else c for c in row] for row in b]
            BINGO=CheckBoard(wc,b)
        else:
            DrawBoard(BINGO,b)
            for win in BINGO:
                print(win)
            print("BINGOOOOOOOOOOOOOOOOOOO")

    elif Mode=="2":

        # Bingo Caller Program

        # VARIABLES USED: Numbers_Called, Number, BingoCalled, HORSE_CHECK
        # IMPORTS USED: colorama

        init(autoreset=True)

        # creating the array
        Numbers_Called = []

        # time to pick a number
        input("Press Enter to draw a bingo ball!")
        Number = random.randint(1, 75)

        # Number = int(input("Enter The Number (1 - 75): "))
        # NEED TO CHANGE IT TO WHERE THE OUTPUT IS A VARIABLE SO THAT I CAN ADD IT TO THE ARRAY
        if Number > 75 or Number < 1:
            print("The Number must be between 1 and 75")
            # Eventually Loop Back To Ask Again
        elif Number >= 1 and Number < 15:
            Number = ("B", Number)
        elif Number >= 16 and Number < 30:
            Number = ("I", Number)
        elif Number >= 31 and Number < 45:
            Number = ("N", Number)
        elif Number >= 46 and Number < 60:
            Number = ("G", Number)
        else:
            Number = ("O", Number)

        print('\n' + Back.GREEN + Fore.LIGHTWHITE_EX + f"{Number}")
        # attempting to add to the array
        Numbers_Called.append(Number)

        BingoCalled = input("\nHas Anyone Called Bingo? (y/n): ").lower()

        if BingoCalled == "y":
            print(Back.LIGHTWHITE_EX + Fore.RED + "Come on up!")
        else:
            while BingoCalled != "y" and BingoCalled != "n":
                print("Please enter either 'y' or 'n' next time.")
                BingoCalled = input("\nHas Anyone Called Bingo? (y/n): ").lower()

            while BingoCalled != "y":
                print(Fore.WHITE + "\nWe need to pick another number.....")
                # time to pick a number
                HORSE_CHECK = input(
                    'Press Enter to draw a bingo ball or type "called" to see what numbers have been called: ').lower()

                # Horse check is there to be an options menu to give the Host tools
                if HORSE_CHECK == "called":
                    init(autoreset=False)
                    print("\n" * 5)
                    print(
                        Back.BLACK + Fore.LIGHTWHITE_EX + "\t" + Back.LIGHTYELLOW_EX + Fore.BLACK + "\t{Numbers_Called}\t" + Back.BLACK + Fore.LIGHTWHITE_EX + "\t")
                    print(Back.LIGHTYELLOW_EX + Fore.LIGHTYELLOW_EX + "\t                 \t\t\t")
                    print(*Numbers_Called, sep="\n")
                    init(autoreset=True)
                    continue

                Number = random.randint(1, 75)

                # Number = int(input("Enter The Number (1 - 75): "))
                if Number > 75 or Number < 1:
                    print("The Number must be between 1 and 75")
                    # Eventually Loop Back To Ask Again
                elif Number >= 1 and Number < 15:
                    Number = ("B", Number)
                elif Number >= 16 and Number < 30:
                    Number = ("I", Number)
                elif Number >= 31 and Number < 45:
                    Number = ("N", Number)
                elif Number >= 46 and Number < 60:
                    Number = ("G", Number)
                else:
                    Number = ("O", Number)

                print('\n' + Back.GREEN + Fore.LIGHTWHITE_EX + f"{Number}")
                # attempting to add to the array
                Numbers_Called.append(Number)

                BingoCalled = input("\nHas Anyone Called Bingo? (y/n): ").lower()
                while BingoCalled != "y" and BingoCalled != "n":
                    print("Please enter either 'y' or 'n' next time.")
                    BingoCalled = input("\nHas Anyone Called Bingo? (y/n): ").lower()
                if BingoCalled == "y":
                    print("Come on up!")
                    print("\nThe following numbers have been called.")

                    init(autoreset=False)
                    print("\n" * 5)
                    print(
                        Back.BLACK + Fore.LIGHTWHITE_EX + "\t" + Back.LIGHTYELLOW_EX + Fore.BLACK + "\t{Numbers_Called}\t" + Back.BLACK + Fore.LIGHTWHITE_EX + "\t")
                    print(Back.LIGHTYELLOW_EX + Fore.LIGHTYELLOW_EX + "\t                 \t\t\t")
                    print(*Numbers_Called, sep="\n")
                    init(autoreset=True)


                    CHECK = input("\nWas the bingo accurate? (y/n): ").lower()
                    if CHECK == "n":
                        BingoCalled = "n"
                    elif CHECK != "n" and CHECK != "y":
                        print('You answered neither y or n. We will assume the bingo was not accurate.')


        init(autoreset=False)
        print("\n" * 5)
        print(
            Back.BLACK + Fore.LIGHTWHITE_EX + "\t" + Back.LIGHTYELLOW_EX + Fore.BLACK + "\t{Numbers_Called}\t" + Back.BLACK + Fore.LIGHTWHITE_EX + "\t")
        print(Back.LIGHTYELLOW_EX + Fore.LIGHTYELLOW_EX + "\t                 \t\t\t")
        print(*Numbers_Called, sep="\n")
    elif Mode == "0":
        break
    else:
        print(CLEAR)
        print('\nPlease try again.\n')