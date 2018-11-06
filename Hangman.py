import random

# menu in English
def menuEn(wordlist):
    print("The Hangman game")
    print(" ________________________________ ")
    print("  |    /                        | ")
    print("  |   /                         | ")
    print("  |  /                        (°_°) ")
    print("  | /                           | ")
    print("  |/                           /|\ ")
    print("  |    Play (1)               / | \ ")
    print("  |                          /  |  \ ")
    print("  |                             | ")
    print("  |    Change language (2)      | ")
    print("  |                            / \ ")
    print("  |                           /   \ ")
    print("  |    Exit (3)              /     \ ")
    print("  |")
    print("  |")
    print("  |")
    print("-----")

    option = input("")

    if option == "1": #enters the game
        print ("Entering the game...")
        maingameEn(wordlist)

    elif option == "2": #enters language select menu
        languageselection()

    elif option == "3": #exits the game
        print ("Exiting the game...")

    else:
        print ("Invalid option")
        menuEn(wordlist)

# menu in Portuguese
def menuPt(wordlist):
    print("Jogo da Forca")
    print(" ________________________________ ")
    print("  |    /                        | ")
    print("  |   /                         | ")
    print("  |  /                        (°_°) ")
    print("  | /                           | ")
    print("  |/                           /|\ ")
    print("  |    Jogar (1)              / | \ ")
    print("  |                          /  |  \ ")
    print("  |                             | ")
    print("  |    Escolher idioma (2)      | ")
    print("  |                            / \ ")
    print("  |                           /   \ ")
    print("  |    Sair (3)              /     \ ")
    print("  |")
    print("  |")
    print("  |")
    print("-----")

    option = input("")

    if option == "1":
        print ("A entrar no jogo...") #Enters the game
        maingamePt(wordlist)

    elif option == "2": #opens language select menu
        languageselection()

    elif option == "3": #Exits the game
        print ("A sair do jogo...")

    else:
        print ("Opcao invalida")
        menuPt(wordlist)


# menu for the language selection
def languageselection():
    print("The Hangman game")
    print(" ________________________________ ")
    print("  |    /                        | ")
    print("  |   /  Select language        | ")
    print("  |  /                        (°_°) ")
    print("  | /                           | ")
    print("  |/                           /|\ ")
    print("  |                           / | \ ")
    print("  |    English (En)          /  |  \ ")
    print("  |                             | ")
    print("  |                             | ")
    print("  |    Portuguese (Pt)         / \ ")
    print("  |                           /   \ ")
    print("  |                          /     \ ")
    print("  |")
    print("  |")
    print("  |")
    print("-----")

    language = input("")
    if language == "Pt" or language == "pt" or language == "Portuguese" or language == "portuguese":  #if portuguese is selected creates a list with words in portuguese from the file word_Pt.txt
        print("Portuguese selected")

        with open("words_Pt.txt","r") as f: #imports words from the file
            wordlist = []
            for line in f:
                category, word = line.split()
                wordlist.append((category, word))
            f.close
        menuPt(wordlist) #goes to the selected language menu

    elif language == "En" or language == "en" or language == "English" or language == "english":  #if english is selected creates a list with words in english from the file word_En.txt
        print("English selected")

        with open("words_En.txt","r") as f: #imports words from the file
            wordlist = []
            for line in f:
                category, word = line.split()
                wordlist.append((category, word))
            f.close
        menuEn(wordlist) #goes to the selected language menu

    else:
        print("Invalid language")
        languageselection()

