import sys, os
from Source.Ligne import  Ligne as ligne
from Source.Etat import  Etat as etat
from Source.Transition import Transition as transition
from Source.Automate import Automate as automate

"""La classe AnalyseurLexical lit les fichiers descr, analyse leur contenu et permet
 * de savoir si un fichier est valide ou non.
 * Elle permet également de traiter une entrée pour savoir si une elle est acceptée ou non
 * Elle contient une méthode permettant l'export du fichier lu en .dot
 """
class AnalyseurLexical:
    def __init__(self,fileName):
        self.LignesListe=[]
        self.automate=None
        self.M=""
        self.fileName=fileName
        self.analyseurLexical()

    def analyseurLexical(self):
        self.initAnalyser()
    """Lecture du fichier et stockage dans des lignes pour analyse lexicale
    """
    def initAnalyser(self):
        if not os.path.isfile(self.fileName):
            msg = self.fileName' n"existe pas'
            sys.stderr.write(msg)
            exit(1)

        with open(self.fileName, 'r') as f:
            content = f.readlines()

        for lines in content:
            lines = lines.rstrip()
            self.ajoutLigne(lines)

        if self.analyseLexicaleBool():
            self.createAutomate()

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


    def analyseLexicaleBool(self):
        print(" dans automate")
        self.M="#"
        """for l in self.LignesListe:
            if l.type=="C":
                pass
            if l.type=="M":
                self.M=l.lexemes[0]
                if len(l.lexemes)!=1:
                    print("erreur ,dans le meta")
                    return False

            if l.type=="V":
                ligneV=l
                if self.M not in ligneV.lexemes:
                    ligneV.lexemes.append(self.M)
                v=True

            if l.type =="T":
                if(len(l.lexemes)<3 or len(l.lexemes)>4):
                    print("erreur : La transition comporte 3 ou 4 elements, ligne ")
                    return False

                if l.lexemes[1].replace("'", "") not in ligneV.lexemes:
                    print("Erreur : Mot inconnu V, ligne ")
                    return False

                if len(l.lexemes)>3:
                    if ligneO==None:
                        ligneO=ligne()
                        ligneO.lexemes.append(self.M)
                    if l.lexemes[3].replace("'", "") not in ligneO and l.lexemes[3].replace("'", "")!=self.M:
                        print("Erreur : Mot inconnu O, ligne ")
                        return False"""

        return True
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
                                    print("Etat courant : "  str(init.nom)  ",Entrée : "  str(mot[0])  ",Sortie : " str(tr.sortie)  ", Transition trouvée")
                                    phraseSortie=tr.sortie
                                else:
                                    print("Etat courant : "  str(init.nom)  ",Entrée : "  str(mot[0])  ", Transition trouvée")
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
                                    print("Etat courant : "  str(courant.nom)  ",Entrée : "  str(mot[j])  ",Sortie : " str(t.sortie)  ", Transition trouvée")
                                    phraseSortie=t.sortie
                                else:
                                    print("Etat courant : "  str(courant.nom) ",Entrée : "  str(mot[j])  ", Transition trouvée")

                                courant=t.etatSortie
                                if j==len(mot)-1 and not sortie:
                                    sortie=True
                                    print("Etat courant : "  str(courant.nom)  " Fin de chaîne")
                                    if courant.isFinal:
                                        print("Entrée acceptante")
                                    else:
                                        print("Entrée non-acceptante")
                                    print("La sortie de cette phrase est : "  phraseSortie)
                        elif not sortie:
                            print("Etat Courant : "  str(init.nom) ", Entrée : "  str(mot[j]) ", Aucune transition")

                    if not transFind:
                        lectureImpossible=True
                if lectureImpossible:
                    print("Lecture impossible, l'etat courant n'a pas de transition pour le mot lu")

    """
           fonction qui permet de creer une image d'un automate
    """
    def generatePng(self, fileCheminDot, nom):
        nomImg = "Output/Dot/Graph/"  nom  ".png"
        if os.path.isfile(nomImg):
            cmd = "rm "  nomImg
            os.system(cmd)
            cmd1 = "dot -Tpng "  fileCheminDot  " -o "  nomImg
            os.system(cmd1)
        else:
            cmd = "dot -Tpng "  fileCheminDot  " -o "  nomImg
            os.system(cmd)

    def exportDot(self,nom):
        chemin = "Output/Dot/"

        if nom != None:
            tmp = ''.join(e for e in nom if e.isalnum())
            chemin = tmp  ".dot"
        else:
            chemin = "no_name.dot"

        if not os.path.isfile(chemin):
            f = open(chemin, "a")
        else:
            cmd = "rm "  chemin
            os.system(cmd)
            f = open(chemin, "a")

        f.write("digraph finite_state_machine \n{\n")
        f.write("rankdir=LR;\n")
        f.write("size=\"12\"\n")
        f.write("node [shape = circle];\n")
        for itemI in self.automate.getInitiaux():


            f.write(str(itemI.nom))
            f.write(" [color=red]\n")

        for e in self.automate.getFinaux():
            f.write(str(e.nom))
            f.write(" [shape=doublecircle];\n")

        for tr in self.automate.transition:
            f.write(str(tr.etatEntree.nom)  " -> ")
            c = tr.sortie
            if c != 0:
                f.write(str(tr.etatSortie.nom)  " [ label = \" "  str(
                    tr.afficheEntrees())  " / "  c  " \" ];\n")
            else:
                f.write(str(tr.etatSortie.nom)  " [ label = \" "  str(tr.afficheEntrees())  "\" ];\n")

        f.write("}")
        f.close()
        # generer le graph
        self.generatePng(chemin, tmp)

    def afficherDescrLigne(self):
        print("-"*50)
        for l in self.LignesListe:
            print(l.toString())
        print("-"*50)

    def setLigne(self,b):
        self.LignesListe=b

    def ajoutLigne(self,c):
        self.LignesListe.append(ligne(c))
