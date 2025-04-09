from dataclasses import dataclass

from model.retailer import Retailer

@dataclass
class Product :
    code: str
    brand : str