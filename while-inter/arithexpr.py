from expr import Expr


class AddExpr(Expr):
    def __init__(self, left,right):
        self.left = left
        self.right = right

    def eval(self, environment):
        lval = self.left.eval(environment)
        rval = self.right.eval(environment)
        return lval + rval


class SubExpr(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, environment):
        lval = self.left.eval(environment)
        rval = self.right.eval(environment)
        return lval - rval


class MulExp(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, environment):
        lval = self.left.eval(environment)
        rval = self.right.eval(environment)
        return lval * rval


class NumExpr(Expr):
    def __init__(self, val):
        self.val = val

    def eval(self, environment):
        return self.val


class VarExp(Expr):
    def __init__(self, token):
        self.token = token

    def eval(self, environment):
        return environment.get(self.token, 0)


class TernaryExp(Expr):

    def __init__(self, bool, exp1, exp2):
        self.bool = bool
        self.exp1 = exp1
        self.exp2 = exp2

    def eval(self,environment):
        if self.bool.eval(environment):
            return self.exp1.eval(environment)
        else:
            return self.exp2.eval(environment)















