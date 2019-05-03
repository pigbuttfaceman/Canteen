from bottle import run, route, view, get, post, request
from itertools import count



class canteen_content:

    _ids = count (0)

    def __init__(self, name, image, stock, sold):
        self.id = next(self._ids)
        self.food_name = name
        self.food_image = image
        self.food_stock = stock
        self.food_sold = sold



contents = [
    canteen_content("Sushi Rolls", "image", 5, 0 ),
    canteen_content("Hot Dog and Chips", "image", 12, 0 ),
    canteen_content("Ham Sammy", "image", 4, 0)
]






run(host='0.0.0.0', port=8080, reloader = True, debug = True)
