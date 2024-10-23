# Real-Time Weather Monitoring System

## Table of Contents
- [Project Overview](#project-overview)
- [Objective](#objective)
- [Data Source](#data-source)
- [Features](#features)
- [Architecture](#architecture)
- [Project preview](#project-preview)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Acknowledgements](#acknowledgements)

## Project Overview
This project implements a real-time data processing system designed to monitor weather conditions and provide summarized insights using rollups and aggregates. The system continuously retrieves weather data from the OpenWeatherMap API and processes this data to generate daily summaries and alerts based on user-defined thresholds.

## Objective
The primary objectives of this project are to:
- Monitor real-time weather data for various cities in India.
- Summarize daily weather conditions using rollups and aggregates.
- Alert users based on configurable thresholds for temperature and weather conditions.

## Data Source
The system retrieves weather data from the [OpenWeatherMap API](https://openweathermap.org/). To use this API, you will need to sign up for a free API key. The system focuses on the following parameters:
- `main`: Main weather condition (e.g., Rain, Snow, Clear).
- `temp`: Current temperature in Celsius.
- `feels_like`: Perceived temperature in Celsius.
- `dt`: Time of the data update (Unix timestamp).

## Features
- **Real-Time Data Retrieval**: Continuously fetches weather data for major metros in India, including Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
- **Data Processing**: Converts temperature from Kelvin to Celsius and aggregates daily weather data.
- **Daily Weather Summary**: Computes daily aggregates for average temperature, maximum temperature, minimum temperature, and dominant weather condition.
- **Alerts**: User-configurable thresholds for temperature and specific conditions to trigger alerts, displayed on the console.
- **Visualizations**: Displays daily weather summaries and historical trends using Plotly.

## Architecture
The system is structured into the following components:
1. **Data Retrieval**: A module that fetches weather data from the OpenWeatherMap API.
2. **Data Processing**: A module that processes and aggregates the weather data.
3. **Database**: SQLite is used for persistent storage of daily summaries.
4. **User Interface**: A PyQt5-based UI for interacting with the application.
5. **Visualizations**: Plotly is used to visualize the weather data.

## Project Preview


## Installation
### Prerequisites
- Python 3.x
- pip (Python package installer)

### Steps to Install
1. **Clone the repository**:
   ```bash
   git clone https://github.com/AyushiGupta160604/weather-monitoring-system.git
   cd weather-monitoring-system

2. **Create a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv\Scripts\activate 

3. **Install required packages**:
    Mentioned in requirements.txt
    ```
    - PyQt5
    - plotly
    - matplotlib
    - Tkinter
    - requests
    - sqlite3
    ```
    **Run the following command**:
    ```
    pip install -r requirements.txt
    ```

4. **Configure API Key**:
    In the weather_api.py file, replace "YOUR_API_KEY" with your actual OpenWeatherMap API key.


## Usage

1. **Initialize the Database**:
    ```
    python database.py
    ```

2. **Start the application**:
    ```
    python app.py
    ```

3. **Monitor Weather Data**:
- Click the **Start Monitoring** button to begin fetching and processing weather data.
- Use the **Show Visualizations** button to view the current weather summaries.

## Testing

### You can run the following test cases to validate the functionality of the system:

### 1. System Setup:

#### Verify that the system starts successfully and connects to the [OpenWeatherMap API](https://openweathermap.org/) using a valid API key.

### 2. Data Retrieval:

#### Simulate API calls at configurable intervals and ensure that the system retrieves weather data for the specified locations and parses the response correctly.

### 3. Temperature Conversion:

#### Test the conversion of temperature values from Kelvin to Celsius based on user preference.

### 4. Daily Weather Summary:

#### Simulate a sequence of weather updates for several days and verify that daily summaries are calculated correctly, including average, maximum, minimum temperatures, and the dominant weather condition.

### 5. Alerting Thresholds:

#### Define and configure user thresholds for temperature or weather conditions and simulate weather data exceeding these thresholds. Verify that alerts are triggered only when a threshold is violated.

## Acknoledgements

- [OpenWeatherMap API](https://openweathermap.org/) for providing the weather data.
- [PyQt5](https://pypi.org/project/PyQt5/) for building the GUI.
- [Plotly](https://plotly.com/python/) for data visualization.