from tkinter.filedialog import askopenfilename

class Parser:
    def __init__(self):
        Parser.exist = True

    def lectureCorpus(listeDocs,Index):
        '''lis chaque corpuus et remplis les clé des fonction
        renvoie le dictionaire
        append sur la liste des documents '''
        f = open(nomFichier, "r")
        lignes = f.readlines()
        f.close()
        listeDocs.append([indiceCorpus,indiceDocument,Titre])

    def getTextDocs(self,int):
        '''renvoie le texte d'un document dans le corpus'''