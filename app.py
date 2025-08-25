# importing Flask class from flask module
from flask import Flask
from weather_service import show_weather
import os,requests
# creating an instance of Flask class
app = Flask(__name__)

# Executes ROOT URL when app runs and it should call ****show_weather*** as well
@app.route('/',methods=['GET','POST'])  #A decorator - allows GET and POST requests
# function returns the msg on Browser
def pav_function():
    return 'For Weather app!'

# Add a route to call show_weather with a zip code
@app.route('/weather/<zipcode>', methods=['GET'])
def weather(zipcode):
    return show_weather(zipcode) #imported the service to call this function

# runs the flask application using the app.run method
if __name__ == '__main__':
    app.run(port=8080, debug=True)