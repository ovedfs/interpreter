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
		tokens_line = []
		i = 0
		length = len(line)
		while i < length:
			char = line[i]
			if char.isdigit() or (char == '.' and (i + 1 < length and line[i + 1].isdigit())):
				number, isFloat = self.extract_number(line, i)
				tokens_line.append(Float(number, num_line, i) if isFloat else Integer(number, num_line, i))
				i += len(number) - 1
			elif char in '+-*/()':
				tokens_line.append(Operation(char, num_line, i))
			elif char == '=':
				tokens_line.append(Assign(num_line, i))
			elif re.match(r'[a-z_]', char):
				name, column = self.extract_variable(line, i)
				tokens_line.append(Variable(name, num_line, column))
				i += len(name) - 1
			i += 1

		return tokens_line

	def extract_number(self, line, i):
		number = ''
		length = len(line)
		isFloat = False
		while i < length and (line[i].isdigit() or (line[i] == '.' and not isFloat)):
			if line[i] == '.':
				isFloat = True
			number += line[i]
			i += 1
		return number, isFloat

	def extract_variable(self, line, i):
		name = line[i]
		length = len(line)
		column = i
		i += 1
		while i < length and re.match(r'[a-z0-9_]', line[i]):
			name += line[i]
			i += 1
		return name, column