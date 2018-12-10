from rechercheDoc import *
from IndexTree import IndexTree
import tkinter as Tk

class Controler:

    def __init__(self, _parser):
        self.tk = Tk.Tk()
        self.view = Toplevel1(self.tk, self)
        self.parser = _parser
        self.index = IndexTree("")
        self.info = []
        self.stoplist = []

    def launch(self):
        # lecture du cropus
        self.parser.lectureCorpus(self.info, self.index, self.stoplist)
        self.tk.mainloop()

    def traitementRequete(self, requete, parametre):  # String , Boolean[Stemming,stopList,phrasalqueries,jocker*]
        # prepare les elements de la requete
        requete = self.parser.normalize(requete)
        requetes = requete.split()

        return requetes

    def rechercherIndex(self, requete, parametre=[0,0,0,0]):  # String[]
        # envoie a la vue la liste des documents pertinent trouvé
        requetes = self.traitementRequete(requete, parametre)
        liste = []
        print(requetes)
        for elt in requetes:
            liste.append(self.index.rechercheMot(elt))
        #crée un fonction intermédaire qui renvoie un liste trié par pertinence des docs
        self.view.sendResultat(liste)
