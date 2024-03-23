from lib.Tokens import Float, Integer

class ExpressionParser:
  def __init__(self, tokens):
    self.tokens = tokens
    self.index = 0
    self.token = self.tokens[self.index]

  def parse(self):
    return self.expression()

  def expression(self):
    left = self.term()
    while self.token.value == '+' or self.token.value == '-':
      op = self.token.value
      self.next()
      right = self.term()
      left = [left, op, right]
    return left

  def term(self):
    left = self.factor()
    self.next()
    while self.token.value == '*' or self.token.value == '/':
      op = self.token.value
      self.next()
      right = self.factor()
      self.next()
      left = [left, op, right]

    return left
      
  def factor(self):
    if type(self.token) == Integer or type(self.token) == Float:
      return self.token.value
    elif self.token.value == '(':
      self.next()
      return self.expression()
    
  def next(self):
    self.index += 1
    if self.index < len(self.tokens):
      self.token = self.tokens[self.index]
  
class Parser:
  def __init__(self, tokens):
    self.tokens = tokens
    self.ast = []

  def parse(self):
    for line in self.tokens:
      lineParser = ExpressionParser(line)
      self.ast.append(lineParser.parse())
    
    return self.ast