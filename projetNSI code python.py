"""
import sqlite3
conn = sqlite3.connect('imdb.db')
c = conn.cursor()
c.execute("select * from name_basics limit 10")
for row in c:
    print(row)
conn.close()
"""

def fichier_txt_en_texte(fichier):
    """
    prend en argument le chemin d'un fichier texte et renvoie le contenu du fichier texte sous forme de chaîne de caractère.
    """
    requete = open(fichier, "r")
    return requete.read()

def stocker_requete(n):
    """
    prend en argument le numéro de la requête et renvoie la question et la requête sésparé
    """
    requete_en_une_ligne = ""     #créé une variable pour stocker la requête en une ligne
    requete = fichier_txt_en_texte("requête/" + str(n) + ".txt")  #enregistre le texte du du fichier texte dans le répertoire requête
    requete = requete.split()  #transforme la requête en tableau
    for i in range(len(requete)):   #cherche le moment où la question s'arrête et sépare la question de la requête
        if requete[i] == "?":
            question = requete[0:i+1]  #stock la question
            requete = requete[i+1:len(requete)]  #stock la réponse
            break  #stop la boucle quand la "?" est trouvé
    for i in range(len(requete)): #transforme le tableau en chaine de caractère 
        requete_en_une_ligne = requete_en_une_ligne + str(requete[i]) + " "
    return requete_en_une_ligne


print(stocker_requete(2))


"""
import sqlite3
class database:
    #https://docs.python.org/3/library/sqlite3.html
    def __init__(self, base):
        self.base = ""

    def connexion(self):
        self.con = sqlite3.connect(self.base)
        self.cur = self.con.cursor()

    def deconnexion(self):
        self.con.close()

    def fetch(self, sql):
        self.connexion()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.deconnexion()
        return result

    def execute(self, sql):
        self.connexion()
        self.cur.execute(sql)
        self.deconnexion()

    def chargersql():
        pass

    def afficher_table(texte, titre = "Requêtes tables"):
	
	    Affiche un texte (résultat d'une requête)
    	dans une fenêtre tkinter
	    Auteurs: M CHOUCHI
    	Arguments:
	    	texte: str du texte à afficher
		    titre: str du titre de la fenêtre
	    Renvoi:
		    rien
	
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
    
    def listedesrequetes():
        pass

    def infotable():
        pass

    def informations_base():
        pass
"""


"""
import sqlite3
def database_connexion(db_file):
    connexion = None
    try:
        connexion = sqlite3.connect(db_file)
    exept Error as e:
        return e

    return connexion
conn = database_connexion("data/imb.db")

def execute_sql(connexion,sql):
    cur = connexion.cursor()
    cur.execute(sql)
    raws = cur.fetchall()
    for row in rows:
        print(row)

run_sql = execute_sql
sql = "SELECT DISTINCT types FROM title_akas"
run_sql(conn,sql)
"""