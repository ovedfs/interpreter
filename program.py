import sys
from lib.interpreter import Interpreter
from lib.lexer import Lexer
from lib.parse import Parser

code = sys.argv[1]

try:
	lexer = Lexer(code)
	tokens = lexer.tokenize()
	print(tokens)
	
	parser = Parser(tokens)
	ast = parser.parse()
	# print(ast)
	
	interpreter = Interpreter(ast)
	interpreter.interpret()
except Exception as e:
	print(e)
