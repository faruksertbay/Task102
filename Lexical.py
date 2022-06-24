import re

class Buffer:
    def load_buffer(self):
        fileContent = open('test.txt', 'r') #Dosyayı okuduk
        text = fileContent.readline() #readline ile satırı textin içine attık

        buffer = [] #Yeni dizi oluşturduk
        count = 1

        while text != "": #text boş olana kadar döngüyü döndür
            buffer.append(text) #dosyadan okuduğumuz data yı arraye attık
            text = fileContent.readline() #eğer birden fazla satır varsa okumaya devam et.
            count += 1

            if count == 10 or text == '': #txt içinde data bittiyse içeri gir
                buf = ''.join(buffer) #bütün indexleri boşluksuz birleştirdik
                count = 1
                yield buf #arrayi döndürdük

                buffer = [] # arrayin içini boşalttık
        fileContent.close()

class LexicalAnalyzer:
    # Token row
    lin_num = 1
    def tokenize(self, code):
        rules = [
            ('ERROR', r'\d+[a-zA-Z]+'),
            ('IF', r'if'),              
            ('ELSE', r'else'),          
            ('WHILE', r'while'),        
            ('FOR', r'for'),            
            ('LOGICAL_OR', r'\|\|'),            
            ('LOGICAL_AND', r'&&'),           
            ('BITWISE_OR', r'\|'),           
            ('BITWISE_AND', r'&'),            
            ('FLOAT', r'\d(\d)*\.\d(\d)*'),   
            ('INTEGER', r'-?\d(\d)*'),        
            ('ID', r'[a-zA-Z]\w*'),     
        ]

        tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)
        
        # Lists of output for the program
        token = []
        lexeme = []

        # It analyzes the code to find the lexemes and their respective Tokens
        for m in re.finditer(tokens_join, code):
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)

            if token_type == 'ERROR':
                token.append(token_type)
                lexeme.append(token_lexeme)
                print('<token={0}, unrecognized_string={1}>'.format(token_type,token_lexeme))
            elif token_type == 'INTEGER':
                token.append(token_type)
                lexeme.append(token_lexeme)
                print('<token={0}, integer_value={1}>'.format(token_type,token_lexeme))
            elif token_type == 'FLOAT':
                token.append(token_type)
                lexeme.append(token_lexeme)
                print('<token={0}, float_value={1}>'.format(token_type,token_lexeme))
            elif token_type == 'ID':
                token.append(token_type)
                lexeme.append(token_lexeme)
                print('<token={0}, index={1}>'.format(token_type,token_lexeme))
            else:
                token.append(token_type)
                lexeme.append(token_lexeme)
                print('<token={0}>'.format(token_type))

        return token, lexeme

if True:
    Buffer = Buffer()
    Analyzer = LexicalAnalyzer()
    # Lists for every list returned list from the function tokenize
    token = []
    lexeme = []
    row = []
    column = []

    while True: #main menu list
        print("1.Call lex()")
        print("2.Show Symbol table")
        print("3.Exit")
        print("----------------------------------------------------------------")

        choice = int(input("Enter: ")) 
        # Tokenize and reload of the buffer
        if choice == 1:
             for i in Buffer.load_buffer():
                t, lex = Analyzer.tokenize(i)
                token += t
                lexeme += lex
        elif choice == 2:
           print('\nRecognize Tokens: ', token)

        elif choice == 3:
            break