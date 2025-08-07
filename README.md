# Weather_App

# Flask Weather App

A clean and modular web application built with Flask that retrieves and displays real-time weather data using the OpenWeatherMap API. This project showcases secure API access, route handling, error management, and user-friendly interface with HTML/CSS styling.

## Features

- Live weather lookup by city name (default: Houston)
- Weather data includes status, temperature, and feels-like readings
- Graceful fallback for invalid city inputs
- Uses `.env` for secure API credential access
- Custom-styled interface built with HTML and CSS
- Rendered using Jinja2 templates and served via Waitress

## Skills Demonstrated

- Flask route design and HTTP request handling
- Secure API integration with `python-dotenv` and `requests`
- Modular code structure with reusable functions (`weather.py`)
- HTML/CSS styling and Jinja2 template rendering
- Error handling, input validation, and user feedback logic
- Production-ready serving via Waitress
- Git project hygiene with `.gitignore` and dependency tracking

## Project Structure

- server.py – Main Flask server
- weather.py – Weather API logic
- .env – Contains API key (never committed)
- requirements.txt – Dependency list
- .gitignore – Prevents tracking sensitive files
- templates/ – HTML views (input, output, error)
- static/styles/style.css – Frontend styling

## Setup Instructions

1. Clone the repository
   '''bash  
   git clone https://github.com/yourusername/weather_flask_app.git
   cd weather_flask_app

3. (Optional)
    Create a virtual environment
    python -m venv venv
    source venv/bin/activate: macOS/Linux
    venv\Scripts\activate:Windows
    
4. Install dependencies
    python -m venv venv
    source venv/bin/activate:  macOS/Linux
    venv\Scripts\activate: Windows

5. Add your .env file with API key
   API_KEY=your_openweathermap_api_key

6. - Run the app
     server.py

7. 
   Navigate to http://localhost:8000 in your browser.

## Author
Developed by Andrew, senior Biology & Geology student at University of Houston–Clear Lake




