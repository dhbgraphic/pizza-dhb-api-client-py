import requests
import os

api_url = "http://localhost:5105/api"
category_url = api_url + "/category"
pizza_deal_url = api_url + "/pizzadeal"
topping_url = api_url + "/topping"
dips_url = api_url + "/dip"

def getAllCategories():
    res = requests.get(category_url + "/getallcategories")
    return res.json()

def addcategory(category):
    res = requests.post(category_url + "/addcategory", json=category)
    return "done"

def getcategorybyid(id):
    res = requests.get(category_url + f"/{id}")
    return res.json()

def getallpizzadeals():
    res = requests.get(pizza_deal_url + "/getallpizzadeals")
    return res.json()

def addpizzadeal(deal):
    import json 
    print(json.dumps(deal, indent=4))
    res = requests.post(pizza_deal_url + "/addpizzadeal", json=deal)
    return "done"

def getpizzadealbyid(id):
    res = requests.get(pizza_deal_url + f"/{id}")
    return res.json()

def getalltoppings():
    res = requests.get(topping_url + "/getalltoppings")
    return res.json()

def addtopping(topping):
    res = requests.post(topping_url + "/addtopping", json=topping)
    return "done"

def gettoppingbyid(id):
    res = requests.get(topping_url + f"/{id}")
    return res.json()

def getalldips():
    res = requests.get(dips_url + "/getalldips")
    return res.json()

def adddip(dip):
    res = requests.post(dips_url + "/adddip", json=dip)
    return "done"

def getdipbyid(id):
    res = requests.get(dips_url + f"/{id}")
    return res.json()

def printmenu():
    print("1. categories menu")
    print("2. pizza deals menu")
    print("3. toppings menu")
    print("4. dips menu")

def printpizzadealmenu():
    print("1. Get all pizzadeals")
    print("2. Get pizzadeal by id")
    print("3. Add pizzadeal")

def printcategorymenu():
    print("1. Get all categories")
    print("2. Get category by id")
    print("3. Add category")

def printtoppingmenu():
    print("1. Get all toppings")
    print("2. Get topping by id")
    print("3. Add topping") 

def printtoppingmenu():
    print("1. Get all dips")
    print("2. Get dip by id")
    print("3. Add dip") 

def categoryhandler():
    run = True
    while run:
        printcategorymenu()
        user_input = input("enter your choice (any other key to back to main menu): ")
        if user_input == "1":
            print(getAllCategories())
        elif user_input == "2":
            id = input("enter category id: ")
            print(getcategorybyid(id))
        elif user_input == "3":
            name = input("name: ")
            categoryid = int(input("category id: "))
            description = input("description: ")
            imageurl = input("image url: ")
            isenabled = bool(input("is enabled (true/false): "))
            print(addcategory({
                "name": name,
                "categoryId": categoryid,
                "description" : description,
                "imageURL": imageurl,
                "isEnabled": isenabled,
            }))
        else:
            run = False

def toppinghandler():
    run = True
    while run:
        printtoppingmenu()
        user_input = input("enter your choice (any other key to back to main menu): ")
        if user_input == "1":
            print(getalltoppings())
        elif user_input == "2":
            id = input("enter topping id: ")
            print(gettoppingbyid(id))
        elif user_input == "3":
            name = input("name: ")
            toppingid = int(input("topping id: "))
            description = input("description: ")
            imageurl = input("image url: ")
            isenabled = bool(input("is enabled (true/false): "))
            price = float(input("price: "))
            print(addtopping({
                    "toppingId": toppingid,
                    "name": name,
                    "description": description,
                    "imageURL": imageurl,
                    "isEnabled": isenabled,
                    "price": price
            }))
        else:
            run = False

def diphandler():
    run = True
    while run:
        printtoppingmenu()
        user_input = input("enter your choice (any other key to back to main menu): ")
        if user_input == "1":
            print(getalldips())
        elif user_input == "2":
            id = input("enter dip id: ")
            print(getdipbyid(id))
        elif user_input == "3":
            name = input("name: ")
            dipid = int(input("dip id: "))
            description = input("description: ")
            imageurl = input("image url: ")
            isenabled = bool(input("is enabled (true/false): "))
            price = float(input("price: "))
            print(adddip({
                    "dipId": dipid,
                    "name": name,
                    "description": description,
                    "imageURL": imageurl,
                    "isEnabled": isenabled,
                    "price": price
            }))
        else:
            run = False

def pizzadealshandler():
    run = True
    while run:
        printpizzadealmenu()
        user_input = input("enter your choice (any other key to back to main menu): ")
        if user_input == "1":
            print(getallpizzadeals())
        elif user_input == "2":
            id = input("enter category id: ")
            print(getpizzadealbyid(id))
        elif user_input == "3":
            name = input("name: ")
            categoryid = int(input("category id: "))
            pizzadealid = int(input("pizza deal id: "))
            description = input("description: ")
            imageurl = input("image url: ")
            isenabled = bool(input("is enabled (true/false): "))
            defaulttoppings = []
            crust = input("crust types (split by comma): ").split(",")
            sauce = input("sauce types (split by comma): ").split(",")
            cook = input("cook types (split by comma): ").split(",")
            cheese = input("cheese types (split by comma): ").split(",")
            dough = input("dough types (split by comma): ").split(",")
            freetoppings = int(input("free toppings: "))
            pizzascount = int(input("number of pizzas: "))
            sizes= []
            while True:
                sizename = input("enter size name: ")
                price = float(input("enter price: "))
                sizes.append({
                    "name": sizename,
                    "price": price
                })
                inp = input("press x to finish, any other key to add more sizes: ")
                if inp == "x":
                    break

            print(addpizzadeal({
                    "pizzaDealId": pizzadealid,
                    "categoryId": categoryid,
                    "name": name,
                    "description": description,
                    "imageURL": imageurl,
                    "isEnabled": isenabled,
                    "defaultToppingIDs": defaulttoppings,
                    "sizes": sizes,
                    "crust": crust,
                    "cheese": cheese,
                    "sauce": sauce,
                    "cook": cook,
                    "cheese": cheese,
                    "dough": dough,
                    "freeToppingsCount": freetoppings,
                    "pizzasCount": pizzascount
            }))
        else:
            run = False

run = True 

while run:
    printmenu()
    user_input = input("enter your choice (any other key to exit): ")
    if user_input == "1":
        os.system("cls")
        categoryhandler()
    elif user_input == "2":
        os.system("cls")
        pizzadealshandler()
    elif user_input == "3":
        os.system("cls")
        toppinghandler()
    elif user_input == "4":
        os.system("cls")
        diphandler()
    else:
        exit()


