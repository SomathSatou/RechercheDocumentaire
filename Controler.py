from rechercheDoc import *
from IndexTree import IndexTree
import tkinter as Tk
from collections import OrderedDict

class Controler:

    def __init__(self, _parser):
        self.tk = Tk.Tk()
        self.view = Toplevel1(self.tk, self)
        self.parser = _parser
        self.index = IndexTree("")
        self.info = []
        self.stoplist = []
        self.stem = {}

    def launch(self):
        # lecture du cropus
        self.parser.steming(self.stem)
        self.parser.lectureCorpus(self.info, self.index, self.stoplist)

        self.tk.mainloop()

    def traitementRequete(self, requete, parametre):  # String , Boolean[Stemming,stopList,phrasalqueries,jocker*]
        # prepare les elements de la requete
        requete = self.parser.normalize(requete)
        requetes = requete.split()

        return requetes

    def sortResultat(self, listes ):
        print(listes)
        tuple = {}
        ret = []
        # a revoir pour éviter les boucles imbriqué
        for elt in listes:
            if tuple.has_key(elt):
                tuple[elt] = tuple[elt]+1
            else:
                tuple[elt] = 1
        tuple = OrderedDict(sorted(tuple.items(), key=lambda t: t[0]))
        for cle in tuple.keys():
            ret.append(cle)
        print(ret)
        return ret

    def rechercherIndex(self, requete, parametre=[0,0,0,0]):  # String[]
        # envoie a la vue la liste des documents pertinent trouvé
        requetes = self.traitementRequete(requete, parametre)
        liste = []
        print(requetes)
        for elt in requetes:
            liste = liste + self.index.rechercheMot(elt)
        print(liste)
        #crée un fonction intermédaire qui renvoie un liste trié par pertinence des docs
        liste = self.sortResultat(liste)
        self.view.sendResultat(liste)

