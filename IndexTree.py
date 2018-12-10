class IndexTree:
    def __init__(self,char):
        self.char = char
        self.ID = []
        self.fils = []

    def ajoutFils(self,mot,id):
        if mot != "":
            trouve = 0
            for elt in self.fils:
                if elt.char == mot[0]:
                    elt.ajoutFils(mot[1:],id)
                    trouve = 1
            if trouve == 0:
                self.fils.append(IndexTree(mot[0]))
                self.fils[len(self.fils)-1].ajoutFils(mot[1:],id)
        else :
            self.ID.append(id)

    def rechercheMot(self,mot):
        if mot == "":
            return self.ID
        else:
            trouve = 0
            for elt in self.fils:
                if elt.char == mot[0]:
                    elt.rechercheMot(mot[1:])
                    trouve = 1
            if trouve == 0 :
                return []


