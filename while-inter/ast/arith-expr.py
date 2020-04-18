from .expr import Expr


class AddExpr(Expr):
    def __init__(self, left,right):
        self.left = left
        self.right = right

    def eval(self, environment):
        environment, lval = self.left.eval(environment)
        environment, rval = self.right.eval(environment)
        return environment, lval + rval


class SubExpr(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, environment):
        environment, lval = self.left.eval(environment)
        environment, rval = self.right.eval(environment)
        return environment, lval - rval


class MulExp(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, environment):
        environment, lval = self.left.eval(environment)
        environment, rval = self.right.eval(environment)
        return environment, lval * rval


class NumExpr(Expr):
    def __init__(self, val):
        self.val = val

    def eval(self,environment):
        return environment, self.val


class VarExp(Expr):
    def __init__(self,token):
        self.token = token

    def eval(self, environment):
        return environment, environment.getordefault(self.token, 0)











