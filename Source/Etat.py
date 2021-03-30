class Etat:
    def __init__(self,nom):
        self.nom=nom
        self.isInitial=None
        self.isFinal=None

    def builEtat1(self,nom,init,fin):
        self.nom=nom
        self.isInitial=init
        self.isFinal=fin
        return self

    def setNom(self,b):
        self.nom=b

    def setIsiniTial(self,b):
        self.isInitial=b

    def setIsFinal(self,b):
        self.isFinal=b

    def stringEtat(self):
        return " " +str(self.nom)
