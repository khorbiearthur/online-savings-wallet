from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'


# Add the login route with a simple text response
@app.route('/Login')
def login():
   return 'Welcome! please login'

# Add the register route with a simple text response
@app.route('/register')
def register():
   return 'sign up here'

# Add the deposit route with a simple text response 
@app.route('/deposit')
def deposit():
   return 'Add money to wallet'

# Add the withdrawal route with a simple text response 
@app.route('/withdraw')
def withdraw():
   return 'withdraw from wallet'



if __name__ == '__main__':
   app.run()
