# weatherapp_microservices
Created a weather app that uses AccuWeather’s API to instantly show the current temperature for any location you type in.

# WeatherApp - Flask API

A Flask-based Weather App that fetches real-time weather data using the AccuWeather API. Users can input a zip code to get the current weather conditions, temperature, and precipitation details.

---

## Features
- Fetches weather data by zip code.
- Displays weather conditions, temperature, and precipitation details.
- Uses Flask for the backend and AccuWeather API for weather data.
- Responsive HTML templates for a clean and user-friendly interface.

---

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- `pip` (Python package manager)


### Project Structure
   WeatherApp_FlaskAPI/
├── app.py                  # Main Flask application
├── weather_service.py      # Weather fetching logic
├── requirements.txt        # Python dependencies
├── templates/
│   └── weather.html        # HTML template for displaying weather data
└── README.md               # Project documentation

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/weather-app.git
2.   cd weather-app
3.   **Start the App**
       python app.py
4. Access app in the browser
   http://127.0.0.1:8080/weather/<zipcode>
### How it looks 
   <img width="1897" height="593" alt="image" src="https://github.com/user-attachments/assets/64d3fa09-a5d0-4e42-b4b2-0806865075a6" />

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
AccuWeather API: For providing weather data.
Flask: For the web framework.
Python: For making development easy and fun.
[Visit AccuWeather API](https://developer.accuweather.com/apis)
Author
Developed by [Pavani Nrusimhadevara](https://www.linkedin.com/in/pavani-nrusimhadevara/).
Code is available on GitHub(https://github.com/venkata-pavani).


