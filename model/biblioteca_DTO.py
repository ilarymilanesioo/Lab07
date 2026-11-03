'''
1. implemento DAO
scrivo query sql per interagire con database MySQL
prima recupero le liste di base (all biblioteche all generi)
poi recupero la query per filtrare i libri come richiesto
Eseguendo i singoli DAO tramite script di testo dovrei ottenere le liste di oggetti DTO
'''
from database.DB._connect import DB_connect
from model.biblioteca_DTO  import Biblioteca

'''
    DTO (Data Transfer Object) dell'entità Biblioteca
'''

@dataclass()
class Biblioteca:
    id: int
    nome: str
    indirizzo: str

    def __eq__(self, other):
        return isinstance(other, Biblioteca) and self.id == other.id

    def __str__(self):
        return f"{self.id} | {self.nome} | Indirizzo: {self.indirizzo}"

    def __repr__(self):
        return f"{self.id} | {self.nome} | Indirizzo: {self.indirizzo}"
