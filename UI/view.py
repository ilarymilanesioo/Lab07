'''
3. VIEW
Aggiungi nell'interfaccia grafica i controlli richiesti dal README:
i due Dropdown uno per le biblioteche, uno per i generi,
il pulsante "Mostra Libri" (ft.Button)
la ListView per stampare i risultat
Avviando main l'interfaccia mostra i nuovi elementi grafici posizionati nel layout sotto al titolo
'''

import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.btn_cerca = None
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None #All'inizio il Controller non è ancora collegato verrà associato subito dopo tramite il metodo apposito

    #per richiamare l'avviso a schermo passando un messaggio di errore o di testo personalizzato
    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    #con cui colleghiamo il Controller alla View, permettendo alla grafica di comunicare con la logica
    def set_controller(self, controller):
        self.controller = controller

    #per aggiornare la grafica a schermo ogni volta che cambiamo i dati
    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        #dropdown (menu a tendina) per biblioteche
        self.dd_biblioteca = ft.Dropdown(
            label="Biblioteca",
            hint_text="Seleziona una biblioteca",
            width=300,
            options=[],
            on_change=self.controller.read_biblioteca  #collega la callback del controller che ho crypto
        )
        # TODO

        # Sezione 3: Libri
        #dropdown per i generi
        self.dd_genere = ft.Dropdown(
            label="Genere",
            hint_text="Seleziona un genere",
            width=300,
            options=[],#verrà popolato da controller
            on_change = self.controller.read_genere
        )
        '''
        # --- AGGIUNGI PULSANTE DI RICERCA ---
        self.btn_cerca = ft.ElevatedButton(
            text="Cerca Libri",
            on_click=self.controller.handle_cerca
        )
'''
        # Sezione risultati
        self.txt_risultato = ft.ListView(expand=1, spacing=10, padding=10)
        # TODO

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            #raggruppa in una riga orizzontale il menu delle biblioteche, quello dei generi e il pulsante di ricerca
            ft.Row(
                [
                    self.dd_biblioteca,
                    self.dd_genere,
                    '''self.btn_cerca'''
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),

            ft.Divider(), #divisore opzionale per separare i filtri dai risultati
            # TODO

            # Sezione 3: Libri
            #mostra elenco libri filtrati
            self.txt_risultato,
            ft.Divider()
            # TODO
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
