class TreeInterpreter:
  def __init__(self, ast):
    self.ast = ast

  def interpret(self, ast = None):
    if ast is None:
      ast = self.ast

    op = ast[1]

    if op == '=':
      left = ast[0]
      right = self.interpret(ast[2]) if isinstance(ast[2], list) else ast[2]
      Interpreter.get_memory()[left] = right
    else:
      left = self.interpret(ast[0]) if isinstance(ast[0], list) else ast[0]
      right = self.interpret(ast[2]) if isinstance(ast[2], list) else ast[2]
      return eval(f"{left} {op} {right}")
  
class Interpreter:
  _memory = {}

  def __init__(self, ast):
    self.ast = ast

  @classmethod
  def get_memory(cls):
    return cls._memory

  def interpret(self):
    for tree in self.ast:
      expInterpreter = TreeInterpreter(tree)
      expInterpreter.interpret()
    
    self.show()

  def show(self):
    for key, value in Interpreter.get_memory().items():
      print(f"{key} = {value}")
