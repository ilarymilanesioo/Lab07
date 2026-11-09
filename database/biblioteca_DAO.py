'''
1. implemento DAO
scrivo query sql per interagire con database MySQL
prima recupero le liste di base (all biblioteche all generi)
poi recupero la query per filtrare i libri come richiesto
Eseguendo i singoli DAO tramite script di testo dovrei ottenere le liste di oggetti DTO
'''
#apro connessione con database da cui leggo i dati con DB_connect
from database.DB_connect import DBConnect
#Biblioteca è la classe DTO che definisce struttura dati di una biblio (id,nome,indirizzo)
#DAO deve importarla perchè questi dati verranno presi e trasformati in oggetti
from model.biblioteca_DTO  import Biblioteca
"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        cnx= DBConnect() #mi connetto al database
        risultato=[] #lista vuota che conterrà tutti oggetti Biblioteca creati
        #controllo sicurezza
        if cnx is None:
            print('Errore di connessione al database')
            return risultato
        #il cursore ci permette di spostarci nel database,inviare query,leggere risultati
        cursore=cnx.cursor(dictionary=True) #dictionary=true: restituisce ogni riga come dizionario ({'id:1,...)
        query='SELECT * FROM biblioteca'
        #invia materialmente query SQL al database per estrarre tutte le colonne (id,...) dalla tabella biblioteca
        cursore.execute(query)
        #ogni riga è un dizio
        for riga in cursore:
            biblioteca=Biblioteca(
                id=riga['id'],
                nome=riga['nome'],
                indirizzo=riga['indirizzo']
            )
            risultato.append(biblioteca)
        cursore.close()
        cnx.close()
        return risultato
    # TODO
