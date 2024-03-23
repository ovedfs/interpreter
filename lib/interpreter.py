class TreeInterpreter:
  def __init__(self, ast):
    self.ast = ast

  def interpret(self, ast = None):
    if ast is None:
      ast = self.ast

    left = self.interpret(ast[0]) if isinstance(ast[0], list) else ast[0]
    op = ast[1]
    right = self.interpret(ast[2]) if isinstance(ast[2], list) else ast[2]

    return eval(f"{left} {op} {right}")
  
class Interpreter:
  def __init__(self, ast):
    self.ast = ast

  def interpret(self):
    for tree in self.ast:
      expInterpreter = TreeInterpreter(tree)
      print(expInterpreter.interpret())
