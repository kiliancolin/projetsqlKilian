def execute(requete,dico):
    l = []
    import sqlite3
    conn = sqlite3.connect('imdb.db')
    c = conn.cursor()
    c.execute(dico[requete][1])
    for row in c:
        l.append(row)
    conn.close()
    return l

def taille_plus_grande_reponse(reponses):
    l = reponses
    maxi = 0
    for i in range(len(l)):
        if len(str(l[i])) > maxi:
            maxi = len(str(l[i]))
    return maxi

def requete(n, dico):
    r = execute(n,dico)
    afficher_table(execute(n,dico),dico[n][0])


import tkinter
import os

def afficher_table(table, titre ="", debut = 0, fin = None):
	if titre != "":
		titre += "\n\n"
	#print(titre + texte_table(table, debut, fin))
	affichage(titre + texte_table(table, debut, fin), titre)
    
def texte_table(table, debut = 0, fin = None):
  max = taille_plus_grande_reponse(table)
  texte = '/' + max * '-' + '/\n'
  for i in range(len(table)):
    texte = texte + '/' + str(table[i]) + '\n/' + max * '-' + '/\n'
  return texte

def affichage(texte, titre = "Requêtes tables"):
	root = tkinter.Tk()
	root.title(str(titre))
	RWidth=root.winfo_screenwidth() - 100
	RHeight=root.winfo_screenheight() - 100
	root.geometry("%dx%d+50+0"%(RWidth, RHeight))
	text=tkinter.Text(root, wrap = 'none')
	scroll_x=tkinter.Scrollbar(text.master, orient='horizontal', command = text.xview)
	scroll_x.config(command = text.xview)
	text.configure(xscrollcommand = scroll_x.set)
	scroll_x.pack(side = 'bottom', fill = 'x', anchor = 'w')
	scroll_y = tkinter.Scrollbar(text.master)
	scroll_y.config(command = text.yview)
	text.configure(yscrollcommand = scroll_y.set)
	scroll_y.pack(side = tkinter.RIGHT, fill = 'y')
	text.insert("1.0", texte)
	text.pack(side = tkinter.LEFT, expand = True, fill = tkinter.BOTH)
	root.mainloop()

def fichier_txt_en_texte(fichier):
    """
    prend en argument le chemin d'un fichier texte et renvoie le contenu du fichier texte sous forme de chaîne de caractère.
    """
    with open(fichier, "r") as requete:
        return requete.read()

def nom(n):
    return "requête/" + str(n) + ".txt"

def texte_en_liste(n):
    requete = fichier_txt_en_texte(nom(n))
    return requete.split()

def liste_en_texte(liste):
    """
    prend en argument une liste et un indice et renvoie la même liste mais l'élement d'indice 'n' est transformé en texte.
    """
    texte = ""
    for i in range(len(liste)):
        texte = texte + str(liste[i]) + " "
    return texte
    
def separer_requete_et_question(n):
    """
    prend en argument le numéro de la requête et renvoie la question et la requête sésparé.
    """
    requete = texte_en_liste(n)  #transforme la requête en tableau
    for i in range(len(requete)):   #cherche le moment où la question s'arrête et sépare la question de la requête
        if requete[i] == "?":
            question = requete[0:i+1]  #stock la question
            requete = requete[i+1:len(requete)]  #stock la réponse
            break  #stop la boucle quand la "?" est trouvé
    return [liste_en_texte(question),liste_en_texte(requete)]

def creer_dictionnaire_vide():
    dico = {}
    return dico

def stocker_requete(n, dico):
    requete = separer_requete_et_question(n)
    dico[n] = [requete[0], requete[1]]
    
def afficher(dico):
    return dico

a = creer_dictionnaire_vide()
stocker_requete(1,a)
stocker_requete(2,a)
stocker_requete(3,a)
stocker_requete(4,a)
stocker_requete(5,a)
stocker_requete(6,a)
stocker_requete(7,a)
stocker_requete(8,a)
stocker_requete(9,a)
stocker_requete(11,a)
stocker_requete(12,a)
stocker_requete(14,a)
stocker_requete(15,a)
#print(afficher(a))
requete(5,a)
#print(execute(1,a))
#print(taille_plus_grande_reponse(execute(1,a)))