import random
from colorama import Fore, Style, ansi

#Mode Selection
while True:
    print('Welcome to Bingo!\nPlease select a mode.\n1: Bingo Board\n2: Bingo Number Caller\nQuit: Exit')
    Mode = input("")


    if Mode=="1":
        INVERT=Fore.GREEN
        RESET=Style.RESET_ALL
        CLEAR=ansi.clear_screen() + ansi.Cursor.POS(1, 1)

        g=[[0 for _ in range(5)] for _ in range(5)]


        # Fill in the board
        used=[]

        for y in range(0,5):
            for x in range(0,5):
                offset=x*15
                while (r:=random.randint(1+offset,15+offset)) in used:
                    continue
                g[y][x]=r
                used.append(r)
        g[2][2]-=1000

        BINGO=[]

        print(CLEAR)
        while (wincondition:=input("Which win condition? (any/horiz/vert/angle)  ").lower()) \
                not in ["any","horiz","vert","angle"]:
                    continue

        while len(BINGO)==0:
            # Clear screen
            print(CLEAR)

            # Draw board
            for row in g:
                print(*[" .." if n<0 else f"{n:>3}" for n in row],sep='')
            print()

            # Get user input
            number=int(input("(Only input the number, not the letter!)\nEx. input '21' not 'B-21'.\nWhat number was called?  "))

            # Set cell called by user
            for y in range(0,5):
                for x in range(0,5):
                    if g[y][x]==number:
                        g[y][x]-=1000
            #g=[[cell-1000 if cell==number else cell for cell in row] for row in g]

            # Check for BINGO
            wins = []
            if wincondition=="any" or wincondition=="angle":
                wins += [[[0,0],[1,1],[2,2],[3,3],[4,4]],
                         [[0,4],[1,3],[2,2],[3,1],[4,0]]]
            if wincondition=="any" or wincondition=="horiz":
                wins += [[[0,0],[0,1],[0,2],[0,3],[0,4]],
                         [[1,0],[1,1],[1,2],[1,3],[1,4]],
                         [[2,0],[2,1],[2,2],[2,3],[2,4]],
                         [[3,0],[3,1],[3,2],[3,3],[3,4]],
                         [[4,0],[4,1],[4,2],[4,3],[4,4]]]
            if wincondition=="any" or wincondition=="vert":
                wins += [[[0,0],[1,0],[2,0],[3,0],[4,0]],
                         [[0,1],[1,1],[2,1],[3,1],[4,1]],
                         [[0,2],[1,2],[2,2],[3,2],[4,2]],
                         [[0,3],[1,3],[2,3],[3,3],[4,3]],
                         [[0,4],[1,4],[2,4],[3,4],[4,4]]]

            # Append wins to BINGO
            for win in wins:
                if all(g[a][b]<0 for [a,b] in win):
                    BINGO.append(win)


        else:
            # Clear screen
            print(CLEAR)

            # Draw board
            for y,row in enumerate(g):
                for x,cell in enumerate(row):
                    if cell<0:
                        coord=[y,x]
                        ch=" **"
                        for win in BINGO:
                            if coord in win:
                                ch=f" {INVERT}{cell+1000:>2}{RESET}"
                        print(ch,end='')
                    else:
                        print(f"{cell:>3}",end='')
                print()

            print()
            for win in BINGO:
                print(win)
            print("BINGOOOOO!!!!")

    elif Mode=="2":

        # Bingo Caller Program

        # VARIABLES USED: Numbers_Called, Number, BingoCalled, HORSE_CHECK
        # IMPORTS USED: colorama
        from colorama import Fore, Back, Style, init

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

        print(Back.GREEN + Fore.LIGHTWHITE_EX + f"{Number}")
        # attempting to add to the array
        Numbers_Called.append(Number)

        BingoCalled = input("\nHas Anyone Called Bingo? (y/n): ").lower()

        if BingoCalled == "y":
            print(Back.LIGHTWHITE_EX + Fore.RED + "Come on up!")
        else:
            while BingoCalled != "y" and BingoCalled != "n":
                print("Please enter either 'y' or 'n' next time.")
                BingoCalled = input("\nHas Anyone Called Bingo? (y/n): ").lower()
            print(Fore.WHITE + "\nWe need to pick another number.....")
            while BingoCalled != "y":
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

                print(Back.GREEN + Fore.LIGHTWHITE_EX + f"{Number}")
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
    elif Mode == "Quit":
        break
    else:
        print('\nPlease try again.\n')