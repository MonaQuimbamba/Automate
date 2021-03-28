from Source.AnalyseurLexical import AnalyseurLexical as analyseur
from Source.AEFND import AEFND as aefnd
from Source.Transition import Transition as transition
from Source.Automate import Automate as automate
from Source.Etat import Etat as eta
from Source.Ligne import Ligne as ligne
from Source.TransitionND import TransitionND as transitionND
import re
import string
import sys

def moteur():

    nomFile=""
    """print("Automate non-determinisé")
    al1 =  analyseur(nomFile)
    al1.afficherDescrLigne()
    nonDet = aefnd()
    ## l'on le determinisé
    newFile = nonDet.exporterDescr(nonDet.determiniser(al1.automate), "ND03")
    print("Automate mtn  determinisé")
    aldet = analyseur(newFile)
    aldet.afficherDescrLigne()
    s3 = input()
    #print("Entrez les mots à analyser, séparés par un retour à la ligne")
    #print("Pour signifier la fin de la saisie, entrez ###")
    strEntree = input()
    saisie=True
    while saisie:
        print(">")
        str2 = strEntree
        if strEntree=="###":
            saisie=False
    aldet.traitementEntree(strEntree)
    #"Export du fichier .descr en fichier .dot"
    #aldet.descrToDot()"""

    """"## Analyse Automate Deterministe
    al2 = analyseur(nomFile)
    al2.afficherDescrLigne()
    al2.exportDot("C0") #"Export du fichier .descr en fichier .dot")
    #print("Entrez les mots à analyser, séparés par un retour à la ligne")
    #print("Pour signifier la fin de la saisie, entrez ###")
    strEntree=""
    saisie=True
    while saisie:
        str2 = input()
        strEntree = str2'\n'
        if str2 =="###":
            saisie=False
    al2.traitementEntree(strEntree)"""
    print("Faire Menu")







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    moteur()
