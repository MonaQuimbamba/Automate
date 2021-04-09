class Ligne:
    def __init__(self,c):
        self.contenu = c
        self.lexemes = []
        self.initLexemes()

    def builLigne1(self):
        self.lexemes=[]

    def initLexemes(self):
        mots = self.contenu.split(" ")
        self.type=mots[0]
        if self.type=="C":
            com=""
            for i in range(1,len(mots)):
                com=mots[i]
            com.replace("'","")
            self.lexemes.append(com)

        elif self.type=="M":
            for i in range(1,len(mots)):
                for j in range(0,len(mots[1])):
                    if mots[i][j]!='\'':
                        self.lexemes.append(mots[i][j])

        elif self.type=="E" or self.type=="I" or self.type=="F":
            for i in range(1,len(mots)):
                self.lexemes.append(mots[i])

        elif self.type=="V" or self.type=="O":
            for i in mots:
                if i not in ["V","O"]:
                    self.lexemes.append(i)

        elif self.type=="T":
            for i in range(1,len(mots)):
                self.lexemes.append(mots[i])

    def setContenu(self,b):
        self.contenu=b

    def setType(self,b):
        self.type=b

    def toString(self):
        s=""
        if self.type=="C":
            s="Ligne Commentaire :"+self.lexemes[0]

        elif self.type=="M":
            s = "Ligne méta-caractère :" + self.lexemes[0]

        elif self.type == "E":
            etats=""
            for str in self.lexemes:
                etats+=str+" "
            s="Etats : "+etats

        elif self.type == "F":
            etatF = ""
            for str in self.lexemes:
                etatF += str  +" "
            if len(self.lexemes)>1:
                s = "Etats finaux: " + etatF
            else:
                s = "Etats final: " + etatF

        elif self.type == "I":
            etatI = ""
            for str in self.lexemes:
                etatI += str + " "
            if len(self.lexemes) > 1:
                s = "Etats Initiaux: " + etatI
            else:
                s = "Etats Initial: " + etatI


        elif self.type == "V":
            vocE = "\""
            for str in self.lexemes:
                vocE += str
            vocE+="\""
            s = "Vocabulaire d'entrée : " + vocE


        elif self.type == "O":
            vocS = "\""
            for str in self.lexemes:
                vocS += str
            vocS+="\""

            s = "Vocabulaire de sortie : " + vocS

        elif self.type == "T":
            if len(self.lexemes)>3:
                tr=self.lexemes[0]+  " " + self.lexemes[1]+  " " + self.lexemes[2] + " " + self.lexemes[3]+  ""
            else:
                tr = self.lexemes[0]+  " " + self.lexemes[1] + " " + self.lexemes[2]

            s= "Transition : " + tr

        return s
