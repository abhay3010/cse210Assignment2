from expr import Expr


class BoolVal(Expr):
    def __init__(self, val):
        self.val = val

    def eval(self, environment):
        return self.val

    def __repr__ (self):
        if self.val:
            return "true"
        else:
            return "false"


class Equality(Expr):

    def __init__(self,lexp,rexp):
        self.lexp = lexp
        self.rexp = rexp

    def eval(self,environment):
        lval = self.lexp.eval(environment)
        rval = self.rexp.eval(environment)
        return lval == rval

    def __repr__(self):
        return "({0}={1})".format(self.lexp, self.rexp)




class LessThan(Expr):

    def __init__(self,lexp,rexp):
        self.lexp = lexp
        self.rexp = rexp

    def eval(self,environment):
        lval = self.lexp.eval(environment)
        rval = self.rexp.eval(environment)
        return lval < rval

    def __repr__(self):
        return "({0}<{1})".format(self.lexp, self.rexp)


class Not(Expr):

    def __init__(self, boolexp):
        self.boolexp = boolexp

    def eval(self,environment):
        response = self.boolexp.eval(environment)
        return not response

    def __repr__(self):
        return "¬" + self.boolexp.__repr__()


class And(Expr):

    def __init__(self, lboolexp, rboolexp):
        self.lexp = lboolexp
        self.rexp = rboolexp

    def eval(self, environment):
        lval = self.lexp.eval(environment)
        rval = self.rexp.eval(environment)
        return lval and rval

    def __repr__(self):
        return "({0}∧{1})".format(self.lexp,self.rexp)

class Or(Expr):

    def __init__(self, lboolexp, rboolexp):
        self.lexp = lboolexp
        self.rexp = rboolexp

    def eval(self, environment):
        lval = self.lexp.eval(environment)
        rval = self.rexp.eval(environment)
        return lval or rval

    def __repr__(self):
        return "({0}∨{1})".format(self.lexp, self.rexp)







