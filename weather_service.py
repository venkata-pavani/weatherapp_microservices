from flask import render_template
import os 
import requests

def show_weather(zipcode):
    #api_key = os.getenv('ACCUWEATHER_API_KEY')  # Fetch the API key from environment Var
    #if not api_key:
     #    return "API Key missing"
    api_key = 'You dont want to know my key'
    print(api_key)
    print("This is zipcode",zipcode)
       
  
    resource_url = 'http://dataservice.accuweather.com/locations/v1/postalcodes/search'

    #Get location key by zip code
    location_params = {
            'apikey': api_key,
            'q': zipcode
    }
    print("These are location params",location_params)
    #hitting accuweather DB and thats why 'GET request'
    
    location_response = requests.get(resource_url,params=location_params)
    print('This is location resonse data',location_response)
    if location_response.status_code == 200 and location_response.json():
        #location_repomse.json() converts API resonse into a dictonary
        #200 status code means 'ALL OK'
        #*Below* we are getting the location key from the responses
        location_key = location_response.json()[0]['Key']
        print("This is location key",location_key)
        #Now to get current weather by LOCATION KEY
        weather_url = f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}' 
        weather_params = {
            'apikey': api_key,
            'details': 'true'
                                }
        weather_response = requests.get(weather_url,params=weather_params)
        print('This is weather resonse data',weather_response)
        print('Weather response JSON:', weather_response.json())
        #now lets get the weather details just like location details
        if weather_response.status_code == 200 and weather_response.json():
                #200 means 'ALL OK'
                #.json is becoz it converts the response data into dictionary  
                weather_data = weather_response.json()[0]
                weather_text = weather_data['WeatherText']
                temperature = weather_data['Temperature']['Metric']['Value']
                has_precip = weather_data['HasPrecipitation']
                if has_precip:
                     precip_msg = "There is precipitatiom"
                else:
                     precip_msg = "There is no precipitation"
                
                #return f"The weather in {zipcode} is {weather_text} with a temperature of {temperature}°C and {precip_msg}."
                # How to write this message in a much fancy format -used HTML for this 
                return render_template('weather.html',zipcode=zipcode,weather_text=weather_text,temperature=temperature,precip_msg=precip_msg)

        else:
            return "Cannot retrieve weather data for this location"
    else:
        return "Cannot find location key for the provided {zipcode}"
    
    
    

        



    



