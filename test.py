import parser
from parser import *

data = '''
enjoy main() {
    (?toml):
        [settings]
        name = "PySnake"
        version = "1.0"
        debug = true
    (?/toml);
}

'''

result = parser.parse(data)
print(result)
