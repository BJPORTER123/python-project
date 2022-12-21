class Creature:
    def __init__(self, name, habitat, description, quantity, buying_cost, selling_price, image = None, id = None):
        self.name = name
        self.habitat = habitat
        self.description = description
        self.quantity = quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.image = image
        self.id = id


