from .expr import Expr
class BoolVal(Expr):
    def __init__(self, val):
        self.val = val

    def eval(self,environment):
        return environment,self.val


class Equality(Expr):

    def __init__(self,lexp,rexp):
        self.lexp = lexp
        self.rexp = rexp

    def eval(self,environment):
        environment, lval = self.lexp.eval(environment)
        environment, rval = self.rexp.eval(environment)
        return environment, lval == rval



class LessThan(Expr):

    def __init__(self,lexp,rexp):
        self.lexp = lexp
        self.rexp = rexp

    def eval(self,environment):
        environment, lval = self.lexp.eval(environment)
        environment, rval = self.rexp.eval(environment)
        return environment, lval < rval


class Not(Expr):

    def __init__(self, boolexp):
        self.boolexp = boolexp

    def eval(self,environment):
        environment, response = self.boolexp.eval(environment)
        return environment, not response


class And(Expr):

    def __init__(self, lboolexp, rboolexp):
        self.lexp = lboolexp
        self.rexp = rboolexp

    def eval(self, environment):
        environment, lval = self.lexp.eval(environment)
        environment, rval = self.rexp.eval(environment)
        return environment, lval and rval


class Or(Expr):

    def __init__(self, lboolexp, rboolexp):
        self.lexp = lboolexp
        self.rexp = rboolexp

    def eval(self, environment):
        environment, lval = self.lexp.eval(environment)
        environment, rval = self.rexp.eval(environment)
        return environment, lval or rval






