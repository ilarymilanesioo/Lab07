'''
1. implemento DAO
scrivo query sql per interagire con database MySQL
prima recupero le liste di base (all biblioteche all generi)
poi recupero la query per filtrare i libri come richiesto
Eseguendo i singoli DAO tramite script di testo dovrei ottenere le liste di oggetti DTO
'''

#apro connessione con database da cui leggo i dati con DB_connect
from database.DB_connect import DBConnect
#Libro: classe DTO dell'entità Libro (id, titolo, autore...)
#il DAO trasformerà le righe del database in oggetti di questo tipo
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass
    #serve a estrarre la lista di tutti i generi letterari presenti nella tabella senza ripeterli
    def get_generi(self):
        cnx=DBConnect.get_connection()
        risultato=[]
        if cnx is None:
            return risultato
        cursore=cnx.cursor(dictionary=True)

        #parola chiave DISTINCT pk ci sono centinaia di libri, molti avranno lo stesso genere (es 50 libri di Fantascienza)
        #DISTINCT dice a MySQL di eliminare i duplicati
        #WHERE...NULL evita di tirare fuori righe in cui il genere è vuoto o nullo
        query='SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL ORDER BY genere'

        cursore.execute(query)
        #la query restituisce solo una colonna (genere)
        #in ogni riga leggiamo direttamente riga["genere"] che è una stringa semplice
        #non un oggetto DTO e lo aggiungiamo alla lista risultato
        for riga in cursore:
            risultato.append(riga['genere'])
        cursore.close()
        cnx.close()
        return risultato

    #riceve i filtri scelti dall'utente e restituisce i libri corrispondenti
    #parametri id_biblioteca e genere sono i valori che arrivano dalle scelte dell'utente
    def get_libri_filtrati(self, id_biblioteca, genere):
        cnx=DB_connect.get_connection()
        risultato = []
        if cnx is None:
            print("Errore di connessione al database")
            return risultato

        cursore = cnx.cursor(dictionary=True)
        #COALESCE(valore1, valore2) restituisce il primo valore non nullo tra quelli passati
        #l'utente seleziona una biblioteca es ID 3, COALESCE(3, id_biblioteca) restituisce 3, quindi la query filtrerà WHERE id_biblioteca = 3
        #l'utente seleziona Nessun filtro (quindi il parametro passato è None), la funzione diventa COALESCE(None, id_biblioteca) che restituisce id_biblioteca
        query=('SELECT id,titolo,autore,genere,anno_pubblicazione,id_biblioteca'
               'FROM libro '
               'WHERE (id_biblioteca =COALESCE(%s,id_biblioteca))'
                   'AND (genere=Coalesce(%s,genere))')
        cursore.execute(query, (id_biblioteca, genere))
        for riga in cursore:
            libro=Libro(
                id=riga["id"],
                titolo=riga["titolo"],
                autore=riga["autore"],
                genere=riga["genere"],
                anno_pubblicazione=riga["anno_pubblicazione"],
                id_biblioteca=riga["id_biblioteca"]
            )
            risultato.append(libro)

        cursore.close()
        cnx.close()
        return risultato

    # TODO
