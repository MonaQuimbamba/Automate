from Source.TransitionND import TransitionND as transitionND
from Source.Etat import Etat as etat
from Source.Transition import  Transition as transition
from Source.Automate import Automate as automate
import sys, os

""" Classe AEFND
    Reprend toutes les méthodes nécessaires à la génération, l'exportation et l'affichage
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
     * @param e Etat
     * @param trans Liste des transitions
     * @return Liste de transitions"""
    def getTransiTionsOf(self,e,trans):
        tr=[]
        for t in trans:
            if t.etatEntree==e:
                tr.append(t)
        return tr

    """
    Récupère la liste d'états F rassemblant tous les états non déterministes
     * qui réalisent la lambda-fermeture des états qui composent la liste T.
     * @param T Ensemble d'états
     * @param a Automate
     * @return liste d'etats
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
     * @param a Automate
     * @return Automate"""
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
                    u=self.lambda_Fermeture(self.transiter(t,c,aut),aut)
                    d.append(transitionND().buildTransitionND(t,u,c))
                    p.append(u)
        return self.toAutomate(l,d,aut.getVoc(),aut.M)

    """ Renvoie un automate généré en fonction des listes d'états L et transitions D déterminisés,
     * du vocabulaire d'entrée voc et du méta-caractère meta : cette méthode est privée et utilisée
     * en interne par déterminiser.
     * @param L Liste des états déterministes(Ensembles d'états)
     * @param D Liste des transitions déterministes
     * @param voc Liste du vocabulaire d'entrée
     * @param meta Méta-caractère
     * @return Automate
     """
    def toAutomate(self,l,d,voc,m):
        etats=[]
        transitions=[]
        for e in l:
            etats.append(etat(l.index(e)).builEtat1(l.index(e),False,False))
        etats[0].setIsiniTial(True)

        for t in d:
            e = etats[l.index(t.entree)]
            for a in t.entree:
                if a.isFinal:
                    e.setIsFinal(True)

            s = etats[l.index(t.sortie)]
            transitions.append(transition().buildTransition3(e,s,t.char))

        return automate(etats,transitions).buildAutomate4(etats,transitions,voc,m)
    """ Génère un fichier .descr a partir d'un automate a.
     * @param a Automate
     * @param name Nom de fichier"""
    def exporterDescr(self,aut,nom):
        chemin = "Output/Descr/"
        if nom != None:
            tmp = ''.join(e for e in nom if e.isalnum())
            chemin = tmp  ".descr"
        else:
            chemin = "no_name.descr"

        if not os.path.isfile(chemin):
            f = open(chemin, "a")
        else:
            cmd = "rm "  chemin
            os.system(cmd)

        f = open(chemin, "a")
        f.write("C :\""  nom  "\" \n")
        f.write("M '"  aut.M "'\n")

        voc="\""
        for c in aut.v:
            voc=c
        voc="\""
        f.write("V " voc "\n")
        f.write("E "  str(len(aut.etats))  "\n")

        etatF=""
        for e in aut.etats:
            if e.isFinal:
                etatF=str(e.nom)  " "

        f.write("F " str(etatF) "\n")


        for t in aut.transition:
            f.write("T " str(t.etatEntree.nom)  " '"str(t.entree)"' "str(t.etatSortie.nom)"\n")

        f.close()

        return chemin
