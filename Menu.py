import lexicalanalyzer

while(True):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|| Menu for Lexical Analyzer ||")
    print("1- Lex() function caller")
    print("2- Show Symbol Table")
    print("3- Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    userinput = int(input("Please choose from menu 1 to 3: "))

    if userinput == 1:

        lexical = lexicalanalyzer.Lexer()
        lexical.Lex()
        continue

    elif userinput == 2:
        lexical = lexicalanalyzer.Lexer()
        lexical.showingsymboltable()
        continue

    elif userinput == 3:
        break
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Please choose a valid number from menu 1 to 3")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
