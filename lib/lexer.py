import re
from lib.Tokens import Token, Integer, Float, Operation, Assign, Variable

class Lexer:
	def __init__(self, code):
		self.code = code
		self.tokens = []

	def __repr__(self):
		return "\n".join([repr(item) for item in Token.tokens]) or ""

	def tokenize(self):
		with open(self.code, 'r') as file:
			for num_line, line in enumerate(file):
				tokens_line = self.tokenize_line(line, num_line)
				self.tokens.append(tokens_line)
				
		return self.tokens
	
	def tokenize_line(self, line, num_line):
		i = 0
		tokens_line = []
		while i < len(line):
			# Numbers
			if line[i] in '0123456789':
				number = ''
				isFloat = False
				column = i
				while i < len(line) and line[i] in '0123456789.':
					if line[i] == '.':
						isFloat = True
					number += line[i]
					i += 1

				if not isFloat:
					tokens_line.append(Integer(number, num_line, column))
				else:
					tokens_line.append(Float(number, num_line, column))
			# Operators and Parentheses
			elif line[i] in '+-*/()':
				tokens_line.append(Operation(line[i], num_line, i))
			# Assign operator
			elif line[i] == '=':
				tokens_line.append(Assign(num_line, i))
			# Variables
			elif re.match(r'[a-z_]', line[i]):
				name = line[i]
				column = i
				i += 1
				while i < len(line) and re.match(r'[a-z0-9_]', line[i]):
					name += line[i]
					i += 1
				tokens_line.append(Variable(name, num_line, column))
			i += 1
			
		return tokens_line