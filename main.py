from cart import Cart

cart = Cart()

# Dodavanje proizvoda u korpu
cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])

# Prikaz sadržaja korpe i ukupne cene
cart.display_cart()
print(f"Ukupna vrednost korpe: {cart.total_cart_value()}$")
