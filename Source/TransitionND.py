class TransitionND:
    def __init__(self):
        self.entree=None
        self.sortie=None
        self.char=None

    def buildTransitionND(self,e,s,c):
        self.entree=e
        self.sortie=s
        self.char=c
        return self

    def toString(self):
        return str(self.entree)"->"str(self.char)"->"str(self.sortie)
