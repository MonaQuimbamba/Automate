class Transition:
    def __init__(self):
        self.etatEntree=None
        self.etatSortie=None
        self.entree=None
        self.sortie=None

    def buildTransition(self,etatE,etatS,e,s):
        self.etatEntree=etatE
        self.etatSortie=etatS
        self.entree=e
        self.sortie=s
        return self

    def buildTransition1(self,etatE,etatS):
        self.etatEntree=etatE
        self.etatSortie=etatS
        return self

    def buildTransition3(self,etatE,etatS,e):
        self.etatEntree = etatE
        self.etatSortie = etatS
        self.entree = e
        self.sortie = ''
        return self

    def setEtatEntree(self,b):
        self.etatEntree=b

    def setEtatSortie(self,b):
        self.etatSortie=b

    def setEntree(self,b):
        self.entree=b

    def setSortie(self,b):
        self.sortie=b

    def afficheEntrees(self):
        res = ""
        for i in range(0, len(self.entree)):
            res = res + self.entree[i]
            if i != len(self.entree) - 1:
                res = res + ";"
        return res

    def getEtatSortie(self):
        return self.etatSortie
