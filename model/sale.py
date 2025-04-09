from dataclasses import dataclass

from model.Product import Product
from model.retailer import Retailer


@dataclass
class Sale():
    data : str
    retailer: int
    prodotto : int
    ricavo : int

    def __str__(self):
        return f'Data: {self.data}; RIcavo: {self.ricavo}; Retailer: {self.retailer}; Prodotto: {self.prodotto}'