def maingamePt(wordlist):
    try:
        wordnumber = random.randint(1,len(wordlist)-1) #chooses the word
        choosedpair = wordlist[wordnumber]
        wordlist.remove(choosedpair)  #removes the choosed word from future games
        category = choosedpair[0]   #separates the word from the category
        word = choosedpair[1]
        letters = list(word)
        lettersshow = []
        for i in range(0,len(word)):  #creates a list with the same number of spaces as letters of the word
            lettersshow.append(" __")
        guessed = []
        rightguessed = 0
        won = False
        lost = False
        fails = 0
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        while won == False and lost == False: #loop will only run if the player havent lost/won yet
            if fails == 0: #interface if the player failed 0 times
                print("Jogo da Forca")
                print(" ________________________________ ")
                print("  |    /                        | ")
                print("  |   /                         | ")
                print("  |  /")
                print("  | /")
                print("  |/")
                print("  |    Para desitir escreva:")
                print("  |          \"Desisto\"")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("-----   ", "".join(lettersshow), " - ", category)

            elif fails == 1: #interface if the player failed 1 time
                print("Jogo da Forca")
                print(" ________________________________ ")
                print("  |    /                        | ")
                print("  |   /                         | ")
                print("  |  /                        (°_°) ")
                print("  | /")
                print("  |/")
                print("  |    Para desitir escreva:")
                print("  |          \"Desisto\"")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("-----   ", "".join(lettersshow), " - ", category)

            elif fails == 2: #interface if the player failed 2 times
                print("Jogo da Forca")
                print(" ________________________________ ")
                print("  |    /                        | ")
                print("  |   /                         | ")
                print("  |  /                        (°_°) ")
                print("  | /                           | ")
                print("  |/                            |")
                print("  |    Para desitir escreva:    |")
                print("  |          \"Desisto\"          |")
                print("  |                             |")
                print("  |                             |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("-----   ", "".join(lettersshow), " - ", category)

            elif fails == 3: #interface if the player failed 3 times
                print("Jogo da Forca")
                print(" ________________________________ ")
                print("  |    /                        | ")
                print("  |   /                         | ")
                print("  |  /                        (°_°) ")
                print("  | /                           | ")
                print("  |/                           /|")
                print("  |    Para desitir escreva:  / |")
                print("  |          \"Desisto\"       /  |")
                print("  |                             | ")
                print("  |                             | ")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("-----   ", "".join(lettersshow), " - ", category)

            elif fails == 4: #interface if the player failed 4 times
                print("Jogo da Forca")
                print(" ________________________________ ")
                print("  |    /                        | ")
                print("  |   /                         | ")
                print("  |  /                        (°_°) ")
                print("  | /                           | ")
                print("  |/                           /|\ ")
                print("  |    Para desitir escreva:  / | \ ")
                print("  |          \"Desisto\"       /  |  \ ")
                print("  |                             | ")
                print("  |                             | ")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("-----   ", "".join(lettersshow), " - ", category)

            elif fails == 5: #interface if the player failed 5 times
                print("Jogo da Forca")
                print(" ________________________________ ")
                print("  |    /                        | ")
                print("  |   /                         | ")
                print("  |  /                        (°_°) ")
                print("  | /                           | ")
                print("  |/                           /|\ ")
                print("  |    Para desitir escreva:  / | \ ")
                print("  |          \"Desisto\"       /  |  \ ")
                print("  |                             | ")
                print("  |                             | ")
                print("  |                            /")
                print("  |                           /")
                print("  |                          /")
                print("  |")
                print("  |")
                print("  |")
                print("-----   ", "".join(lettersshow), " - ", category)

            else: #will end the game if the player has more than 5 fails
                lost = True
                break

            guess = input("")

            if guess in guessed: #check if the player repeated some letter
                print("You've already said that letter")

            elif guess == "Give up" or guess == "give up": #gaves up
                print("Jogo da Forca")
                print(" ________________________________ ")
                print("  |    /                        | ")
                print("  |   /                         | ")
                print("  |  /                        (°_°) ")
                print("  | /                           | ")
                print("  |/                           /|\ ")
                print("  |                           / | \ ")
                print("  |         Desistiu         /  |  \ ")
                print("  |                             | ")
                print("  |                             | ")
                print("  |                            / \ ")
                print("  |                           /   \ ")
                print("  |                          /     \ ")
                print("  |")
                print("  |")
                print("  |")
                print("-----   ", word, " - ", category)
                input("")
                menuEn(wordlist)

            elif len(guess) != 1: #if is more than one caracter
                print("Palpite invalido: Escreva apenas uma letra de cada vez")

            elif guess in ALPHABET: #if player writes in upper case is not valid
                print("Palpite invalido: Nao use maiusculas")

            elif guess not in alphabet: #if it is not a letter is not valid
                print("Caracter invalido")

            else:
                guessed.append(guess) #will add the letter to the listof letters already guessed
                if guess in letters: #if player guesses right will remove that word from the list of remaining letters and add it to the guessed letters
                    while guess in letters:
                        guesslocation = letters.index(guess)
                        del lettersshow[guesslocation]
                        lettersshow.insert(guesslocation,guess)
                        del letters[guesslocation]
                        letters.insert(guesslocation," ")
                        rightguessed = rightguessed + 1

                    if rightguessed == len(word): #sees if player as already guessed all letters
                        won = True

                else:
                    fails = fails + 1
                    if fails >= 6: #if player fail more than 5 times
                        lost = True

        if won == True: #player wins
            print("Jogo da Forca")
            print(" ________________________________ ")
            print("  |    /                        | ")
            print("  |   /                         | ")
            print("  |  /                        (°_°) ")
            print("  | /                           | ")
            print("  |/                           /|\ ")
            print("  |        Parabens           / | \ ")
            print("  |        Ganhaste          /  |  \ ")
            print("  |                             | ")
            print("  |                             | ")
            print("  |                            / \ ")
            print("  |                           /   \ ")
            print("  |                          /     \ ")
            print("  |")
            print("  |")
            print("  |")
            print("-----   ", word, " - ", category)
            input("")
            menuEn(wordlist)

        elif lost == True: #player loses
            print("Jogo da Forca")
            print(" ________________________________ ")
            print("  |    /                        | ")
            print("  |   /                         | ")
            print("  |  /                        (°_°) ")
            print("  | /                           | ")
            print("  |/                           /|\ ")
            print("  |         Perdeste          / | \ ")
            print("  |                          /  |  \ ")
            print("  |                             | ")
            print("  |                             | ")
            print("  |                            / \ ")
            print("  |                           /   \ ")
            print("  |                          /     \ ")
            print("  |")
            print("  |")
            print("  |")
            print("-----   ", word, " - ", category)
            input("")
            menuEn(wordlist)

    except ValueError: #Will execute if wordlist gets empty
        print("_________________Erro_________________ \n Já jogaste todas as palavras disponiveis \n Agora podes jogar noutro idioma (1) \n Ou podes adicionar mais palavras ao ficheiro \"words_Pt\" para adicionar palavras ao jogo")
        answer = input("")
        if answer == "1":
            languageselection()

def maingameEn(wordlist):
    try:
        wordnumber = random.randint(1,len(wordlist)-1) #chooses the word
        choosedpair = wordlist[wordnumber]
        wordlist.remove(choosedpair)  #removes the choosed word from future games
        category = choosedpair[0]   #separates the word from the category
        word = choosedpair[1]
        letters = list(word)
        lettersshow = []
        for i in range(0,len(word)):  #creates a list with the same number of spaces as letters of the word
            lettersshow.append(" __")
        guessed = []
        rightguessed = 0
        won = False
        lost = False
        fails = 0
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        while won == False and lost == False: #loop will only run if the player havent lost/won yet
            if fails == 0: #interface if the player failed 0 times
                print("The Hangman game")
                print(" ________________________________ ")
                print("  |    /                        | ")
                print("  |   /                         | ")
                print("  |  /")
                print("  | /")
                print("  |/")
                print("  |  To give up write:")
                print("  |      \"Give up\"")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("-----   ", "".join(lettersshow), " - ", category)

            elif fails == 1: #interface if the player failed 1 time
                print("The Hangman game")
                print(" ________________________________ ")
                print("  |    /                        | ")
                print("  |   /                         | ")
                print("  |  /                        (°_°) ")
                print("  | /")
                print("  |/")
                print("  |  To give up write:")
                print("  |      \"Give up\"")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("-----   ", "".join(lettersshow), " - ", category)

            elif fails == 2: #interface if the player failed 2 times
                print("The Hangman game")
                print(" ________________________________ ")
                print("  |    /                        | ")
                print("  |   /                         | ")
                print("  |  /                        (°_°) ")
                print("  | /                           | ")
                print("  |/                            |")
                print("  |  To give up write:          |")
                print("  |      \"Give up\"              |")
                print("  |                             |")
                print("  |                             |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("-----   ", "".join(lettersshow), " - ", category)

            elif fails == 3: #interface if the player failed 3 times
                print("The Hangman game")
                print(" ________________________________ ")
                print("  |    /                        | ")
                print("  |   /                         | ")
                print("  |  /                        (°_°) ")
                print("  | /                           | ")
                print("  |/                           /|")
                print("  |  To give up write:        / |")
                print("  |      \"Give up\"           /  |")
                print("  |                             | ")
                print("  |                             | ")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("-----   ", "".join(lettersshow), " - ", category)

            elif fails == 4: #interface if the player failed 4 times
                print("The Hangman game")
                print(" ________________________________ ")
                print("  |    /                        | ")
                print("  |   /                         | ")
                print("  |  /                        (°_°) ")
                print("  | /                           | ")
                print("  |/                           /|\ ")
                print("  |  To give up write:        / | \ ")
                print("  |      \"Give up\"           /  |  \ ")
                print("  |                             | ")
                print("  |                             | ")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("  |")
                print("-----   ", "".join(lettersshow), " - ", category)

            elif fails == 5: #interface if the player failed 5 times
                print("The Hangman game")
                print(" ________________________________ ")
                print("  |    /                        | ")
                print("  |   /                         | ")
                print("  |  /                        (°_°) ")
                print("  | /                           | ")
                print("  |/                           /|\ ")
                print("  |  To give up write:        / | \ ")
                print("  |      \"Give up\"           /  |  \ ")
                print("  |                             | ")
                print("  |                             | ")
                print("  |                            /")
                print("  |                           /")
                print("  |                          /")
                print("  |")
                print("  |")
                print("  |")
                print("-----   ", "".join(lettersshow), " - ", category)

            else: #will end the game if the player has more than 5 fails
                lost = True
                break

            guess = input("")

            if guess in guessed: #check if the player repeated some letter
                print("You've already said that letter")

            elif guess == "Give up" or guess == "give up": #gaves up
                print("The Hangman game")
                print(" ________________________________ ")
                print("  |    /                        | ")
                print("  |   /                         | ")
                print("  |  /                        (°_°) ")
                print("  | /                           | ")
                print("  |/                           /|\ ")
                print("  |           You             / | \ ")
                print("  |         Gave Up          /  |  \ ")
                print("  |                             | ")
                print("  |                             | ")
                print("  |                            / \ ")
                print("  |                           /   \ ")
                print("  |                          /     \ ")
                print("  |")
                print("  |")
                print("  |")
                print("-----   ", word, " - ", category)
                input("")
                menuEn(wordlist)

            elif len(guess) != 1: #if is more than one caracter
                print("Invalid Guess: Please write one letter at a time")

            elif guess in ALPHABET: #if player writes in upper case is not valid
                print("Invalid Guess: please use lowercase")

            elif guess not in alphabet: #if it is not a letter is not valid
                print("Invalid Guess")

            else:
                guessed.append(guess) #will add the letter to the listof letters already guessed
                if guess in letters: #if player guesses right will remove that word from the list of remaining letters and add it to the guessed letters
                    while guess in letters:
                        guesslocation = letters.index(guess)
                        del lettersshow[guesslocation]
                        lettersshow.insert(guesslocation,guess)
                        del letters[guesslocation]
                        letters.insert(guesslocation," ")
                        rightguessed = rightguessed + 1

                    if rightguessed == len(word): #sees if player as already guessed all letters
                        won = True

                else:
                    fails = fails + 1
                    if fails >= 6: #if player fail more than 5 times
                        lost = True

        if won == True: #player wins
            print("The Hangman game")
            print(" ________________________________ ")
            print("  |    /                        | ")
            print("  |   /                         | ")
            print("  |  /                        (°_°) ")
            print("  | /                           | ")
            print("  |/                           /|\ ")
            print("  |     Congratulations      / | \ ")
            print("  |         You Won          /  |  \ ")
            print("  |                             | ")
            print("  |                             | ")
            print("  |                            / \ ")
            print("  |                           /   \ ")
            print("  |                          /     \ ")
            print("  |")
            print("  |")
            print("  |")
            print("-----   ", word, " - ", category)
            input("")
            print(wordlist)
            menuEn(wordlist)

        elif lost == True: #player loses
            print("The Hangman game")
            print(" ________________________________ ")
            print("  |    /                        | ")
            print("  |   /                         | ")
            print("  |  /                        (°_°) ")
            print("  | /                           | ")
            print("  |/                           /|\ ")
            print("  |        Game Over          / | \ ")
            print("  |                          /  |  \ ")
            print("  |                             | ")
            print("  |                             | ")
            print("  |                            / \ ")
            print("  |                           /   \ ")
            print("  |                          /     \ ")
            print("  |")
            print("  |")
            print("  |")
            print("-----   ", word, " - ", category)
            input("")
            menuEn(wordlist)

    except ValueError: #Will execute if wordlist gets empty
        print("_________________Error_________________ \n You played all the words available \n You can now play in another language (1) \n Or you can add more words to \"words_En\" to add more words to the game.")
        answer = input("")
        if answer == "1":
            languageselection()

languageselection()
