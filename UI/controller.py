import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def read_retailer(self, e):
        print(self._view.ddRetailer.value)
        print(self._view.ddBrand.value)
        print(self._view.ddAnno.value)

    def handleTopVendite(self, e):

        self._view.lvTxtOut.controls.clear()

        myModel = Model()

        vendite = []

        if self._view.ddAnno.value == "Nessun filtro" and self._view.ddBrand.value == "Nessun filtro" and self._view.ddRetailer.value == "Nessun filtro":
            vendite = myModel.getVendite()

        elif self._view.ddAnno.value != "Nessun filtro" and self._view.ddBrand.value != "Nessun filtro" and self._view.ddRetailer.value != "Nessun filtro":
            for vendita in myModel.getVendite():
                if vendita.data.split("-")[0] == str(self._view.ddAnno.value) and vendita.retailer == int(self._view.ddRetailer.value):
                    for prodotto in myModel.getProdotti():
                        if vendita.prodotto == prodotto.code:
                            if prodotto.brand == self._view.ddBrand.value:
                                vendite.append(vendita)

        elif self._view.ddAnno.value != "Nessun filtro" and self._view.ddBrand.value == "Nessun filtro" and self._view.ddRetailer.value == "Nessun filtro":
            for vendita in myModel.getVendite():
                if vendita.data.split("-")[0] == str(self._view.ddAnno.value):
                    vendite.append(vendita)

        elif self._view.ddAnno.value == "Nessun filtro" and self._view.ddBrand.value != "Nessun filtro" and self._view.ddRetailer.value == "Nessun filtro":
            for vendita in myModel.getVendite():
                for prodotto in myModel.getProdotti():
                    if vendita.prodotto == prodotto.code:
                        if prodotto.brand == self._view.ddBrand.value:
                            vendite.append(vendita)

        elif self._view.ddAnno.value == "Nessun filtro" and self._view.ddBrand.value == "Nessun filtro" and self._view.ddRetailer.value != "Nessun filtro":
            for vendita in myModel.getVendite():
                if vendita.retailer == int(self._view.ddRetailer.value):
                    vendite.append(vendita)

        elif self._view.ddAnno.value != "Nessun filtro" and self._view.ddBrand.value == "Nessun filtro" and self._view.ddRetailer.value != "Nessun filtro":
            for vendita in myModel.getVendite():
                if vendita.data.split("-")[0] == str(self._view.ddAnno.value) and vendita.retailer == int(self._view.ddRetailer.value):
                    vendite.append(vendita)

        elif self._view.ddAnno.value != "Nessun filtro" and self._view.ddBrand.value != "Nessun filtro" and self._view.ddRetailer.value == "Nessun filtro":
            for vendita in myModel.getVendite():
                if vendita.data.split("-")[0] == str(self._view.ddAnno.value):
                    for prodotto in myModel.getProdotti():
                        if vendita.prodotto == prodotto.code:
                            if prodotto.brand == self._view.ddBrand.value:
                                vendite.append(vendita)

        elif self._view.ddAnno.value == "Nessun filtro" and self._view.ddBrand.value != "Nessun filtro" and self._view.ddRetailer.value != "Nessun filtro":
            for vendita in myModel.getVendite():
                if vendita.retailer == int(self._view.ddRetailer.value):
                    for prodotto in myModel.getProdotti():
                        if vendita.prodotto == prodotto.code:
                            if prodotto.brand == self._view.ddBrand.value:
                                vendite.append(vendita)

        if vendite.__len__() == 0:
            self._view.lvTxtOut.controls.append(ft.Text('Nessuna vendita disponibile'))

        massimi = []

        i = 1

        while i <= 5:
            max = 0
            for vendita in vendite:
                if int(vendita.ricavo) > max and vendita not in massimi:
                    max = int(vendita.ricavo)

            for vendita in vendite:
                if int(vendita.ricavo) == max and vendita not in massimi:
                    self._view.lvTxtOut.controls.append(ft.Text(str(vendita)))
                    massimi.append(vendita)
                    i = i + 1

        self._view.update_page()


    def handleAnalizzaVendite(self, e):

        self._view.lvTxtOut.controls.clear()

        myModel = Model()

        vendite = []

        if self._view.ddAnno.value != "Nessun filtro" and self._view.ddBrand.value != "Nessun filtro" and self._view.ddRetailer.value != "Nessun filtro":
            for vendita in myModel.getVendite():
                if vendita.data.split("-")[0] == str(self._view.ddAnno.value) and vendita.retailer == int(self._view.ddRetailer.value):
                    for prodotto in myModel.getProdotti():
                        if vendita.prodotto == prodotto.code:
                            if prodotto.brand == self._view.ddBrand.value:
                                vendite.append(vendita)

        elif self._view.ddAnno.value == "Nessun filtro" and self._view.ddBrand.value == "Nessun filtro" and self._view.ddRetailer.value == "Nessun filtro":
            vendite = myModel.getVendite()

        elif self._view.ddAnno.value != "Nessun filtro" and self._view.ddBrand.value == "Nessun filtro" and self._view.ddRetailer.value == "Nessun filtro":
            for vendita in myModel.getVendite():
                if vendita.data.split("-")[0] == str(self._view.ddAnno.value):
                    vendite.append(vendita)

        elif self._view.ddAnno.value == "Nessun filtro" and self._view.ddBrand.value != "Nessun filtro" and self._view.ddRetailer.value == "Nessun filtro":
            for vendita in myModel.getVendite():
                for prodotto in myModel.getProdotti():
                    if vendita.prodotto == prodotto.code:
                        if prodotto.brand == self._view.ddBrand.value:
                            vendite.append(vendita)

        elif self._view.ddAnno.value == "Nessun filtro" and self._view.ddBrand.value == "Nessun filtro" and self._view.ddRetailer.value != "Nessun filtro":
            for vendita in myModel.getVendite():
                if vendita.retailer == int(self._view.ddRetailer.value):
                    vendite.append(vendita)

        elif self._view.ddAnno.value != "Nessun filtro" and self._view.ddBrand.value == "Nessun filtro" and self._view.ddRetailer.value != "Nessun filtro":
            for vendita in myModel.getVendite():
                if vendita.data.split("-")[0] == str(self._view.ddAnno.value) and vendita.retailer == int(self._view.ddRetailer.value):
                    vendite.append(vendita)

        elif self._view.ddAnno.value != "Nessun filtro" and self._view.ddBrand.value != "Nessun filtro" and self._view.ddRetailer.value == "Nessun filtro":
            for vendita in myModel.getVendite():
                if vendita.data.split("-")[0] == str(self._view.ddAnno.value):
                    for prodotto in myModel.getProdotti():
                        if vendita.prodotto == prodotto.code:
                            if prodotto.brand == self._view.ddBrand.value:
                                vendite.append(vendita)

        elif self._view.ddAnno.value == "Nessun filtro" and self._view.ddBrand.value != "Nessun filtro" and self._view.ddRetailer.value != "Nessun filtro":
            for vendita in myModel.getVendite():
                if vendita.retailer == int(self._view.ddRetailer.value):
                    for prodotto in myModel.getProdotti():
                        if vendita.prodotto == prodotto.code:
                            if prodotto.brand == self._view.ddBrand.value:
                                vendite.append(vendita)

        if vendite.__len__() == 0:
            self._view.lvTxtOut.controls.append(ft.Text('Nessuna vendita disponibile'))


        self._view.lvTxtOut.controls.append(ft.Text("Statistiche vendite:"))

        giroAffari = 0.0
        for vendita in vendite:
            giroAffari += float(vendita.ricavo)

        self._view.lvTxtOut.controls.append(ft.Text(f"Giro d'affari: {giroAffari}"))
        self._view.lvTxtOut.controls.append(ft.Text(f"Numero vendite: {vendite.__len__()}"))

        retailers = []

        for vendita in vendite:
            if vendita.retailer not in retailers:
                retailers.append(vendita.retailer)

        prodotti = []

        for vendita in vendite:
            if vendita.prodotto not in prodotti:
                prodotti.append(vendita.prodotto)

        self._view.lvTxtOut.controls.append(ft.Text(f"Numero retailers coinvolti: {retailers.__len__()}"))
        self._view.lvTxtOut.controls.append(ft.Text(f"Numero prodotti coinvolti: {prodotti.__len__()}"))

        self._view.update_page()
