import enum
from typing import List, Dict
import random

def main():
    # Creamos la lista de tiendas con sus cualidades
    stores: List[Dict[str,str,int,int,float]] = [{
        "code": "MIR",
        "name": "Miraflores",
        "min_sales": 85,
        "max_sales": 110,
        "percent_sales_price": 18.75
    }, {
        "code": "SUR",
        "name": "Surquillo",
        "min_sales": 75,
        "max_sales": 100,
        "percent_sales_price": 17.95
    }, {
        "code": "LIM",
        "name": "Centro de Lima",
        "min_sales": 90,
        "max_sales": 135,
        "percent_sales_price": 18.15
    }, {
        "code": "SJM",
        "name": "San Juan de Miraflores",
        "min_sales": 95,
        "max_sales": 140,
        "percent_sales_price": 17.88
    }, {
        "code": "CHO",
        "name": "Chorrillos",
        "min_sales": 70,
        "max_sales": 95,
        "percent_sales_price": 17.80
    }]


    #Creamos lista de productos
    products: List[Dict[str, float, int]]= [{
        "name": "Memoria USB Kingston 64 GB",
        "base_price": 38.90,
        "percent_dsct": 10
    }, {
        "name": "Mouse inalámbrico Teraware Negro",
        "base_price": 59.90,
        "percent_dsct": 5
    }, {
        "name": "Teclado inalámbrico Logitech K120",
        "base_price": 39.90,
        "percent_dsct": 0
    }, {
        "name": "Batería externa G 5000 mAh ",
        "base_price": 49.90,
        "percent_dsct": 0
    }, {
        "name": "Micrófono Maono AU-903",
        "base_price": 189.90,
        "percent_dsct": 5
    }, {
        "name": "Audífonos bluetooth True Wireless Xiaomi",
        "base_price": 129.50,
        "percent_dsct": 10
    }, {
        "name": "Mouse pad gamer Teraware M",
        "base_price": 55.90,
        "percent_dsct": 0
    }, {
        "name": "Cámara web Jetion PJT-DCM141",
        "base_price": 89.90,
        "percent_dsct": 20
    }, {
        "name": "Hub Teraware conector usb 4",
        "base_price": 49.90,
        "percent_dsct": 0
    }, {
        "name": "Cooler para laptop Teraware 5 niveles",
        "base_price": 59.90,
        "percent_dsct": 5
    }]

    #Iteramos sobre cantidad de tiendas
    for key, store in enumerate(stores):
        #Total de ventas por día obtenidas de forma aleatoria
        sales:int = random.randint(store["min_sales"], store["max_sales"])

        print(f"{store['name']} Total de Tickets de Ventas: {sales}")
        #?Otra forma de hacer lo mismo de la línea anterior:
        #print("{} Total de Tickets de Ventas: {}".format(store['name'], sales))
        
        #Iteramos sobre cantidad de ventas 
        for i in range(sales):
            #Debemos obtener: MIR000001
            correlative: str = str(i+1).zfill(5) #zfill() -> llena de 0 las veces que pases por parámetro
            ticket_numer: str = f"{store['code']}{correlative}"
            list_rand_products = random.sample(range(len(products)), random.randint(1,3))
            #[1,8,7]
            #Iteramos sobre la lista aleatoria de productos para crear el detalle del ticket
            for k,v in enumerate(list_rand_products):
                print(products[v]['name'])
            
            
            print(ticket_numer)




if __name__ == "__main__":
    main()


