from AnalyseurLexical import AnalyseurLexical as analyseur
from AEFND import AEFND as aefnd
from Transition import Transition as transition
from Automate import Automate as automate
from Etat import Etat as eta
from Ligne import Ligne as ligne
from TransitionND import TransitionND as transitionND
import tkinter as tk
from tkinter import filedialog


def moteur(path):

    nomFile = path

    #
    menu1=True
    while menu1:
        in1=path
        in1=in1.split("/")
        in1=in1[len(in1)-2]
        if in1=="Exemples_Test_Déterminisation":
            print(" Vous avez choisi un automate non deterministe")
            print("Affichage de l'Automate non-determinisé")
            al1 =  analyseur(nomFile)
            al1.afficherDescrLigne()
            nonDet = aefnd()
            nomOutFile=nomFile.split("/")[-1:][0]
            ## le determiniser
            newFile = nonDet.exporterDescr(nonDet.determiniser(al1.automate),nomOutFile)
            print("L'Automate est mtn  determinisé")
            aldet = analyseur(newFile)
            aldet.afficherDescrLigne()
            menu2=True
            while menu2:
                print("*********************************Menu 2***************************************")
                print("-----Analyse d'un automate non-Deterministe-----")
                print("1 - Analyse d'entrée ")
                print("2 - Exporter l'automate determinisé en .dot ")
                print("3 - Retour au Menu 1")
                in2 = input()
                in2=int(in2)
                if in2 ==1:
                    print("Entrez les mots à analyser, séparés par un retour à la ligne")
                    print("Pour signifier la fin de la saisie, entrez ###")
                    strEntree = ""
                    saisie = True
                    while saisie:
                        str2 = input()
                        strEntree += str2 + '\n'
                        if str2 == "###":
                            saisie = False
                    aldet.traitementEntree(strEntree)
                elif in2==2:
                    print("Exportation du fichier .descr en fichier .dot")
                    aldet.exportDot(nomOutFile)
                elif in2==3:
                    menu1 = False
                    menu2=False
        elif in1 == "Exemples_Test_Moteur":
            print(" Vous avez choisi un automate deterministe")
            print("Affichage de l'Automate")
            al1 = analyseur(nomFile)
            al1.afficherDescrLigne()
            nomOutFile = nomFile.split("/")[-1:][0]
            menu2 = True
            while menu2:
                print("*****************************Menu 2************************************")
                print("-----Analyse d'un automate non-Deterministe-----")
                print("1 - Analyse d'entrée ")
                print("2 - Exporter l'automate determinisé en .dot ")
                print("3 - Quitter ")
                in2 = input()
                in2=int(in2)

                if in2 == 3:
                    menu2 = False
                    menu1=False
                if in2 == 1:
                    print("Entrez les mots à analyser, séparés par un retour à la ligne")
                    print("Pour signifier la fin de la saisie, entrez ###")
                    strEntree = ""
                    saisie = True
                    while saisie:
                        str2 = input()
                        strEntree += str2 + '\n'
                        if str2 == "###":
                            saisie = False
                    al1.traitementEntree(strEntree)
                if in2 == 2:
                    print("Exportation du fichier .descr en fichier .dot")
                    al1.exportDot(nomOutFile)
        else:
            print("Coucou vous n'avez pas choisi les automate dans le bon fichier bye ")
            menu1=False










# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n\n\n Allez dans le dossier Ressources/Exemples_Test_Déterminisation pour choisir un automate non - deterministe")
    print(" Allez dans le dossier Ressources/Exemples_Test_Moteur pour choisir un automate deterministe")
    root = tk.Tk()
    root.withdraw()
    nomFile =filedialog.askopenfilename()
    moteur(nomFile)