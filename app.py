import sys
import time
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from weather_api import get_weather_data
from data_processor import process_weather_update
from alert_system import check_alerts
from database import insert_daily_summary, init_db
from visualizations import plot_daily_temperatures
import matplotlib.pyplot as plt

cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

init_db()

class WeatherMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.last_update_day = None
        self.daily_summaries = {}

    def init_ui(self):
        self.setWindowTitle("Weather Monitoring System")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.start_button = QPushButton("Start Monitoring")
        self.start_button.clicked.connect(self.start_monitoring)
        layout.addWidget(self.start_button)

        self.status_label = QLabel("Status: Ready")
        layout.addWidget(self.status_label)

        self.plot_button = QPushButton("Show Visualizations")
        self.plot_button.clicked.connect(self.show_visualizations)
        layout.addWidget(self.plot_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_monitoring(self):
        self.status_label.setText("Status: Monitoring...")
        self.run_weather_monitoring()

    # def run_weather_monitoring(self):
    #     while True:
    #         for city in cities:
    #             weather = get_weather_data(city)
    #             if weather:
    #                 print(f"Weather data for {city}: {weather}")
    #                 avg_temp, max_temp, min_temp, dominant_condition = process_weather_update(city, weather)
    #                 current_day = time.strftime('%Y-%m-%d', time.gmtime())

    #                 self.daily_summaries[current_day] = (avg_temp, max_temp, min_temp, dominant_condition)
    #                 print(f"Daily summaries for {current_day}: {self.daily_summaries[current_day]}")  # Debugging line

    #         current_day = time.strftime('%Y-%m-%d', time.gmtime())
    #         if current_day != self.last_update_day:
    #             for date, data in self.daily_summaries.items():
    #                 avg_temp, max_temp, min_temp, dominant_condition = data  # Unpack the data
    #                 print(f"Inserting summary for {date}: Avg {avg_temp}, Max {max_temp}, Min {min_temp}, Condition {dominant_condition}")
    #                 print(f"Values before insertion: date={date}, avg_temp={avg_temp}, max_temp={max_temp}, min_temp={min_temp}, dominant_condition={dominant_condition}")

    #                 insert_daily_summary(date, avg_temp, max_temp, min_temp, dominant_condition)

    #             self.daily_summaries.clear()
    #             self.last_update_day = current_day
            
    #         time.sleep(10)
    def run_weather_monitoring(self):
        while True:
            for city in cities:
                weather = get_weather_data(city)
                if weather:
                    print(f"Weather data for {city}: {weather}")  # Debugging line
                    result = process_weather_update(city, weather)
                
                    if result:  # Only proceed if result is not None
                        avg_temp, max_temp, min_temp, dominant_condition = result
                        current_day = time.strftime('%Y-%m-%d', time.gmtime())
                    
                    # Store the summary in daily_summaries
                        self.daily_summaries[current_day] = (avg_temp, max_temp, min_temp, dominant_condition)
                        print(f"Daily summaries for {current_day}: {self.daily_summaries[current_day]}")  # Debugging line
                    else:
                        print(f"Could not process weather data for {city}.")
                else:
                    print(f"Failed to retrieve weather data for {city}.")

            current_day = time.strftime('%Y-%m-%d', time.gmtime())
            if current_day != self.last_update_day:
                for date, data in self.daily_summaries.items():
                    avg_temp, max_temp, min_temp, dominant_condition = data  # Unpack the data
                    print(f"Inserting summary for {date}: Avg {avg_temp}, Max {max_temp}, Min {min_temp}, Condition {dominant_condition}")
                    insert_daily_summary(date, avg_temp, max_temp, min_temp, dominant_condition)

                self.daily_summaries.clear()  # Clear the dictionary after inserting
                self.last_update_day = current_day
        
            time.sleep(10)


    def show_visualizations(self):
        conn = sqlite3.connect('weather_data.db')
        c = conn.cursor()

        c.execute("SELECT * FROM daily_weather ORDER BY date")
        rows = c.fetchall()

        if not rows:
            print("No data in daily_weather table.")
        else:
            print(f"Fetched {len(rows)} rows from daily_weather table.")

        dates = [row[0] for row in rows]
        avg_temps = [row[1] for row in rows]
        max_temps = [row[2] for row in rows]
        min_temps = [row[3] for row in rows]

        print(dates, avg_temps, max_temps, min_temps)

        if dates and avg_temps and max_temps and min_temps:
            plot_daily_temperatures(dates, avg_temps, max_temps, min_temps)
        else:
            print("No data to plot.")
        conn.close()

def main():
    app = QApplication(sys.argv)
    window = WeatherMonitor()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()