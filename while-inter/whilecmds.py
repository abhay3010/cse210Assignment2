class Cmd:
    def execute(self, env):
        raise NotImplementedError()


class Skip(Cmd):
    def __init__(self):
        pass

    def execute(self, env):
        return None, env

    def __repr__(self):
        return "skip"


class Assign(Cmd):
    def __init__(self, variable, expr):
        self.variable = variable
        self.expr = expr

    def execute(self, env):
        env[self.variable.token] = self.expr.eval(env)
        return Skip(), env

    def __repr__(self):
        return self.variable.__repr__() +  " := "+ self.expr.__repr__()


class Compound(Cmd):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def execute(self, env):
        if isinstance(self.first, Skip):
            return self.second, env
        else:
            remaining,env  = self.first.execute(env)
            return Compound(remaining,self.second), env



class If(Cmd):
    def __init__(self, condition, true_exp, false_exp):
        self.condition = condition
        self.true_exp = true_exp
        self.false_exp = false_exp

    def execute(self,env):
        if self.condition.eval(env):
            return self.true_exp, env
        else:
            return self.false_exp, env


class While(Cmd):
    def __init__(self, condition, command):
        self.condition = condition
        self.command = command

    def execute(self, env):
        if self.condition.eval(env):
           return Compound(self.command, While(self.condition, self.command)), env
        else:
            return Skip(), env





