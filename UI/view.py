import flet as ft
from database.DAO import DAO
from model.model import Model


class View():
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab06"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        self._model = None
        # graphical elements
        self._title = None
        self.ddAnno = None
        self.ddBrand = None
        self.ddRetailer = None
        self.btnTopVendite = None
        self.btnAnalizzaVendite = None
        self.lvTxtOut = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        self.ddAnno = ft.Dropdown(label = "anno", width = 150, options=[ft.dropdown.Option('Nessun filtro')])

        myModel = Model()

        for anno in myModel.getAnni():
            self.ddAnno.options.append(ft.dropdown.Option(anno))

        self.ddBrand = ft.Dropdown(label = "brand", width = 150, options=[ft.dropdown.Option('Nessun filtro')])
        for brand in myModel.getBrands():
            self.ddBrand.options.append(ft.dropdown.Option(brand))

        self.ddRetailer = ft.Dropdown(label = "retailer", width = 450, options=[ft.dropdown.Option('Nessun filtro')], on_change=self._controller.read_retailer)
        for retailer in myModel.getRetailers():
            self.ddRetailer.options.append(ft.dropdown.Option(key = retailer.code, text = retailer.name))

        self.btnTopVendite = ft.ElevatedButton(text = "Top Vendite", on_click=self._controller.handleTopVendite)
        self.btnAnalizzaVendite = ft.ElevatedButton(text = "Analizza Vendite", on_click=self._controller.handleAnalizzaVendite)

        self.lvTxtOut = ft.ListView()

        row1 = ft.Row([self.ddAnno, self.ddBrand, self.ddRetailer])
        row2 = ft.Row([self.btnTopVendite, self.btnAnalizzaVendite], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2, self.lvTxtOut)
        self._page.update()


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
