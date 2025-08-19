""" Token Types """

INTEGER = 'INTEGER '
PLUS = 'PLUS'
MINUS = 'MINUS'
MULT = 'MULT'
DIV = 'DIV'
EOF = 'EOF'
WHITESPACE = 'WHITESPACE'

class Token : 
    def __init__(self, type, value): 
        self.type = type
        self.value = value
    
    def __str__(self): 
        return f"Token({self.type}, {self.value})"
    
    def __repr__(self):
        return self.__str__()

class Interpreter :
    def __init__(self, text): 
        self.text = text 
        self.pos = 0
        self.current_token=None # object Token()
        
    def error(self): 
        raise Exception("Error in parsing the input")
    
    def integer(self):
        """parse the multi-digit integer"""
        result = ''
        text = self.text
        
        while self.pos < len(text) and text[self.pos].isdigit():
            result += text[self.pos]
            self.pos += 1
        return int(result)
    
    def get_next_token(self):
        text = self.text 
        
        while self.pos < len(self.text): 
            
            if text[self.pos].isspace():
                while self.pos < len(text) and text[self.pos] == ' ': 
                    self.pos += 1 
                continue
            
            if text[self.pos].isdigit():
                token = Token(INTEGER, self.integer())
                return token 
            
            if text[self.pos] == '+': 
                self.pos += 1
                token = Token(PLUS, '+')
                return token
            
            if text[self.pos] == '-':
                self.pos += 1
                token = Token(MINUS, '-')
                return token 
            
            if text[self.pos] == '*':
                self.pos += 1
                token = Token(MULT, '*')
                return token 
            
            if text[self.pos] == '/':
                self.pos += 1
                token = Token(DIV, '/')
                return token 
            
            self.error() # otherwise 
        return Token(EOF, None)
    
    def eat(self, token_type): 
        """
        compare the current token type with the passed token type and 
        if they match then "eat" the current token and assign the next 
        token to the self.current_token, otherwise raise an exception 
        """
        if self.current_token.type == token_type: 
            self.current_token = self.get_next_token()
        else: 
            self.error()
        
    def expr(self):  
        self.current_token = self.get_next_token()
        result = self.current_token.value
        self.eat(INTEGER)
        
        while self.current_token.type in (PLUS, MINUS, MULT, DIV): 
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result += self.current_token.value
            elif token.type == MINUS:
                self.eat(MINUS)
                result -= self.current_token.value
            elif token.type == MULT:
                self.eat(MULT)
                result *= self.current_token.value
            elif token.type == DIV: 
                self.eat(DIV)
                result /= self.current_token.value
            self.eat(INTEGER)
        
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
        
if __name__ == "__main__": 
    main()
        
        