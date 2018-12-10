from rechercheDoc import *
from IndexTree import IndexTree
import tkinter as Tk

class Controler:

    def __init__(self, _parser):
        self.tk = Tk.Tk()
        self.view = create_Toplevel1(self)
        self._w = '.'
        self.parser = _parser
        self.docs = []
        self.index = IndexTree("")
        self.info = []
        self.stoplist = []

    def launch(self):
        # lecture du cropus
        self.parser.lectureCorpus(self.docs, self.info, self.index)
        self.view = vp_start_gui(self)

    def traitementRequete(self, requete, parametre):  # String , Boolean[]
        # prepare les elements de la requete
        return

    def rechercherIndex(self, requete):  # String[]
        # envoie a la vue la liste des documents pertinent trouvé
        liste = []
        for elt in requete:
            liste.append(self.index.rechercheMot(elt))
        Toplevel1.sendResultat(liste)
