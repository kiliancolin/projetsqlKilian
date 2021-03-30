import os

def nombre_requete(repertoire):
    path = "C:\\Users\\Elève\\Desktop\\projet NSI\\projetsqlKilian\\projetsqlKilian\\" + repertoire
    nom_requete = os.listdir(path)    
    return nom_requete


def fonction():
    for i in range(18):
        with open('requête' + str(i+1) + '.py','x') as requete:
            requete.write("""#!"C:\winpython\python-3.8.5.amd64\python.exe"

import sqlite3
import os

def database_connexion(db_file):
    connexion = None
    try:
        connexion = sqlite3.connect(db_file)
    except Error as e:
        return e

    return connexion
conn=database_connexion("data/imdb.db")

def execute(n,dico):
    l = []
    import sqlite3
    conn = sqlite3.connect('imdb.db')
    c = conn.cursor()
    c.execute(dico[n][1])
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

def requete(n,dico):
    r = execute(n,dico)
    afficher_table(execute(n,dico),dico[n][0])

def fichier_txt_en_texte(fichier):
    with open(fichier, "r") as requete:
        return requete.read()

def chemin(nom, repertoire):
    return repertoire + '/' + nom

def texte_en_liste(nom_requete, repertoire):
    requete = fichier_txt_en_texte(chemin(nom_requete, repertoire))
    return requete.split()

def liste_en_texte(liste):
    texte = ""
    for i in range(len(liste)):
        texte = texte + str(liste[i]) + " "
    return texte
    
def separer_requete_et_question(nom, repertoire):
    requete = texte_en_liste(nom, repertoire)  #transforme la requete en tableau
    question = ""
    for i in range(len(requete)):   #cherche le moment ou la question s'arrete et separe la question de la requete
        if requete[i] == "?":
            question = requete[0:i+1]  #stock la question
            requete = requete[i+1:len(requete)]  #stock la reponse
            break  #stop la boucle quand le "?" est trouve
    return [liste_en_texte(question),liste_en_texte(requete)]

def creer_dictionnaire_vide():
    dico = {}
    return dico

def nom_element_du_repertoire(repertoire):
    path = "C:\laragon\www\projet2/" + repertoire
    nom_requete = os.listdir(path)    
    return nom_requete

def stocker_requete(dico, repertoire):
    liste = nom_element_du_repertoire(repertoire)
    for i in range(len(liste)):
        requete = separer_requete_et_question(liste[i], repertoire)
        dico[i] = ['#' + str(i+1) + ') ' + requete[0], requete[1]]
        
    
def afficher(dico):
    return dico

a = creer_dictionnaire_vide()
stocker_requete(a,'requete')

def debuthtml():
    print("Content-type: text/html")
    print(""\n"")
    print("<html><head>")
    print(""\n"")
    print(" <style> table, th, td {border: 1px solid black;  padding: 5px; border-collapse: collapse;} </style> ")
    print("</head><body>")

def finhtml():
    print("</body></html>")

def execute_sql(connexion,sql):
    cur = connexion.cursor()
    cur.execute(sql[""" + str(i) + """ ][1])
    rows = cur.fetchall()
    debuthtml()
    table = str(sql[""" + str(i) + """][0]) +"<table>"     
    for row in rows:
        table += "<tr><td>" + str(row[0]) + "</td></tr>" 
    table +="</table>" 
    print(table)
    finhtml()
    
run_sql=execute_sql

run_sql(conn,a)

""")

fonction()