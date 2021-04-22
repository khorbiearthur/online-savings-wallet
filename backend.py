from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'


# Add the login route with a simple text response
# Add the register route with a simple text response
# Add the deposit route with a simple text response 
# Add the withdrawal route with a simple text response 


if __name__ == '__main__':
   app.run()