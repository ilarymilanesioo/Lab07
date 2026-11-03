'''
1. implemento DAO
scrivo query sql per interagire con database MySQL
prima recupero le liste di base (all biblioteche all generi)
poi recupero la query per filtrare i libri come richiesto
Eseguendo i singoli DAO tramite script di testo dovrei ottenere le liste di oggetti DTO
'''
from database.DB_connect import DB_connect
from model.biblioteca_DTO import Biblioteca
'''
    DTO (Data Transfer Object) dell'entità Libro
'''

@dataclass()
class Libro:
    id: int
    titolo: str
    autore: str
    genere: str
    anno_pubblicazione: int
    id_biblioteca: int

    def __eq__(self, other):
        return isinstance(other, Libro) and self.id == other.id

    def __str__(self):
        return (f"{self.id} | {self.titolo} | Autore: {self.autore} | Genere: {self.genere} | "
                f"Anno: {self.anno_pubblicazione} | Biblioteca: {self.id_biblioteca}")

    def __repr__(self):
        return (f"{self.id} | {self.titolo} | Autore: {self.autore} | Genere: {self.genere} | "
                f"Anno: {self.anno_pubblicazione} | Biblioteca: {self.id_biblioteca}")
    #recupero le biblioteche
    def get_bibliotecaDAO(self):
        cnx=DB._connect.get_connection()
        cursor=cnx.cursor()
