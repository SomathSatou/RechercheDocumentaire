from IndexTree import IndexTree
from InfoDoc import InfoDoc

import re
import os

class Parser:
    def __init__(self):
        Parser.exist = True

    def lectureCorpus(self, listInfo, index, stoplist):
        '''lis chaque corpuus et remplis les clé des fonction
        renvoie le dictionaire
        append sur la liste des documents '''
        pathCorpus = "/home/etudiant/PycharmProjects/RechercheDocumentaire/Ressource/DOC/"
        pathRessource = "/home/etudiant/PycharmProjects/RechercheDocumentaire/Ressource/"
        listeDocs = os.listdir(pathCorpus)

        fstop = open(pathRessource + "stopwords.txt", "r")
        stopDoc = fstop.read()
        for stop in stopDoc.split("\n"):
            stoplist.append(stop)

        indiceCorpus = 0
        for doc in listeDocs:
            titrelu = False
            indiceDocument = 0
            f = open(pathCorpus+doc, "r")
            fichier_entier = f.read()
            files = fichier_entier.split("\n")
            lireTexte = 0
            for ligne in files:
                if ligne == "<DOC>" :
                    indiceDocument += 1
                regex = re.compile(r'<HEAD>(?P<titre>[\W\w+\-]*)</HEAD>')
                monTitre = re.match(regex, ligne)
                if monTitre is not None :
                    if not titrelu :
                        Titre = monTitre.group('titre')
                        info = InfoDoc(indiceCorpus, indiceDocument, Titre)
                        listInfo.append(info)
                        titrelu = True
                if ligne == "<TEXT>" :
                    lireTexte=1
                    titrelu = False
                if lireTexte ==1:
                    mots = ligne.split(" ")
                    for elt in mots :
                        elt = self.normalize(elt)
                        log = open("log.txt", "a")
                        log.write(elt)
                        log.write("\n")
                        log.close()
                        if elt != "":
                            index.ajoutFils(elt, len(listInfo)-1)
                if ligne == "</TEXT>" :
                    lireTexte = 0
            print("corpus nombre de fichier : " +str(indiceCorpus+1) + " nombre de doc : " + str(indiceDocument+1))
            #print(" nombre de lettre repéré : "+str(len(index.fils))+"/36")
            indiceCorpus += 1
            f.close()
            '''charactere =[]
            for elt in index.fils:
                charactere.append(elt.char)
            print(charactere)'''
        return


    def getTextDocs(self,int):
        '''renvoie le texte d'un document dans le corpus'''

    def normalize(self, text):
        if text != "":
            if ord(text[0]) == 45:
                text = text[1:]
                if text == "-":
                    text = text[1:]
            text = text.lower()
            text = text.replace('[', '')
            text = text.replace(']', '')
            text = text.replace(',', '')
            text = text.replace('_', '')
            text = text.replace('\'', '')
            text = text.replace('\"', '')
            text = text.replace('<', '')
            text = text.replace('>', '')
            text = text.replace('.', '')
            text = text.replace('`', '')
            text = text.replace('/', '')
            text = text.replace('$', '')
            text = text.replace('&', '')
            text = text.replace('(', '')
            text = text.replace(')', '')
            text = text.replace('{', '')
            text = text.replace('}', '')
            text = text.replace('\\', '')
            text = text.replace('~', '')
            text = text.replace('=', '')
            text = text.replace('|', '')
            text = text.replace(';', '')
            text = text.replace('?', '')
        return text

    def permaterm(self, text):
        listTerm = []
        return listTerm

    def steming(self,stemDic):
        f = open("/home/etudiant/PycharmProjects/RechercheDocumentaire/Ressource/stem.txt", "r")
        allStem = f.read()
        list = allStem.split("\n")
        for elt in list:
            regex = re.compile(r'(?P<root>[\w+\-]*) \| (?P<words>[\s\w]+)')
            stem = re.match(regex, elt)
            if stem is not None:
                Words = str(stem.group('words'))
                Words = Words.split()
                stemDic[str(stem.group('root'))] = Words