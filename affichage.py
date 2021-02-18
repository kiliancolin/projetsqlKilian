# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
########################################################################
#	imports
########################################################################
import tkinter
import os

def afficher_table(table, titre ="", debut = 0, fin = None):
	"""
	Affiche une table.
	Cette fonction était demandée dans le sujet.
	On peut avoir un affichage en console ou dans une fenêtre tkinter
	Cependant, on la redéfini ci-dessous.
	Auteurs: M CHOUCHI
	Arguments:
		table: une liste de tuples
		titre: str du titre à afficher avant la table
		debut: indice de la première ligne que l'on veut afficher
		fin: indice de la dernière ligne que l'on veut afficher
			si fin est à None, on affiche jusqu'à la dernière ligne
	Renvoi:
		rien
	"""
	if titre != "":
		titre += "\n\n"
	#print(titre + texte_table(table, debut, fin))
	affichage(titre + texte_table(table, debut, fin), titre)


def affichage(texte, titre = "Requêtes tables"):
	"""
	Affiche un texte (résultat d'une requête)
	dans une fenêtre tkinter
	Auteurs: M CHOUCHI
	Arguments:
		texte: str du texte à afficher
		titre: str du titre de la fenêtre
	Renvoi:
		rien
	"""
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

affichage("teste",titre = "Requêtes tables")