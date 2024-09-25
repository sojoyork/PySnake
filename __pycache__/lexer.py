import ply.lex as lex

# List of token names
tokens = (
    'ENJOY', 'MAIN', 'PRINT', 'STRING', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN',
    'ID', 'EQUALS', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'SEMICOLON'
)

# Regular expression rules for simple tokens
t_ENJOY = r'enjoy'
t_MAIN = r'main'
t_PRINT = r'print'
t_STRING = r'\".*?\"'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_SEMICOLON = r';'


# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Newline handling
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Identifier token
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Number token
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer
data = '''
enjoy main() {
    x = 10 + 20;
    print("Hello world");
}
'''

lexer.input(data)
for tok in lexer:
    print(tok)
