from product_manager import ProductManager
from product import Product

# Kreiranje menadžera proizvoda
manager = ProductManager()

# Dodavanje proizvoda
manager.add_product(Product("Laptop", 1000, 5))
manager.add_product(Product("Telefon", 500, 10))
manager.add_product(Product("Tablet", 300, 7))

# Prikaz proizvoda i ukupne vrednosti
manager.display_products()
print(f"Ukupna vrednost inventara: {manager.total_inventory_value()}$")
