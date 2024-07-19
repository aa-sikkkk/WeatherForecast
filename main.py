import tkinter as tk
from tkinter import ttk, messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import json
import os

# Constants
API_KEY = "YOUR_API_KEY" # ADD YOUR API KEY FROM OpenWeatherMap
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"
HISTORY_FILE = "weather_history.json"

# Function to fetch weather data
def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

# Function to display weather data
def display_weather():
    cities = city_entry.get().split(',')
    all_data = []
    for city in cities:
        city = city.strip()
        weather_data = get_weather(city)
        if weather_data.get('cod') != '200':
            messagebox.showerror("Error", f"City {city} not found!")
            return
        all_data.append(weather_data)
    
    plot_weather_data(all_data)

# Function to plot weather data
def plot_weather_data(data):
    figure = plt.Figure(figsize=(10, 6), dpi=100)
    ax = figure.add_subplot(111)
    
    for weather_data in data:
        city = weather_data['city']['name']
        forecast = weather_data['list']
        temperatures = [item['main']['temp'] for item in forecast]
        timestamps = [item['dt_txt'] for item in forecast]

        ax.plot(timestamps, temperatures, marker='o', label=city)

    ax.set_title("Temperature Forecast")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°C)")
    ax.tick_params(axis='x', rotation=45)
    ax.legend()

    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2, column=0, columnspan=4, pady=10)

    # Save data to history
    save_to_history(data)

# Function to save data to history
def save_to_history(data):
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as file:
            history_data = json.load(file)
    else:
        history_data = {}

    for weather_data in data:
        city = weather_data['city']['name']
        if city not in history_data:
            history_data[city] = []
        history_data[city].append(weather_data)

    with open(HISTORY_FILE, 'w') as file:
        json.dump(history_data, file, indent=4)

# Function to load historical data
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to display historical data
def display_history():
    history_data = load_history()
    city = history_entry.get()
    if city in history_data:
        data = history_data[city][-1]
        plot_weather_data([data])
    else:
        messagebox.showerror("Error", f"No historical data for {city}")

# Main GUI window
window = tk.Tk()
window.title("Advanced Weather Forecasting")
window.geometry("1000x700")

# City entry
tk.Label(window, text="Enter City(s) (comma separated):").grid(row=0, column=0, padx=10, pady=10)
city_entry = tk.Entry(window, width=50)
city_entry.grid(row=0, column=1, padx=10, pady=10)

# Get Weather Button
get_weather_button = tk.Button(window, text="Get Weather", command=display_weather)
get_weather_button.grid(row=0, column=2, padx=10, pady=10)

# History entry
tk.Label(window, text="Enter City for Historical Data:").grid(row=1, column=0, padx=10, pady=10)
history_entry = tk.Entry(window)
history_entry.grid(row=1, column=1, padx=10, pady=10)

# Get Historical Data Button
get_history_button = tk.Button(window, text="Get Historical Data", command=display_history)
get_history_button.grid(row=1, column=2, padx=10, pady=10)

window.mainloop()
