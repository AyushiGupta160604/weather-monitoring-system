import smtplib
from email.mime.text import MIMEText
from utils import kelvin_to_celsius

alert_thresholds = {
    'temp_max': 35.0 
}

def check_alerts(weather):
    from data_processor import kelvin_to_celsius
    temp = kelvin_to_celsius(weather['temp'])
    if temp > alert_thresholds['temp_max']:
        print(f"Alert: High temperature detected! Current temp: {temp:.2f}°C")


EMAIL_FROM = 'youremail@example.com'
EMAIL_TO = 'recipient@example.com'
EMAIL_SUBJECT = 'Weather Alert!'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USER = 'youremail@example.com'
SMTP_PASSWORD = 'yourpassword'

def send_email_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

def check_alerts(weather):
    temp = kelvin_to_celsius(weather['temp'])
    if temp > alert_thresholds['temp_max']:
        alert_msg = f"High temperature detected! Current temp: {temp:.2f}°C"
        print(alert_msg)  # Console alert
        send_email_alert(alert_msg)  # Send email alert
