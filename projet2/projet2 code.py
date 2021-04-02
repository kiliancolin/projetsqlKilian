import os

def nombre_requete(repertoire):
    path = "C:\\laragon\\www\\projet2\\" + repertoire
    nom_requete = os.listdir(path)    
    return len(nom_requete)

def fichier_txt_en_texte(fichier):
    """
    prend en argument le chemin d'un fichier texte
    Renvoie le contenu du fichier texte sous forme de chaîne de caractère.
    """
    with open(fichier, "r") as requete:
        return requete.read()

def chemin(nom, repertoire):
    """
    Prend en argument le nom du fichier où est stocké la requête et le nom du répertoire dans lequel est stocké la requête.
    Renvoie le chemin de la requête.
    """
    return repertoire + '/' + nom

def texte_en_liste(nom_requete, repertoire):
    requete = fichier_txt_en_texte(chemin(nom_requete, repertoire))
    return requete.split()

def liste_en_texte(liste):
    """
    prend en argument une liste et un indice et renvoie la même liste mais l'élement d'indice 'n' est transformé en texte.
    """
    texte = ""
    for i in range(len(liste)):
        texte = texte + str(liste[i]) + " "
    return texte[0:len(texte)]

def separer_requete_et_question(nom, repertoire):
    """
    prend en argument le numéro de la requête et renvoie la question et la requête sésparé.
    """
    requete = texte_en_liste(nom, repertoire)  #transforme la requête en tableau
    question = ""
    for i in range(len(requete)):   #cherche le moment où la question s'arrête et sépare la question de la requête
        if requete[i] == "?":
            question = requete[0:i+1]  #stock la question
            requete = requete[i+1:len(requete)]  #stock la réponse
            break  #stop la boucle quand la "?" est trouvé
    return [liste_en_texte(question),liste_en_texte(requete)]

def creer_dictionnaire_vide():
    """
    Ne contient aucun argument et renvoie un dictionnaire vide.
    """
    dico = {}
    return dico

def nom_element_du_repertoire(repertoire):
    """
    prend en argument le nom d'un répertoire ranger dans le dossier projetsqlKilian.
    renvoie une liste dont chaque élément est le nom d'un des fichier du repertoir.
    """
    path = "C:\\laragon\\www\\projet2\\" + repertoire
    nom_requete = os.listdir(path)    
    return nom_requete

def stocker_requete(dico, repertoire):
    """
    prend en argument dico un dictionnaire vide et repertoire le nom du repertoir où sont sockés les requêtes.
    ne renvoie rien
    """
    liste = nom_element_du_repertoire(repertoire)
    for i in range(len(liste)):
        requete = separer_requete_et_question(liste[i], repertoire)
        dico[i] = ['#' + str(i+1) + ') ' + requete[0], requete[1]]

def afficher(dico):
    """
    prend en argument un dictionnaire et renvoie ce disctionnaire.
    """
    return dico

a = creer_dictionnaire_vide()
stocker_requete(a,"requete")

def vider(repertoire, data):
    """
    Prend en argument repertoire le nom du répertoire qui doit être vidé et data un fichier/dossier qui ne doit pas être supprimé.
    Ne renvoie rien.
    """
    i = nombre_requete(repertoire) - 1
    liste = nom_element_du_repertoire(repertoire)
    while i >= 0:
        if liste[i] == data:
            i = i - 1
        os.remove(repertoire + "/" + liste[i])
        i = i - 1

def creer_fichier_python(dico,repertoire):
    """
    Prend en argument un dictionnaire de requête et un repertoire.
    Remplit le répertoire avec des fichiers python dont les noms sont chaque indice du dictionnaire.
    """
    for i in range(nombre_requete(repertoire)):
        question = str(dico[i][0])
        with open("requete_python/" + question[0:len(question)-2] + '.py','w') as requete:
            requete.write("""#!"C:\winpython\python-3.8.5.amd64\python.exe"

import sqlite3
def database_connexion(db_file):
    connexion = None
    try:
        connexion = sqlite3.connect(db_file)
    except Error as e:
        return e

    return connexion
conn=database_connexion("data/imdb.db")

def debuthtml():
    print("Content-type: text/html")
    print("")
    print("<html><head>")
    print("")
    print(" <style> table, th, td {border: 1px solid black;  padding: 5px; border-collapse: collapse;} </style> ")
    print("</head><body>")

def finhtml():
    print("</body></html>")

def execute_sql(connexion,sql):
    cur = connexion.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    debuthtml()
    table = """ + '"' + str(dico[i][0]) + '"' + """'<table>'    
    for row in rows:
        table += "<tr><td>"+str(row[0])+"</td></tr>"
    table +="</table>"
    print(table)
    finhtml()
    
run_sql=execute_sql

sql= """ + '"' + str(dico[i][1]) + '"' + """
run_sql(conn,sql)
""")

#a = creer_dictionnaire_vide()
#stocker_requete(a,'requete')
#creer_fichier_python(a,"requete")
vider("requete_python", "data")
