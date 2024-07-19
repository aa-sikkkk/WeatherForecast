# 🌦️ WeatherForecast

## 🌟 Overview

The WeatherForecast is a Python-based GUI tool that allows users to fetch and visualize weather data for multiple cities. It uses the OpenWeatherMap API to retrieve real-time weather forecasts and historical weather data. Users can compare weather conditions across different locations and customize the displayed graphs to their preferences.

## ✨ Features

- **🌍 Multiple Cities Comparison**: Fetch and compare weather forecasts for multiple cities simultaneously.
- **📅 Historical Weather Data**: Retrieve and display historical weather data for any city.
- **📈 Customizable Graphs**: Customize the displayed graphs, including selecting different weather parameters and time ranges.
- **💾 Offline Data Storage**: Store fetched weather data locally for offline access and future comparisons.
- **🔔 Real-time Updates**: Receive real-time weather updates and notifications for significant weather changes.

## 🛠️ Installation

1. **📥 Clone the Repository**:

    ```sh
    git clone https://github.com/godlyharry/WeatherForecast.git
    cd WeatherForecast
    ```

2. **📦 Install Required Libraries**:

    ```sh
    pip install requests matplotlib pandas
    ```

3. **🔑 Get an API Key**:
   Register for an API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and replace `YOUR_API_KEY` in the script with your actual API key.

## 🚀 Usage

1. **▶️ Run the Application**:

    ```sh
    python main.py
    ```

2. **🏙️ Enter City Names**:
   - In the "Enter City(s)" field, input one or more city names separated by commas to fetch and compare their weather forecasts.
   - Click the "Get Weather" button to display the weather data.

3. **🔍 View Historical Data**:
   - Enter a city name in the "Enter City for Historical Data" field.
   - Click the "Get Historical Data" button to display the historical weather data for the specified city.

## 📂 Code Structure

- **`main.py`**: Main script for the GUI application.
- **`weather_history.json`**: File used to store historical weather data locally.



## 🤝 Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API.
- [Matplotlib](https://matplotlib.org/) for the graph plotting library.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework.
