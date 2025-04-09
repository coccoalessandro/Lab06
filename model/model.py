import mysql

from database.DAO import DAO
from model.sale import Sale


class Model:
    def __init__(self):
        self.dao = DAO()

    def getAnni(self):
        return self.dao.getDateSales()

    def getBrands(self):
        return self.dao.getBrand()

    def getRetailers(self):
        return self.dao.getRetailer()

    def getVendite(self):
        return self.dao.getSales()

    def getProdotti(self):
        return self.dao.getProducts()


if __name__ == "__main__":
    model = Model()
    print(model.getRetailers())
