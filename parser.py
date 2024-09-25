from ply import *
from lexer import *
import ply.yacc as yacc
import toml

# Symbol and function tables
symbol_table = {}
function_table = {}

# Main program structure
def p_program(p):
    '''program : ENJOY MAIN LPAREN RPAREN LBRACE statements RBRACE'''
    p[0] = ('main', p[6])

# Statements handling
def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

# Boolean assignment with `boolean.set`
def p_statement_boolean_assign(p):
    '''statement : ID DOT ID EQUALS boolean SEMICOLON'''
    p[0] = ('boolean_assign', p[1], p[3], p[5])

# Boolean values
def p_boolean(p):
    '''boolean : TRUE
               | FALSE'''
    p[0] = ('boolean', p[1])

# Check the value of a variable using `is`
def p_statement_is(p):
    '''statement : IS ID SEMICOLON'''
    p[0] = ('check_boolean', p[2])

# Printing
def p_statement_print(p):
    '''statement : PRINT LPAREN STRING RPAREN SEMICOLON'''
    p[0] = ('print', p[3])

# Variable assignment
def p_statement_assign(p):
    '''statement : ID EQUALS expression SEMICOLON'''
    p[0] = ('assign', p[1], p[3])

def p_statement_print_var(p):
    '''statement : PRINT LPAREN ID RPAREN SEMICOLON'''
    var_name = p[3]
    if var_name in symbol_table:
        value = symbol_table[var_name]
        print(value)  # Print the value as is
    else:
        print(f"Error: Variable '{var_name}' is not defined")

# Expression rules for basic arithmetic
def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_term(p):
    '''expression : term'''
    p[0] = p[1]

def p_term_binop(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]

def p_factor_num(p):
    '''factor : NUMBER'''
    p[0] = ('num', p[1])

def p_factor_id(p):
    '''factor : ID'''
    p[0] = ('id', p[1])

# IF-ELSE statements
def p_statement_if(p):
    '''statement : IF LPAREN boolean RPAREN LBRACE statements RBRACE else_part'''
    p[0] = ('if_else', p[3], p[6], p[8])

def p_else_part(p):
    '''else_part : ELSE LBRACE statements RBRACE
                 | empty'''
    p[0] = ('else', p[3]) if len(p) == 5 else None

# UNTIL and FOREVER loops
def p_statement_until(p):
    '''statement : UNTIL LPAREN boolean RPAREN LBRACE statements RBRACE'''
    p[0] = ('until', p[3], p[6])

def p_statement_forever(p):
    '''statement : FOREVER LBRACE statements RBRACE'''
    p[0] = ('forever', p[3])

# Arrays
def p_statement_assign_array(p):
    '''statement : ID EQUALS LBRACKET elements RBRACKET SEMICOLON'''
    symbol_table[p[1]] = p[4]  # Assign array elements to the variable in the symbol table
    p[0] = ('assign', p[1], p[4])
    
def p_elements(p):
    '''elements : expression COMMA elements
                | expression COMMA
                | expression'''
    if len(p) == 4:
        p[0] = [p[1]] + p[3]  # Add element to the list
    elif len(p) == 3:
        p[0] = [p[1]]  # Single element followed by a comma
    else:
        p[0] = [p[1]]  # Single element without a comma

def p_expression_array_access(p):
    '''expression : ID LBRACKET expression RBRACKET'''
    arr_name = p[1]
    index = p[3]  # This should be an integer
    
    # Make sure the index is an integer
    if isinstance(index, tuple) and index[0] == 'num':
        index = int(index[1])
    
    if arr_name in symbol_table:
        array = symbol_table[arr_name]
        if isinstance(array, list):
            try:
                p[0] = array[index]  # Access the array at the specified index
            except IndexError:
                print('Index out of bounds')
                p[0] = None
        else:
            print(f"Error: {arr_name} is not an array")
            p[0] = None
    else:
        print(f"Error: Array '{arr_name}' is not defined")
        p[0] = None

def p_expression_array(p):
    '''expression : LBRACKET elements RBRACKET'''
    # Convert from ('num', 1) to just 1
    p[0] = [x[1] if isinstance(x, tuple) and x[0] == 'num' else x for x in p[2]]

# Function handling
def p_function_definition(p):
    '''statement : ENJOY ID LPAREN RPAREN LBRACE statements RBRACE'''
    function_table[p[2]] = p[6]
    p[0] = ('function_def', p[2], p[6])

def p_function_call(p):
    '''statement : ID LPAREN RPAREN SEMICOLON'''
    if p[1] in function_table:
        execute_statements(function_table[p[1]])
    else:
        print(f"Error: Function '{p[1]}' not defined")
    p[0] = ('function_call', p[1])

# Helper function to handle empty productions
def p_empty(p):
    '''empty :'''
    pass

# Helper functions
def execute_statements(statements):
    for statement in statements:
        execute_statement(statement)

def execute_statement(statement):
    stmt_type = statement[0]
    # Handle other statement executions (print, assign, etc.)
    if stmt_type == 'print':
        print(statement[1])

# TOML handling
def p_toml_block(p):
    '''statement : TOML_START toml_content TOML_END'''
    toml_content = p[2]
    parsed_toml = toml.loads(toml_content)
    execute_toml(parsed_toml)

def execute_toml(parsed_toml):
    if "settings" in parsed_toml:
        settings = parsed_toml["settings"]
        name = settings.get("name", "Default Name")
        version = settings.get("version", "1.0")
        debug = settings.get("debug", False)
        print(f"Loaded settings: {name}, Version: {version}, Debug: {debug}")

# Add rule for TOML content extraction
def p_toml_content(p):
    '''toml_content : toml_line toml_content
                    | toml_line'''
    if len(p) == 3:
        p[0] = p[1] + "\n" + p[2]
    else:
        p[0] = p[1]

def p_toml_line(p):
    '''toml_line : ID EQUALS STRING
                 | ID EQUALS boolean'''
    p[0] = f"{p[1]} = {p[3]}"

# Inputs
# INPUT handling
def p_statement_input(p):
    '''statement : ID EQUALS INPUT LPAREN STRING RPAREN SEMICOLON'''
    input_value = input(p[5])  # Get user input with the prompt
    p[0] = ('assign', p[1], input_value)  # Assign the input to the variable

# IF THEN with boolean expressions
def p_statement_if_then(p):
    '''statement : IF boolean THEN statement'''
    if p[2][1] == 'true':
        p[0] = p[4]  # Execute the statement after THEN if the condition is true
    else:
        p[0] = None

# ELSE part
def p_statement_if_then_else(p):
    '''statement : IF boolean THEN statement ELSE statement'''
    if p[2][1] == 'true':
        p[0] = p[4]  # Execute the statement after THEN if true
    else:
        p[0] = p[6]  # Execute the statement after ELSE if false

# Boolean expressions with OR, AND, NOT
def p_boolean_expression(p):
    '''boolean : boolean OR boolean
               | boolean AND boolean
               | NOT boolean'''
    if p[2] == 'OR':
        p[0] = ('or', p[1], p[3])
    elif p[2] == 'AND':
        p[0] = ('and', p[1], p[3])
    elif p[1] == 'NOT':
        p[0] = ('not', p[2])

# Error handling
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build parser
parser = yacc.yacc()

# Sample execution
if __name__ == "__main__":
    while True:
        try:
            s = input('pysnake > ')
        except EOFError:
            break
        if s:
            parser.parse(s)
