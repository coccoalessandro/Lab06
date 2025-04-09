from database.DB_connect import DBConnect
from model.Product import Product
from model.retailer import Retailer
from model.sale import Sale


class DAO():
    def __init__(self):
        pass

    def getDateSales(self):

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = ("""SELECT YEAR(Date)
                 FROM go_daily_sales""")

        cursor.execute(query)

        anni = []
        for row in cursor:
            if row["YEAR(Date)"] not in anni:
                anni.append(row["YEAR(Date)"])

        cursor.close()
        cnx.close()
        return anni

    def getBrand(self):

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = ("""SELECT Product_number, Product_brand
                         FROM go_products""")

        cursor.execute(query)

        brands = []
        for row in cursor:
            if row["Product_brand"] not in brands:
                brands.append(row["Product_brand"])

        cursor.close()
        cnx.close()
        return brands

    def getRetailer(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = ("""SELECT Retailer_code, Retailer_name
                     FROM go_retailers""")

        cursor.execute(query)

        retailers = []
        for row in cursor:
            if row["Retailer_code"] not in retailers:
                retailers.append(Retailer(code = row["Retailer_code"], name = row["Retailer_name"]))

        cursor.close()
        cnx.close()
        return retailers

    def getSales(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = ("""SELECT *
                    FROM go_daily_sales""")

        cursor.execute(query)

        sales = []
        for row in cursor:
            sales.append(Sale(data = str(row["Date"]), retailer = row["Retailer_code"], prodotto = row["Product_number"], ricavo = row["Unit_sale_price"]*row["Quantity"]))

        cursor.close()
        cnx.close()
        return sales

    def getProducts(self):

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = ("""SELECT *
                    FROM go_products""")

        cursor.execute(query)

        prod = []

        for row in cursor:
            if row["Product_brand"] not in prod:
                prod.append(Product(code = row["Product_number"], brand = row["Product_brand"]))

        cursor.close()
        cnx.close()
        return prod

if __name__ == '__main__':
    mydao = DAO()
    print(mydao.getRetailer())


