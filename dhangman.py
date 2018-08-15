def hangman(word):
    wrong = 0
    stages = [ "",
             "_____     ",
             "]         ",
             "]    ]    ",
             "]    0    ",
             "]   ( )   ",
             "]   (_)   ",
             "]         "
               ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman Game! If you don't like, type 'quit'.")
    while wrong < len(stages) -1:
        print("\n")
        msg = "Guess a character"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        elif char == "quit":
            break
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You Win")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print(" The correct answer is {}.".format(word))

lista = ["cat", "dog", "door", "poop", "scottland", "candy"]
import random
s = random.randint(0,len(lista)-1)
hangman(lista[s])
