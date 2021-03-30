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
        return self.afficherEnsEtat(self.entree)+"->"+str(self.char)+"->"+self.afficherEnsEtat(self.sortie)

    def afficherEnsEtat(self,etat):
        res="["
        for e in etat:
            res+=str(e.nom)+" "
        res+="]"
        return res