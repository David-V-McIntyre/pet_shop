# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(a):
    pet_shop = a["name"]
    return pet_shop
    
def get_total_cash(a):
    total_cash = 0
    total_cash = a["admin"]["total_cash"]
    return total_cash

def add_or_remove_cash(a,b):
    a["admin"]["total_cash"] += b
    return a["admin"]["total_cash"]

def get_pets_sold(a):
    pets_sold = a["admin"]["pets_sold"]
    return pets_sold

def increase_pets_sold(a,b):
    a["admin"]["pets_sold"] += b
    return a["admin"]["pets_sold"]

def get_stock_count(a):
    stock_count = len(a["pets"])
    return stock_count

def get_pets_by_breed(a, b):
    pets_by_breed = []
    for pet in a["pets"]:
        if pet["breed"] == b:
            pets_by_breed.append(pet)
    return pets_by_breed

def find_pet_by_name(a,b):
    for pet in a["pets"]:
        if pet["name"] == b:
            return pet
    
def remove_pet_by_name(a,b):
    for pet in a["pets"]:
        if pet["name"] == b:
            a["pets"].remove(pet)
    
def add_pet_to_stock(a,b):
    new_pet = b 
    a["pets"].append(new_pet)
            

            
