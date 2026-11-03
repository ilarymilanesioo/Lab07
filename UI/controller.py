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
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN

    # TODO

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    # TODO
