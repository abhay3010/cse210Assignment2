from parser.builder import ParserBuilder
import sys
def print_env(env):
    response = []
    for key in sorted(env.keys()):
        response.append("{0} → {1}".format(key, env[key]))
    response_str = "{"+", ".join(response) + "}"
    print(response_str)



def main():
    g = ParserBuilder(debug=False).get_parser()
    for line in sys.stdin:
        env = {}
        ast = g.parse(line)
        #print(ast)
        env = ast.execute(env)
        print_env(env)

if __name__ == "__main__":
    main()
