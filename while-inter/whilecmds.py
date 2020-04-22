class Cmd:
    def execute(self, env):
        raise NotImplementedError()


class Skip(Cmd):
    def __init__(self):
        pass

    def execute(self, env):
        return env


class Assign(Cmd):
    def __init__(self, variable, expr):
        self.variable = variable
        self.expr = expr

    def execute(self, env):
        env[self.variable.token] = self.expr.eval(env)
        return env


class Compound(Cmd):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def execute(self, env):
        env = self.first.execute(env)
        env = self.second.execute(env)
        return env


class If(Cmd):
    def __init__(self, condition, true_exp, false_exp):
        self.condition = condition
        self.true_exp = true_exp
        self.false_exp = false_exp

    def execute(self,env):
        if self.condition.eval(env):
            return self.true_exp.execute(env)
        else:
            return self.false_exp.execute(env)


class While(Cmd):
    def __init__(self, condition, command):
        self.condition = condition
        self.command = command

    def execute(self, env):
        if self.condition.eval(env):
            env = self.command.execute(env)
            return While(self.condition, self.command).execute(env)
        else:
            return env





