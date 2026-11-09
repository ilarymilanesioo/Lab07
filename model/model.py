'''
2. Aggiorno Modello
Model fa da intermediario logico tra i DAO (che parlano con il database)
e il Controller (che parla con l'interfaccia grafica).
Non fa calcoli pesanti: si limita a creare le istanze dei DAO e
a esporre dei metodi puliti che il Controller potrà chiamare facilmente
'''

from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    #str= in Python non è obbligatorio specificare che tipo di dato sia una variabile
    #ma scrivere 'str' serve a dire a chi legge il codice "In questo parametro mi aspetto di ricevere una str"
    #non blocca comunque il codice se metto int al posto di uan str richiesta
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        #self: per accedere alle variabili e agli attributi interni creati nel costruttore (__init__)
        return self._libro_dao.get_libri_filtrati(biblioteca, genere)
        # TODO

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        return self._libro_dao.get_generi()
        # TODO

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        return self._biblioteca_dao.get_biblioteche()
        # TODO
