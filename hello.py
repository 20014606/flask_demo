from flask import Flask
   app = Flask(__name__) # creating app
   @app.route('/', methods['GET']) #routing it to the home page
   def home(): #function
       return "hello world"
   app.run(port=5000, debug=true) #function call by the app