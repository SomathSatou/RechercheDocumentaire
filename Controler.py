from rechercheDoc import *

class Controler:

    def __init__(self, _parser):
        self.parser = _parser
        self.docs = []
        self.index = []
        self.stoplist = []

    def launch(self):
        '''lecture du cropus'''
        self.parser.lectureCorpus(self.docs,self.index)
        vp_start_gui()

    def traitementRequete(self, String requete, boolean[] parametre):
        '''prepare les elements de la requete'''

    def rechercherIndex(self, String[] requete):
        '''envoie a la vue la liste des documents pertinent trouvé'''
        Toplevel1.sendResultat(Stgring[] liste)
