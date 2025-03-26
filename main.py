from product_manager import ProductManager
from product import Product
from cart import Cart

cart = Cart()

# Kreiranje menadžera proizvoda
manager = ProductManager()

# Dodavanje proizvoda
manager.add_product(Product("Laptop", 1000, 5))
manager.add_product(Product("Telefon", 500, 10))
manager.add_product(Product("Tablet", 300, 7))

# Prikaz proizvoda i ukupne vrednosti
manager.display_products()
print(f"Ukupna vrednost inventara: {manager.total_inventory_value()}$")

# Dodavanje proizvoda u korpu
cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])

# Prikaz sadržaja korpe i ukupne cene
cart.display_cart()
print(f"Ukupna vrednost korpe: {cart.total_cart_value()}$")
