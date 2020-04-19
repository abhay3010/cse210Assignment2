class Cmd:
    def execute(self,env):
        raise NotImplementedError()


class Skip(Cmd):
    def __init__(self):

    def execute(self,env):
        return env

class AssignExpr(Cmd):
    def __init__(self, variable, expr):
        self.variable = variable
        self.expr = expr

    def execute(self,env):
        env[self.varialbe.eval()] = self.expr.eval()
        return env

