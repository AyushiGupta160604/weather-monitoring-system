import sqlite3

def init_db():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS daily_weather (
                    date TEXT PRIMARY KEY,
                    avg_temp REAL,
                    max_temp REAL,
                    min_temp REAL,
                    dominant_condition TEXT
                )''')
    conn.commit()
    conn.close()
    # print("successfully")


def insert_daily_summary(date, avg_temp, max_temp, min_temp, dominant_condition):
    try:
        conn = sqlite3.connect('weather_data.db')
        c = conn.cursor()
        print(f"Inserting into database: {date}, {avg_temp}, {max_temp}, {min_temp}, {dominant_condition}")
        c.execute('''INSERT INTO daily_weather (date, avg_temp, max_temp, min_temp, dominant_condition)
                     VALUES (?, ?, ?, ?, ?)''', (date, avg_temp, max_temp, min_temp, dominant_condition))
        conn.commit()
        print(f"Successfully inserted data for {date}.")
    except sqlite3.IntegrityError as e:
        print(f"Integrity error: {e} for date {date}. Data may already exist.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e} for date {date}.")
    finally:
        conn.close()



def fetch_all_weather_data():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM daily_weather")
    rows = c.fetchall()
    conn.close()
    return rows

print(fetch_all_weather_data())
