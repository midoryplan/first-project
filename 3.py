import json 
import os
from datetime import datetime 

menu="""
1-appending product
2-deleting product
3-changing product
4-buying product
5-showing all products
6-reserching 
7-exit
"""

if not os.path.exists("products.json"):
    with open("products.json","w") as file:
        json.dump([],file)

if not os.path.exists("sales.json"):
    with open("sales.json","w") as file:
        json.dump([],file)

class Product:
    def __init__(self, name, price, available_stock: int):
        self.name= name
        self.price= price
        self.available_stock= available_stock

    def to_dict(self):
        return {"name": self.name, "price": int(self.price), "available_stock":int(self.available_stock)}

class Sale:
    def __init__(self, name, price, customer):
        self.name= name
        self.price= price
        self.customer= customer
        self.sales= 1
        self.time= datetime.now()

    def to_dict_2(self):
        return {"customer":self.customer, "name":self.name, "price":self.price, "seles":self.sales, "time":self.time}
    
def name_me():
    found= False
    global product_name
    product_name= input("write the name of product:")
    with open("products.json","r") as file:
        global products
        products= json.load(file)
        for product in products:
            if product_name== product["name"]:
                found= True
                return product 
        if not found:
            return print("there is no product by this name")
        
def to_string(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    
while True:
    user_input= input(menu)

    #appending
    if user_input=="1":
        with open("products.json","r") as file:
            product=json.load(file)
            name, price, available_stock= input("write name, price and available_stock with a | between them:").strip().split("|")
            object=Product(name, price, available_stock)
            product.append(object.to_dict())
            with open("products.json","w") as file:
                json.dump(product,file,indent=4)
                print(f"you have a new product:{name}")

    #deleting
    elif user_input=="2":
        name_of= name_me()
        if isinstance(name_of, dict):
            products.remove(name_of)
            with open("products.json","w") as file:
                json.dump(products,file)
                print(f"was deleted :{name_of["name"]}")

    #changing
    elif user_input=="3":
        menu_2="""
        1-changing name
        2-changing price 
        3-changing available_stock
        4-exit
        """
        user_input_2= input(menu_2)
        while True:
            #changing name
            if user_input_2=="1":
                name_of_2= name_me()
                if isinstance(name_of_2, dict):
                    input_name= input("write replacement:")
                    name_of_2["name"]= input_name
                    with open("products.json","w") as file:
                        json.dump(products,file)
                        print(f"new name:{input_name}")
                        break
            #changing price 
            elif user_input_2=="2":
                name_of_2= name_me()
                if isinstance(name_of_2, dict):
                    input_price= input("write replacement:")
                    name_of_2["price"]= input_price
                    with open("products.json","w") as file:
                        json.dump(products,file)
                        print(f"new price:{input_price}")
                        break
            #changing available_stock
            elif user_input_2=="3":
                name_of_2= name_me()
                if isinstance(name_of_2, dict):
                    input_stock= input("write replacement:")
                    name_of_2["available_stock"]= input_stock
                    with open("products.json","w") as file:
                        json.dump(products,file)
                        print(f"new available_stock:{input_stock}")
                        break
            #exit
            elif user_input_2=="4":
                print("have a good day!")
                break
            else:
                print("just between 1 and 4")
                break
        
    #buying
    elif user_input=="4":
        name_of_3= name_me()
        if isinstance(name_of_3, dict):
            if name_of_3["available_stock"] > 0:
                name_of_3["available_stock"] -= 1
                with open("products.json","w") as file:
                    json.dump(products,file)
                with open("sales.json","r") as file:
                    sale_list= json.load(file)
                    customer= input("write your name please:")
                    print(f"you will pay:{name_of_3["price"]}")
                    sales= Sale(product_name, name_of_3["price"],customer)
                    sale_list.append(sales.to_dict_2())
                    with open("sales.json","w") as file:
                        json.dump(sale_list,file,indent=4, default=to_string)
            else:
                print("that is not enough!")

    #showing all products
    elif user_input=="5":
        with open("products.json","r") as file:
            list= json.load(file)
            for one in list:
                print(one)
                print("----------")

    #reserching
    elif user_input=="6":
        print(name_me())

    #exit
    elif user_input=="7":
        print("have a good day!")
        break

    else:
        print("just between 1 and 7")
        continue

# 95 from 100 !