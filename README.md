# Vehicle Sensor Data Simulator 🚗📊

This Python script simulates random **vehicle sensor data** (engine, speed, battery, etc.) and logs it into a CSV file.  
It can be used for testing, practice, or generating datasets for analysis and visualization.

---

## 🔧 Features
- Generates **100 rows** of random vehicle data.
- Sensor parameters include:
  - Engine RPM
  - Vehicle Speed (km/h)
  - Coolant Temperature (°C)
  - Oil Pressure (bar)
  - Fuel Level (%)
  - Throttle Position (%)
  - Battery Voltage (V)
  - Current Draw (A) *(negative if charging)*
  - Torque (Nm)
  - Air-Fuel Ratio
- **Timestamps increase randomly (1–10 seconds)** for a more realistic simulation.
- Data is saved to `vehicle_sensor_data.csv`.

---

## 📂 Example Output
```csv
TimeStamp,Engine (RPM),Speed (km/h),Coolant Temperature (°C),Oil Pressure (bar),Fuel Level (%),Throttle Position (%),Battery Voltage (Volts),Current Draw (Amperes),Torque (Nm),Air-Fuel Ratio
2025-10-02 08:15:21,2456,120,85.2,3.14,65.4,47.8,13.67,45.2,220,14.7
2025-10-02 08:15:23,3100,130,88.1,2.98,64.1,52.0,13.45,-12.6,240,13.9
