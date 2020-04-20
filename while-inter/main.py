from parser.parser_builder import ParserBuilder
g = ParserBuilder().get_parser()
ast = g.parse("x:=3+5")
env = {}
print(ast)
env = ast.execute(env)
print(env)
