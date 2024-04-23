import pandas as pd
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
    
    # Generate a single random fuel efficiency value for each vehicle
    fuel_efficiency_values = [random.uniform(12.75, 21.26) for _ in range(num_vehicles)]
    
    for vehicle_id in range(1, num_vehicles + 1):
        fuel_efficiency = fuel_efficiency_values[vehicle_id - 1]  # Get the fuel efficiency for this vehicle
        
        # Randomly select fuel type for the vehicle
        fuel_type = random.choice(['Petrol', 'Diesel'])
        
        # Randomly select initial timestamp for each vehicle within the week
        initial_date = datetime(2024, 4, (random.randint(1, 7))) # Initial date is between 01 and 07
        initial_hour = random.randint(4, 23)  # Initial hour is between 04:00 and 23:00
        initial_minute = random.choice(range(0, 60, 5))  # Multiples of 5 for minutes
        
        start_time = initial_date + timedelta(hours=initial_hour, minutes=initial_minute)
        
        prev_entry_time = start_time
        for i in range(entries_per_vehicle):
            timestamp = prev_entry_time + timedelta(minutes=5)
            # Ensure that seconds end in 00
            timestamp = timestamp.replace(second=0)
            
            if i == 0:
                distance = 0
                prev_avg_speed = 0
            else:
                # Calculate distance based on the difference in latitude and longitude
                prev_entry = data[-1]
                distance = calculate_distance(prev_entry['latitude'], prev_entry['longitude'],
                                              random.uniform(52.46, 52.50), random.uniform(-1.93, -1.86))
                time_diff_hours = (timestamp - prev_entry_time).seconds / 3600
                prev_avg_speed = distance / time_diff_hours if time_diff_hours > 0 else 0
                
            # Determine ignition status
            if random.random() < 0.1:  # 10% chance of ignition being Off
                ignition_status = 'Off'
            else:
                ignition_status = 'On'
                
            # Determine current speed
            if ignition_status == 'Off':
                current_speed = 0
            else:
                current_speed = random.uniform(0, 65)
                
            # Calculate carbon emissions based on fuel type
            if fuel_type == 'Diesel':
                carbon_emissions = (distance / fuel_efficiency) * 2.68
            elif fuel_type == 'Petrol':
                carbon_emissions = (distance / fuel_efficiency) * 2.31
            else:
                carbon_emissions = 0
                
            # Format vehicle ID as 3-digit number with leading zeros
            vehicle_id_formatted = f"{vehicle_id:03}"
            
            data.append({'id': len(data) + 1, 'reg_number': vehicle_id_formatted, 'timestamp': timestamp, 
                         'latitude': random.uniform(52.46, 52.50), 'longitude': random.uniform(-1.93, -1.86),
                         'distance': distance, 'ignition': ignition_status, 'current_speed': current_speed,
                         'prev_avg_speed': prev_avg_speed, 'fuel_efficiency': fuel_efficiency, 
                         'fuel_type': fuel_type, 'carbon_emissions': carbon_emissions})
            
            prev_entry_time = timestamp
            
    return data

# Generate telematics data
telematics_data = generate_telematics_data()

# Create DataFrame
df = pd.DataFrame(telematics_data, columns=['id', 'reg_number', 'timestamp', 'latitude', 'longitude',
                                            'distance', 'ignition', 'current_speed', 'prev_avg_speed',
                                            'fuel_efficiency', 'fuel_type', 'carbon_emissions'])

# Export DataFrame to CSV
df.to_csv('telematics_data.csv', index=False)

# Display first few rows of the DataFrame
print(df.head())
