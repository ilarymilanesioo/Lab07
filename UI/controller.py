'''
4. logica del Controller
Inizializza il popolamento dei menu a tendina all'avvio (richiamando il Model),
gestisci la memorizzazione delle scelte dell'utente (tramite il parametro on_select)
implementa la funzione legata al pulsante per popolare la ListView o mostrare l'alert se la ricerca non produce risultati.
'''


import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
#riceve input dalla View, chiede dati al Model e rimanda i risultati indietro alla View
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

        # Riempie i menu a tendina appena si apre l'app
        self.popola_dropdown()

    # POPOLA DROPDOWN
    #serve a riempire i menu a tendina della View all'avvio dell'applicazione,
    #prendendo i dati dal Model
    def popola_dropdown(self):
        #1
        biblioteche = self._model.get_biblioteche()
        for b in biblioteche:
            #per ogni biblioteca creiamo un'opzione con id (key) e nome (text)
            self._view.dd_biblioteca.options.append(
                ft.dropdown.Option(key=str(b.id), text=b.nome)
            )
        #2
        generi = self._model.get_generi()
        for g in generi:
            self._view.dd_genere.options.append(
                ft.dropdown.Option(key=g, text=g)
            )
        #aggiorniamo la grafica della View per mostrare le opzioni caricate
        self._view.update()
    # TODO

    # CALLBACKS DROPDOWN
    #callbacks sono le funzioni che scattano automaticamente quando l'utente sceglie una voce dai menu a tendina
    #servono ad aggiornare le variabili di stato che abbiamo visto nell'__init__
    def read_biblioteca(self, e):
        #eseguita quando l'utente seleziona una biblioteca dal menu
        self.biblioteca_selezionata = self._view.dd_biblioteca.value

    def read_genere(self, e):
        #eseguita quando l'utente seleziona un genere dal menu
        self.genere_selezionato = self._view.dd_genere.value
    #aggiungo on_change a view:
    #quando l'utente seleziona una voce dal menu a tendina
    #la View chiama in automatico la rispettiva funzione del Controller (read_biblioteca o read_genere),
    #salvando la scelta dentro le variabili di stato (self.biblioteca_selezionata e self.genere_selezionato)
    #senza dover aspettare per forza il click sul bottone Cerca
    # TODO

    # AZIONE: MOSTRA LIBRI
    #è la funzione associata al pulsante di ricerca (Cerca Libri)
    #Prende i filtri selezionati, interroga il Model e stampa i risultati a schermo
    def handle_cerca(self, e):
        #gestisce il click del bottone di ricerca, filtrando e stampando i libri
        #svuoto la lista precedente dei risultati a schermo
        self._view.txt_result.controls.clear()

        #chiamo il Model passando i filtri correnti
        #se le variabili sono None, il COALESCE nel DAO gestirà il filtro vuoto
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        #stampo i risultati nell'interfaccia
        if not libri:
            self._view.txt_result.controls.append(
                ft.Text("Nessun libro trovato con i criteri selezionati")
            )
        else:
            self._view.txt_result.controls.append(
                ft.Text(f"Trovati {len(libri)} libri:")
            )
            for libro in libri:
                self._view.txt_result.controls.append(
                    ft.Text(f"• {libro.titolo} - {libro.autore} ({libro.genere})")
                )

        #aggiorno pagina per rendere visibili i risultati
        self._view.update()
    # TODO
