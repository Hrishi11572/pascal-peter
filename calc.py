# the parts of a statement = tokens 

# token types = INT, PLUS, EOF (end of file)

INTEGER = 'INTEGER '
PLUS = 'PLUS'
EOF = 'EOF'

# Defining the Token class here 

class Token: 
    def __init__ (self, type, value): 
        # token type : INTEGER, PLUS, EOF 
        self.type = type 
        # token value : 0-9, +, None (as of now)
        self.value = value 
    
    def __str__(self): 
        '''
        This is how we represent the instance of our 
        Token class 
        
        eg. 
            Token(INTEGER, 3)
            Token(PLUS, '+')
        '''
        return f"Token({self.type}, {self.value})"
    
    def __repr__(self): 
        return self.__str__() # calling the above method
        

# defining the Interpreter calss here 

class Interpreter : 
    
    def __init__(self, text): 
        # client string input eg. "3+5"
        self.text = text 
        self.pos = 0 # self.pos is the index on self.text 
        self.current_token = None # current token instance 
    
    def error(self): 
        raise Exception("Error in parsing the input")
    
    def get_next_token(self): 
        '''
        This is the Lexical analyser or lexer or tokenizer 
        this method breaks a sentence apart into tokens, One token at a time 
        '''
        text = self.text  # the sentence 
        
        if self.pos > len(text) - 1: 
            return Token(EOF, None) 
        
        current_char = text[self.pos]
        
        if current_char.isdigit(): 
            token = Token(INTEGER, int(current_char))
            self.pos += 1 
            return token
        
        if current_char == '+': 
            token = Token(PLUS, current_char)
            self.pos += 1
            return token 
        
        self.error() # otherwise something is wrong 
    
    def eat(self, token_type): 
        # compare the current token type with the passed token type and if they match then "eat" the current token and assign the next token to the self.current_token, otherwise raise an exception 
        
        if self.current_token.type == token_type: 
            self.current_token = self.get_next_token()
        else: 
            self.error()
    
    def expr(self): 
        # evaluate : INTEGER PLUS INTEGER
        # set current token to the first token taken from the input 
        self.current_token = self.get_next_token()
        
        # for now the current_token is a single digit int
        left = self.current_token
        self.eat(INTEGER)
        
        # the next token should be a plus sign 
        op = self.current_token
        self.eat(PLUS)
        
        # ideally the next token should be a single digit int 
        right = self.current_token
        self.eat(INTEGER)
        
        # after the above call the self.current_taken = EOF 
        result = left.value + right.value 
        return result 
    

def main(): 
    while True: 
        try: 
            text = input('>> ')
        except EOFError: 
            break
        
        if not text: 
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__': 
    main()        
        