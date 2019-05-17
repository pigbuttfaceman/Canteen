from bottle import run, route, view, get, post, request, static_file
from itertools import count


#Funtion
class canteen_content:

    _ids = count (0)

    def __init__(self, name, image, stock, sold, cost, cart,):
        self.id = next(self._ids)
        self.food_name = name
        self.food_image = image
        self.food_stock = stock
        self.food_sold = sold
        self.food_cost = cost
        self.food_cart = cart


#This is a list of times that contain the values for the items
contents = [
    canteen_content("Sushi Rolls", "sushirolls.jpg", 5, 0, 3.50, 0 ),
    canteen_content("Hot Dog and Chips", "hotdog.jpg", 12, 0, 4, 0 ),
    canteen_content("Ham Sammie", "hamsammie.jpg", 4, 0, 8, 0)
]




#index page/the main front page
@route("/")
@view ("index")
def index():

    pass


#This is the ordering page where the user will choose the food items they wish to have.
@route("/order") 
@view("order") 
def order(): 
    data = dict (contents_list = contents) 
    return data 


#This grabs the pictures from the images file
@route('/picture/<filename>')
def saved_picture (filename):
    return static_file(filename, root='./images')


#This is the success page the user will see after clicking the order button
@route('/order_success/<food_id>')
@view ('order_success')
def order_success(food_id):
    
    food_id = int(food_id)
    found_food = None
    for food in contents:
        if food.id == food_id:
            found_food = food
    data = dict (food = found_food)
    found_food.food_stock = found_food.food_stock - 1  #These plus and minus to the sold and stock variables
    found_food.food_sold = found_food.food_sold + 1
    found_food.food_cart = found_food.food_cart + found_food.food_cost
    
    return data




run(host='0.0.0.0', port=8080, reloader = True, debug = True)
