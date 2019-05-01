from bottle import run, route, view, get, post, request
from itertools import count



class canteen:

    _ids = count (0)

    def __init__(self, name, stock, image):
        self.id = next(self._ids)
        self.food_name = name
        self.food_image = image
        self.food_stock = stock
        self.food_sold = sold



contents = [
    canteen_content("sushi rolls", "image", 8 ),
    canteen_content("hot dog and chips", "image", 12 ),
    canteen_content("ham sandwhich", "image", 3)
]






run(host='0.0.0.0', port=8080, reloader = True, debug = True)
