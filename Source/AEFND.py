from TransitionND import TransitionND as transitionND
from Etat import Etat as etat
from Transition import  Transition as transition
from Automate import Automate as automate
import sys, os

""" Classe AEFND
    cette classe va reprendre les méthodes nécessaires à la génération, l'exportation et l'affichage
    d'un automate non déterministe vers un automate déterministe.
"""
class AEFND:
    def __init__(self):
        print("---")
        """
        Récupère la liste de tous les voisins F de la liste d'entrée T ayant comme transition
          le caractère placé en paramètre a.
          @param T Ensemble d'états
          @param a caractère transitoire
          @param aut Automate
          @return liste d'Etats
        """
    def transiter(self,T,a,aut):
        f=[]
        for e in T:
            voisins = self.getTransiTionsOf(e,aut.getTransitions())
            for v in voisins:
                if v.entree == a:
                    u= v.getEtatSortie()
                    if u not in f:
                        f.append(u)
        return f
        """ Récupère toutes les transitions dont l'état e est l'état entrant.
          @param e Etat
          @param trans Liste des transitions
          @return Liste de transitions
         """
    def getTransiTionsOf(self,e,trans):
        tr=[]
        for t in trans:
            if t.etatEntree==e:
                tr.append(t)
        return tr
        """
        Récupère la liste d'états F rassemblant tous les états non déterministes
          qui réalisent la lambda-fermeture des états qui composent la liste T.
          @param T Ensemble d'états
          @param a Automate
          @return liste d'etats
        """
    def lambda_Fermeture(self,T,aut):
        v=aut.getTransitions()
        f=[]
        p=[]
        for e in T:
            p.append(e)

        while p:
            t=p[0]
            if t not in f:
                f.append(t)
                trans=self.getTransiTionsOf(t,v)
                for tr in trans:
                    if tr.entree== aut.M:
                        p.append(tr.etatSortie)
            p.remove(t)

        return f
        """Déterminise un automate non-déterministe.
          @param a Automate
          @return Automate
        """
    def determiniser(self,aut):
        p=[]
        p.append(self.lambda_Fermeture(aut.getInitiaux(),aut))
        l=[]
        d=[]
        voc=aut.getVoc()
        while p:
            t=p.pop()
            if t not in l:
                l.append(t)
                for c in voc:
                    if c!="#":
                        u=self.lambda_Fermeture(self.transiter(t,c,aut),aut)
                        d.append(transitionND().buildTransitionND(t,u,c))
                        p.append(u)

        print("Etat : \n")
        l=self.cleanEtat(l)
        self.afficherEtat(l)
        print("\n Transitions")
        d = self.cleanTransition(d)
        self.afficherTransition(d)

        return self.toAutomate(l,d,aut.getVoc(),aut.M,aut)
        """
            Affiche un ensemble d'états d'une façon propre
            @param l liste de liste d'états
            @return void
        """
    def afficherEtat(self,l):

        et = ""
        i = 0
        for etas in l:
            i += 1
            et += "["
            for e in etas:
                if e:
                    et += "" + str(e.nom)
            et+="]"
            et += "\n"
        print(et)
        """
               Affiche un état d'une façon propre
               @param l liste  d'états
               @return void
        """
    def afficheOnlyEtat(self,l):
        et="["
        if l:
            for e in l:
                et+=str(e.nom)
        et+="]"
        print(et)
        """
               Affiche un ensemble transitions  d'une façon propre
               @param l liste de transition
               @return void
        """
    def afficherTransition(self,t):
        trans="\n"
        if t:
            for tr in t:
                trans+=str(tr.toString())+"\n"
        print(trans)
        """
        enlever les etats null d'une liste d'états
        @:param listEtat liste d'états
        @:return Liste d'états
      """
    def cleanEtat(self,listEtat):
        res=[]
        for e in listEtat:
            if e:
                res.append(e)
        return res
        """ Renvoie un automate généré en fonction des listes d'états L et transitions D déterminisés,
        du vocabulaire d'entrée voc et du méta-caractère meta : cette méthode est privée et utilisée
        en interne par déterminiser.
        @param L Liste des états déterministes(Ensembles d'états)
        @param D Liste des transitions déterministes
        @param voc Liste du vocabulaire d'entrée
        @param meta Méta-caractère
        @return Automate
       """

    def toAutomate(self,l,d,voc,m,aut):

        etats=[]
        transitions=[]
        for e in l:
             ## on se debarrasse des éttas avec transition null
            etats.append(etat(l.index(e)).builEtat1(l.index(e),False,False))
        etats[0].setIsiniTial(True)
        # donner les états finaux :
        tmpEtats=self.getNomEtats(l)

        for i in range(len(etats)):
            if self.verifierEtatisFinalIN(aut.getFinaux(),tmpEtats[i]):
                etats[i].setIsFinal(True)


        for t in d:
            e = etats[l.index(t.entree)]

            if t.sortie:
                s = etats[l.index(t.sortie)]
                transitions.append(transition().buildTransition3(e,s,t.char))


        return automate(etats,transitions).buildAutomate4(etats,transitions,voc,m)

    def getNomEtats(self, l):
        res = []
        for etas in l:
            et = []
            for e in etas:
                if e:
                    et.append(int(e.nom))
            res.append(et)
        return res
    def verifierEtatisFinalIN(self,finauxEtat,tmpEtats):

        for e in self.getEtatFinaux(finauxEtat):
            if e in tmpEtats:
                return True

    def getEtatFinaux(self,liste):
        res=[]
        for e in liste:
            res.append(e.nom)
        return res
        """
            enlever les transations vers un état null
            @:param listTransition liste de Transition
            @:return void
        """
    def cleanTransition(self,listTransition):
        res=[]
        for t in listTransition:
            if len(t.entree)!=0 or len(t.sortie)!=0:
                res.append(t)
        return res

        """ Génère un fichier .descr a partir d'un automate a.
          @:param a Automate
          @:param name Nom de fichier
        """
        """
            Permet faire un fichier .Descr
            @:param un automate aut et le nom du fichier de .Descr
        """
    def exporterDescr(self,aut,nom):
        chemin = "../Output/Descr/"+str(nom)
        if not os.path.isfile(chemin):
            f = open(chemin, "a")
        else:
            cmd = "rm " + chemin
            os.system(cmd)
            f = open(chemin, "a")

        f.write("C :\""+  str(nom) + "\" \n")
        f.write("M '"  +str(aut.M) +"'\n")

        voc="\""
        for c in aut.v:
            voc+=c
        voc+="\""
        f.write("V " +str(voc) +"\n")
        f.write("E " + str(len(aut.etats)) + "\n")
        etatF=""
        for e in aut.etats:
            if e.isFinal:
                etatF+=str(e.nom)+  " "

        f.write("F " +str(etatF)+ "\n")

        for t in aut.transition:
            f.write("T " +str(t.etatEntree.nom) + " '"+str(t.entree)+"' "+str(t.etatSortie.nom)+"\n")
        f.close()

        return chemin
