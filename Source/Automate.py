class Automate:
    def __init__(self,e,t):
        self.etats=e
        self.transition=t
        self.v=None
        self.M=None
    def buildAutomate2(self,e):
        self.etats=e
        return self

    def buildAutomate3(self,e,t,v):
        self.etats=e
        self.transition=t
        self.v=v
        return self

    def buildAutomate4(self,e,t,v,m):
        self.etats = e
        self.transition = t
        self.v = v
        self.M=m
        return self

    def getInitiaux(self):
        res=[]
        for e in self.etats:
            if e.isInitial:
                res.append(e)
        return res

    def getFinaux(self):
        res=[]
        for e in self.etats:
            if e.isFinal:
                res.append(e)
        return res

    def getInit(self):
        res=None
        for e in self.etats:
            if e.isInitial:
                res=e
        return res

    def getTransitions(self):
        return self.transition
    def getVoc(self):
        return self.v
