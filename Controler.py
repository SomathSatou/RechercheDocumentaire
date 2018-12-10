from rechercheDoc import *
from IndexTree import IndexTree
import tkinter as Tk

class Controler:

    def __init__(self, _parser):
        self.tk = Tk.Tk()
        self.view = Toplevel1(self.tk, self)
        self.parser = _parser
        self.docs = []
        self.index = IndexTree("")
        self.info = []
        self.stoplist = []

    def launch(self):
        # lecture du cropus
        self.parser.lectureCorpus(self.docs, self.info, self.index)
        self.tk.mainloop()

    def traitementRequete(self, requete, parametre):  # String , Boolean[]
        # prepare les elements de la requete
        requetes = requete.split()
        return requetes

    def rechercherIndex(self, requete):  # String[]
        # envoie a la vue la liste des documents pertinent trouvé
        requetes = self.traitementRequete(requete,parametre=[])
        liste = []
        print("voici la requete " )
        print(requetes)
        for elt in requetes:
            liste.append(self.index.rechercheMot(elt))
        self.view.sendResultat(liste)
