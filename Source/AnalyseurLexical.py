import sys, os
from Ligne import  Ligne as ligne
from Etat import  Etat as etat
from Transition import Transition as transition
from Automate import Automate as automate

"""La classe AnalyseurLexical lit les fichiers descr, analyse leur contenu et permet
  de savoir si un fichier est valide ou non.
  Elle permet également de traiter une entrée pour savoir si une elle est acceptée ou non
  Elle contient une méthode permettant l'export du fichier lu en .dot
 """
class AnalyseurLexical:
    def __init__(self,fileName):
        self.LignesListe=[]
        self.automate=None
        self.M="#"
        self.fileName=fileName
        self.analyseurLexical()

    def analyseurLexical(self):
        self.initAnalyser()
    """Lecture du fichier et stockage dans des lignes pour analyse lexicale
    """
    def initAnalyser(self):
        if not os.path.isfile(self.fileName):
            msg = self.fileName+' n"existe pas'
            sys.stderr.write(msg)
            exit(1)

        with open(self.fileName, 'r') as f:
            content = f.readlines()

        for lines in content:
            lines = lines.rstrip()
            self.ajoutLigne(lines)
        self.createAutomate()
        """ 
        Permet de faire un automate
        """
    def createAutomate(self):
        etats=[]
        trans=[]
        voc=[]
        for l in self.LignesListe:
            if l.type=="E":
                for i in range(0,int(l.lexemes[0])):
                    etats.append(etat(i))

            if l.type == "I":
                for lex in l.lexemes:
                    for e in etats:
                        if e.nom==int(lex):
                            e.setIsiniTial(True)

            if l.type == "F":
                existeEntree=False
                for e in etats:
                    if e.isFinal:
                        existeEntree=True

                if not existeEntree:
                    etats[0].setIsiniTial(True)

                for lex in l.lexemes:
                    for e in etats:
                        if int(e.nom) == int(lex):
                            e.setIsFinal(True)

            if l.type=="T":
                entree=None
                sortie=None
                if len(l.lexemes)>3:
                    for e in etats:
                        if e.nom==int(l.lexemes[0]):
                            entree=e
                        if e.nom==int(l.lexemes[2]):
                            sortie=e
                    trans.append(transition().buildTransition(entree,sortie,l.lexemes[1][1],l.lexemes[3][1]))

                else:
                    for e in etats:
                        if e.nom==int(l.lexemes[0]):
                            entree=e
                        if e.nom==int(l.lexemes[2]):
                            sortie=e
                    trans.append(transition().buildTransition3(entree,sortie,l.lexemes[1][1]))

            if l.type=="V":
                for lex in l.lexemes:
                    for c in lex:
                        if c!='"':
                            voc.append(c)

        self.automate= automate(etats,trans).buildAutomate4(etats,trans,voc,self.M)

    """ Traitement d'une entrée dans l'automate
     * Savoir si une entrée est acceptante ou non
     """
    def traitementEntree(self,entree):

        init = self.automate.getInit()
        motsEntree = entree.split("\n")
        for charMot in motsEntree:
            entreeTraitee=False
            courant=init
            phraseSortie=""
            sortie=False
            if charMot !="###":
                mot = charMot
                if mot:
                    if mot[0] not in self.automate.v:
                        print("Erreur : Mot d'entrée non inclu dans le vocabulaire")

                    for tr in self.automate.getTransitions():
                        if tr.etatEntree.nom==init.nom and not entreeTraitee:
                            if tr.entree==mot[0]:
                                entreeTraitee=True
                                courant=tr.etatSortie
                                if tr.sortie!="#":
                                    print("Etat courant : "+  str(init.nom) + ",Entrée : " + str(mot[0]) + ",Sortie : " +str(tr.sortie) + ", Transition trouvée")
                                    phraseSortie=tr.sortie
                                else:
                                    print("Etat courant : " + str(init.nom) + ",Entrée : " + str(mot[0]) + ", Transition trouvée")
                lectureImpossible =False
                for j in range(1,len(mot)):
                    if mot[j] not in self.automate.v:
                        print("Erreur : Mot d'entrée non inclu dans le vocabulaire")

                    transFind=False
                    for t in self.automate.getTransitions():
                        if entreeTraitee and not sortie:
                            if t.etatEntree.nom==courant.nom and t.entree == mot[j] and not transFind:
                                transFind=True
                                if t.sortie!="#":
                                    print("Etat courant : "  +str(courant.nom)+  ",Entrée : "+  str(mot[j]) + ",Sortie : "+ str(t.sortie) + ", Transition trouvée")
                                    phraseSortie=t.sortie
                                else:
                                    print("Etat courant : " + str(courant.nom) +",Entrée : " + str(mot[j]) + ", Transition trouvée")

                                courant=t.etatSortie
                                if j==len(mot)-1 and not sortie:
                                    sortie=True
                                    print("Etat courant : " + str(courant.nom) + " Fin de chaîne")
                                    if courant.isFinal:
                                        print("Entrée acceptante")
                                    else:
                                        print("Entrée non-acceptante")
                                    print("La sortie de cette phrase est : " + phraseSortie)
                        elif not sortie:
                            print("Etat Courant : "+  str(init.nom) +", Entrée : " + str(mot[j])+ ", Aucune transition")

                    if not transFind:
                        lectureImpossible=True
                if lectureImpossible:
                    print("Lecture impossible, l'etat courant n'a pas de transition pour le mot lu")

    """
           fonction qui permet de creer une image d'un automate
    """
    def generatePng(self,fileCheminDot, nom):
        nomImg = "../Output/Dot/Graph/"+str(nom)+".png"
        if os.path.isfile(nomImg):
            cmd = "rm " + nomImg
            os.system(cmd)
            cmd1 = "dot -Tpng " + fileCheminDot + " -o " + nomImg
            os.system(cmd1)
        else:
            cmd = "dot -Tpng " + fileCheminDot+  " -o "  +nomImg
            os.system(cmd)

    """
        faire le fichier .dot pour generer le graph 
    """
    def exportDot(self,nom):

        chemin = "../Output/Dot/"+str(nom)+".dot"
        if not os.path.isfile(chemin):
            f = open(chemin, "a")
        else:
            cmd = "rm " + chemin
            os.system(cmd)
            f = open(chemin, "a")

        f.write("digraph finite_state_machine \n{\n")
        f.write("rankdir=LR;\n")
        f.write("size=\"12\"\n")
        f.write("node [shape = circle];\n")
        for itemI in self.automate.getInitiaux():
            f.write(str(itemI.nom))
            f.write(" [color=blue]\n")
        for e in self.automate.getFinaux():
            f.write(str(e.nom))
            f.write(" [shape=doublecircle];\n")
        for tr in self.automate.transition:
            f.write(str(tr.etatEntree.nom) + " -> ")
            c = tr.sortie
            if c != 0:
                f.write(str(tr.etatSortie.nom) + " [ label = \" " + str(
                    tr.afficheEntrees()) + " / "+  c + " \" ];\n")
            else:
                f.write(str(tr.etatSortie.nom)+  " [ label = \" "  +str(tr.afficheEntrees())+  "\" ];\n")
        f.write("}")
        f.close()
        # generer le graph
        self.generatePng(chemin,nom)

    """
        afficher les lignes d'un automate
    """
    def afficherDescrLigne(self):
        print("-"*50)
        for l in self.LignesListe:
            print(l.toString())
        print("-"*50)

    """
        modifier les liignes d'un automate
    """
    def setLigne(self,b):
        self.LignesListe=b
    """
        ajouter lignes dans un automate
    """
    def ajoutLigne(self,c):
        self.LignesListe.append(ligne(c))
