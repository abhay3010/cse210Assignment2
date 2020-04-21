from parglare import Grammar,Parser
from ast.cmd import *
from ast.arithexpr import  *
from ast.boolexp import *
grammar = """
cmd : skip 
    | cmd ";" cmd {left, 1}
    | "if" bool "then" cmd "else" cmd
    | variable ":=" exp
    | "while" bool "do" cmd {left, 4 }
    | "{" cmd "}" ;
exp: number
    | variable
    | exp "+" exp {left, 2}
    | exp "-" exp {left, 2}
    | exp "*" exp {left, 3} 
    | "(" exp ")" 
    | bool "?" exp ":" exp {right, 1};
    
bool: true
    | false
    | exp "=" exp {left,2}
    | exp "<" exp  {left,2}
    | "¬"  bool
    | bool "∧" bool {left,2}
    | bool "∨" bool {left,2}
    | "(" bool ")" ;
terminals
number: /[-]?\d+/;
variable: /[a-zA-Z_][_a-zA-Z0-9]*/;
skip: "skip";
true:  "true";
false: "false";
"""
actions = {
    "cmd":[ lambda _,cmd : Skip(),
            lambda _, cmd : Compound(cmd[0],cmd[2]),
            lambda _, cmd : If(cmd[1], cmd[3], cmd[5]),
            lambda _, cmd : Assign(cmd[0], cmd[2]),
            lambda _, cmd : While(cmd[1], cmd[3]),
            lambda _, cmd : cmd[1]

        ],
    "bool": [lambda _, match: match[0],
             lambda _, match: match[0],
             lambda _, exp: Equality(exp[0], exp[2]),
             lambda _, exp: LessThan(exp[0], exp[2]),
             lambda _, exp: Not(exp[1]),
             lambda _, bool : And(bool[0], bool[2]),
             lambda _, bool : Or(bool[0], bool[2]),
             lambda _, cmd : cmd[1]

             ],
    "exp": [
        lambda _, value : value[0],
        lambda _, value : value[0],
        lambda _, exp : AddExpr(exp[0], exp[2]),
        lambda _, exp : SubExpr(exp[0], exp[2]),
        lambda _, exp : MulExp(exp[0], exp[2]),
        lambda _, exp : exp[1],
        lambda _, exp : TernaryExp(exp[0], exp[2], exp[4])
        ],
    "number": lambda _, value: NumExpr(int(value)),
    "true": lambda _, value : BoolVal(True),
    "false": lambda _, value : BoolVal(False),
    "skip": lambda _, value: value,
    "variable": lambda _, value: VarExp(value),
    }


class ParserBuilder:

    def __init__(self, debug=False):
        self.grammar = grammar
        self.actions = actions
        self.debug = debug

    def get_parser(self):
        g = Grammar.from_string(self.grammar,debug=self.debug,debug_colors=self.debug)
        return Parser(g, debug=self.debug, actions=self.actions, debug_colors=self.debug)






