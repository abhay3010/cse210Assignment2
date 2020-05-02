from builder import ParserBuilder
import sys

from whilecmds import Skip


def get_env_str(env):
    response = []
    for key in sorted(env.keys()):
        response.append("{0} → {1}".format(key, env[key]))
    response_str = "{"+", ".join(response) + "}"
    return response_str




def main():
    g = ParserBuilder(debug=False).get_parser()
    for line in sys.stdin:
        env = {}
        ast = g.parse(line)
        iterations  = 10000
        print ("original ast,",ast)
        while not isinstance(ast, Skip) and iterations > 0:
            ast, env = ast.execute(env)
            print ("→ ", ast, get_env_str(env))
            iterations-=1





if __name__ == "__main__":
    main()
