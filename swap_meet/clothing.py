# from pyparsing import condition_as_parse_action
from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition=0, age=0):
        category = 'Clothing'
        super().__init__(category = category, condition=condition, age = age)

        
    def __str__(self):
        return 'The finest clothing you could wear.'