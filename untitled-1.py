from bottle import run, route, view, get, post, request, static_file
from itertools import count


#Funtion
class canteen_content:

    _ids = count (0)

    def __init__(self, name, image, stock, sold, cost, cart, amount):
        self.id = next(self._ids)
        self.food_name = name
        self.food_image = image
        self.food_stock = stock
        self.food_sold = sold
        self.food_cost = cost
        self.food_cart = cart
        self.food_amount = amount


#This is a list that creates and contains the values for the items
contents = [
    canteen_content("Sushi Rolls", "sushirolls.jpg", 5, 0, 3.50, 0, 0 ),
    canteen_content("Hot Dog and Fries", "hotdog.jpg", 12, 0, 4, 0, 0 ),
    canteen_content("Ham Sammie", "hamsammie.jpg", 4, 0, 8, 0, 0)
]




#index page/the main front page
@route("/")
@view ("index")
def index():

    pass


#This is the ordering page where the user will choose the food items they wish to order.
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
    found_food.food_stock -= 1  #These plus and minus to the sold and stock variables
    found_food.food_sold += 1
    found_food.food_cart = found_food.food_cart + found_food.food_cost
    return data


#plus_stock This shows all the values of the items themselves (I.e stock, sold, cost and an add button)
@route("/plus_stock")
@view ("plus_stock")
def plus_stock():
    data = dict (contents_list = contents) 
    return data   

#This is a success page that takes the user inputted value and adds it to the stock value of the chosen food item
@route('/add_success/<food_id>', method = 'POST')
@view ('add_success')
def add_success(food_id):
    amount = request.forms.get('amount') #This grabs the users input 
    amount = int(amount)
    food_id = int(food_id)
    found_food = None
    for food in contents:
        if food.id == food_id:
            found_food = food
    data = dict (food = found_food)
    found_food.food_stock += amount #This is the code that adds the input to the stock value
    
    return data
 



#This is a page that takes the ID of the food item and allows the user to input a new stock value to it
#It then passes everthing to the add_success page where it will add the new stock value to the old stock value of that food item
@route("/user_input/<food_id>")
@view ("user_input")
def user_input(food_id):
    data = dict (contents_list = contents)
    food_id = int(food_id)
    found_food = None
    for food in contents:
        if food.id == food_id:
            found_food = food
    data = dict (food = found_food)    
    return data  


#stock This shows all the values of the items themselves
@route("/stock")
@view ("stock")
def stock():
    data = dict (contents_list = contents) #This defines contents_list
    return data    








#This is spare code 
@route('/filler/<food_id>')
@view ('filler')
def filler(food_id):
    
    food_id = int(food_id)
    found_food = None
    for food in contents:
        if food.id == food_id:
            found_food = food
    data = dict (food = found_food)
    found_food.food_stock += 1  
    
    return data




run(host='0.0.0.0', port=8080, reloader = True, debug = True)