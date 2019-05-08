from bottle import run, route, view, get, post, request, static_file
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
    canteen_content("Sushi Rolls", "sushirolls.jpg", 5, 0 ),
    canteen_content("Hot Dog and Chips", "hotdog.jpg", 12, 0 ),
    canteen_content("Ham Sammie", "hamsammie.jpg", 4, 0)
]




#index page
@route("/")
@view ("index")
def index():

    pass


@route("/order") 
@view("order") 
def order(): 
    data = dict (contents_list = contents) 
    return data 


@route('/picture/<filename>')
def saved_picture (filename):
    return static_file(filename, root='./images')



run(host='0.0.0.0', port=8080, reloader = True, debug = True)
