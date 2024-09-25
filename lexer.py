import ply.lex as lex

# List of token names
tokens = (
    'ENJOY', 'MAIN', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 
    'LBRACKET', 'RBRACKET', 'COMMA',  # Add these tokens
    'SEMICOLON', 'PRINT', 'ID', 'NUMBER', 'EQUALS', 
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'TRUE', 'FALSE', 
    'DOT', 'INPUT', 'IF', 'THEN', 'ELSE', 'UNTIL', 
    'FOREVER', 'TOML_START', 'TOML_END', 'OR', 'AND', 'NOT', 
    'STRING', 'IS'
)

# Regular expression rules for simple tokens
t_ENJOY = r'enjoy'
t_MAIN = r'main'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['  # Define left bracket
t_RBRACKET = r'\]'   # Define right bracket
t_COMMA = r','       # Define comma
t_SEMICOLON = r';'
t_PRINT = r'print'
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_TRUE = r'true'
t_FALSE = r'false'
t_DOT = r'\.'
t_INPUT = r'input'
t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
t_UNTIL = r'until'
t_FOREVER = r'forever'
t_TOML_START = r'\{\s*'
t_TOML_END = r'\s*\}'
t_OR = r'or'
t_AND = r'and'
t_IS = 'is'
t_NOT = r'not'
t_STRING = r'\".*?\"'  # Adjust the regex if necessary

# Identifier token
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'ID'    # Check for reserved words
    return t

# Number token
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule for whitespace
t_ignore = ' \t'

# Define a rule for newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
