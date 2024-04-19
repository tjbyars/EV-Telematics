import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from geopy.distance import geodesic

# Function to calculate distance between two coordinates
def calculate_distance(start_lat, start_lon, end_lat, end_lon):
    start_point = (start_lat, start_lon)
    end_point = (end_lat, end_lon)
    return geodesic(start_point, end_point).kilometers

# Generate random data for the dataset
def generate_telematics_data(num_vehicles=50, entries_per_vehicle=10):
    data = []
    start_time = datetime(2024, 4, 1)
    end_time = start_time + timedelta(days=1)
    entry_id = 1
    for vehicle_id in range(1, num_vehicles + 1):
        prev_entry_time = start_time
        for i in range(entries_per_vehicle):
            timestamp = prev_entry_time + timedelta(minutes=5)
            if i == 0:
                distance = 0
                speed = 0
            else:
                # Calculate distance based on the difference in latitude and longitude
                prev_entry = data[-1]
                distance = calculate_distance(prev_entry['Latitude'], prev_entry['Longitude'],
                                              random.uniform(52.46, 52.50), random.uniform(-1.93, -1.86))
                time_diff_hours = (timestamp - prev_entry_time).seconds / 3600
                speed = distance / time_diff_hours if time_diff_hours > 0 else 0
                
            ignition_status = random.choice(['On', 'Off'])
            carbon_emissions = distance * random.uniform(0.2, 0.5)  # Assuming carbon emissions per km
            
            # Generating random depot and address (for demonstration purposes)
            depot = f'Depot_{random.randint(1, 5)}'
            address = f'Address_{random.randint(1, 10)}'
            
            # Format vehicle ID as 3-digit number with leading zeros
            vehicle_id_formatted = f"{vehicle_id:03}"
            
            data.append({'ID': entry_id, 'Reg Number': vehicle_id_formatted, 'Distance': distance, 'Fuel Efficiency': random.uniform(5, 15),
                         'Timestamp': timestamp, 'Ignition On/Off': ignition_status, 'Latitude': random.uniform(52.46, 52.50),
                         'Longitude': random.uniform(-1.93, -1.86), 'Depot': depot, 'Address': address,
                         'Speed': speed, 'Carbon Emissions': carbon_emissions})
            
            entry_id += 1
            prev_entry_time = timestamp
    return data

# Generate telematics data
telematics_data = generate_telematics_data()

# Create DataFrame
df = pd.DataFrame(telematics_data)

# Export DataFrame to CSV
df.to_csv('telematics_data.csv', index=False)

# Display first few rows of the DataFrame
print(df.head())
