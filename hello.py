from flask import Flask
   app = Flask(__name__)
   @app.route('/', methods['GET']) #routing it to the home page
   def home():
    return "hello world"
   app.run(port=5000, debug=true) #function call by the app