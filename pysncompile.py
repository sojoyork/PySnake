import sys
from parser import *
import py_compile
import os


print("""
************************************
** Americanboi, PySnake compiler  **
** PySnake Licence                **
************************************
""")
# Function to generate Python code from the parsed AST
# Convert AST to Python code (customize as necessary)
# This is a simple example; modify as per your actual AST structure
# Function to generate Python code from the parsed statements
# Function to generate Python code from the parsed statements
# Function to generate Python code from the parsed AST
def generate_python_code(ast):
    # Convert AST to Python code (customize as necessary)
    # This is a simple example; modify as per your actual AST structure
    python_code = str(ast)
    return f"outputvars = {python_code}\nprint(outputvars)\n"

# Function to convert the .pysn file into a .py file
def convert_pysn_to_py(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.read()

    # Parse the PySnake code into AST using the parser
    result = parser.parse(data)

    # Generate Python code from the AST
    python_code = generate_python_code(result)

    # Write the Python code to the output .py file
    with open(output_file, 'w') as file:
        file.write(python_code)

    print(f"Converted {input_file} to {output_file}")

# Function to compile .py to .pyc and place in output folder
def compile_to_pyc(py_file, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    compiled_path = os.path.join(output_folder, os.path.basename(py_file) + "c")
    
    py_compile.compile(py_file, cfile=compiled_path)
    print(f"Compiled {py_file} to {compiled_path}")

# Command-line interface
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python pysn_compiler.py <input file>.pysn <output py file>.py <output folder>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_py_file = sys.argv[2]
    output_folder = sys.argv[3]

    # Convert .pysn to .py
    convert_pysn_to_py(input_file, output_py_file)

    # Compile .py to .pyc in the specified output folder
    compile_to_pyc(output_py_file, output_folder)
