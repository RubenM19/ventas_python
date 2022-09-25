from typing import List, Dict
import random
from config import IGV_PERCENT, QUANTITY_MAX, QUANTITY_MIN, PRODUCT_MAX, PRODUCT_MIN, VALUE_POINT, CURRENCY_SYMBOL
import math

def main():
    # Creamos la lista de tiendas con sus cualidades
    stores: List[Dict[str, str | int | float]] = [{
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
    products: List[Dict[str, str | float | int]]= [{
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
        sales:int = random.randint(int(store["min_sales"]), int(store["max_sales"]))

        """print(f"{store['name']} Total de Tickets de Ventas: {sales}")"""
        #?Otra forma de hacer lo mismo de la línea anterior:
        #print("{} Total de Tickets de Ventas: {}".format(store['name'], sales))

        #Declaramos una lista para que almacene los tickets de venta
        list_ticket: List[Dict[str, str|float]] = []

        #Declaramos una lista para que almacene los detalles de tickets de venta
        list_detail: List[Dict[str, str|float]] = []
        
        #Iteramos sobre cantidad de ventas para crear el ticket de venta
        for i in range(sales):
            #Los tichets de Ventas deben ser aleatorios

            #Debemos obtener: MIR000001
            correlative: str = str(i+1).zfill(5) #zfill() -> llena de 0 las veces que pases por parámetro
            
            #Obtenermos el codigo del ticket
            ticket_number: str = f"{store['code']}{correlative}"
            
            #random.simple -> Devuelve lista de números únicos
            #Los números aleatorios obtenidos serás indices para obtener productos.
            list_rand_products = random.sample(range(len(products)), random.randint(PRODUCT_MIN,PRODUCT_MAX))
            #[1,8,7]
            #Variable para calcular el total acumulado
            ticket_subtotal: float = 0
            #Variable para almacenar el descuento acumulado
            ticket_discount: float = 0

            #Iteramos sobre la lista aleatoria de productos para crear el detalle del ticket
            for k,v in enumerate(list_rand_products):
               
               #Valor que se usará como precio de venta 
               #El round para que el redondeo no pase de 2 decimales
               price_sale: float = round(float(products[v]['base_price']) + (float(products[v]['base_price']) * float(store['percent_sales_price'])/100), 2)
               
               #Calculamos el descuento del rpoducto
               discount: float = round(price_sale * (float(products[v]['percent_dsct'])/100), 2)
               
               #Agregamos el descuento acumulado
               ticket_discount+=discount
               
               #Calculamos el precio final
               final_sale_price:float = round(price_sale - abs(discount), 2)

               quantity: int = random.randint(QUANTITY_MIN, QUANTITY_MAX)

               total: float = round(final_sale_price * quantity, 2)

               #Calculamos el total de descuento
               ticket_subtotal += total
               #Detalles del ticket
               detail: Dict[str, str | float] ={
                "ticket_number": ticket_number,
                "product_name": products[v]['name'],
                "base_sale_price": products[v]['base_price'],
                "sale_price": price_sale,
                "discount": discount,
                "final_price": final_sale_price,
                "quantity": quantity,
                "total": total
               }
               list_detail.append(detail)
        
            ticket_igv: float = ticket_subtotal * IGV_PERCENT/100
            ticket_total: float = ticket_subtotal + ticket_igv
            ticket_pint: int = math.ceil(ticket_subtotal / VALUE_POINT)

            ticket: Dict[str, str|float] = {
                "number": ticket_number,
                "subtotal": ticket_subtotal,
                "igv": ticket_igv,
                "total": ticket_total,
                "points": ticket_pint,
                "discount": ticket_discount
            }
            list_ticket.append(ticket)
        
        print(f"Tienda: {store['name']}")
        print(f"Total de Tickets: {len(list_ticket)}")
            




if __name__ == "__main__":
    main()


