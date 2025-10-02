import csv
import random
from datetime import datetime, timedelta

file_name = "vehicle_sensor_data.csv"

# Fields for the Simulator
fields = ['TimeStamp','Engine (RPM)', 'Speed (km/h)', 'Coolant Temperature (°C)', 'Oil Pressure (bar)', 
          'Fuel Level (%)', 'Throttle Position (%)', 'Battery Voltage (Volts)', 'Current Draw (Amperes)',
            'Torque (Nm)', 'Air-Fuel Ratio' ]
start_time = datetime.now()

with open (file_name, 'w', newline='') as csvfile:
    sensors = csv.DictWriter(csvfile, fieldnames=fields)
    sensors.writeheader()

    for i in range(100): # Generate 100 rows
        # Randomize timestamp for each iteration.
        timestamp = start_time + timedelta(seconds= random.randint(1,10))

        row = {'TimeStamp': timestamp.strftime("%Y-%m-%d %H:%M:%S"), 'Engine (RPM)': random.randint(500, 7000), 'Speed (km/h)':random.randint(0, 220), 'Coolant Temperature (°C)':
            round(random.uniform(70, 120),2), 'Oil Pressure (bar)': round(random.uniform(1.0, 5.0), 2),
            'Fuel Level (%)': round(random.uniform(0, 100), 2), 'Throttle Position (%)': round(random.uniform(0, 100),2),
            'Battery Voltage (Volts)': round(random.uniform(11.50, 14.80),2), 'Current Draw (Amperes)':
            round(random.uniform(-50, 200),2),'Torque (Nm)': random.randint(50, 400), 'Air-Fuel Ratio':
            round(random.uniform(12.0, 16.0),2) }
        
        sensors.writerow(row)
