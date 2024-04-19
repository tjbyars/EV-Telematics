import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from geopy.distance import geodesic

# Function to generate random timestamp within a given range
def random_timestamp(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

# Function to calculate distance between two coordinates
def calculate_distance(start_lat, start_lon, end_lat, end_lon):
    start_point = (start_lat, start_lon)
    end_point = (end_lat, end_lon)
    return geodesic(start_point, end_point).kilometers

# Generate random data for the dataset
def generate_telematics_data(num_vehicles=50, num_trips=100):
    data = []
    start_date = datetime(2024, 2, 1)
    end_date = datetime(2024, 2, 29)
    for vehicle_id in range(1, num_vehicles + 1):
        for _ in range(num_trips):
            start_time = random_timestamp(start_date, end_date)
            end_time = start_time + timedelta(minutes=random.randint(30, 120))
            start_lon = round(random.uniform(-1.91, -1.88), 6)
            start_lat = round(random.uniform(52.47, 52.49), 6)
            end_lon = round(random.uniform(-1.91, -1.88), 6)
            end_lat = round(random.uniform(52.47, 52.49), 6)
            
            distance_traveled = calculate_distance(start_lat, start_lon, end_lat, end_lon)
            time_diff_hours = (end_time - start_time).seconds / 3600
            avg_speed = distance_traveled / time_diff_hours if time_diff_hours > 0 else 0

            day_of_week = start_time.strftime('%A')
            vehicle_type = random.choice(['Sedan', 'SUV', 'Truck'])
            road_type = random.choice(['Urban', 'Rural'])
            weather_conditions = random.choice(['Clear', 'Cloudy', 'Rain'])
            
            data.append([vehicle_id, start_time, end_time, start_lon, start_lat, end_lon, end_lat,
                         avg_speed, day_of_week, vehicle_type, road_type, weather_conditions, distance_traveled])
    return data

# Generate telematics data
telematics_data = generate_telematics_data()

# Create DataFrame
columns = ['driver id', 'timestamp of trip start time', 'timestamp of trip end time', 
           'longitude of trip start', 'latitude of trip start', 'longitude of the trip end', 'latitude of the trip end', 
           'average speed', 'day of the week', 'vehicle type', 'road type', 'weather conditions', 'distance traveled']
df = pd.DataFrame(telematics_data, columns=columns)

# Export DataFrame to CSV
df.to_csv('telematics_data.csv', index=False)

# Display first few rows of the DataFrame
print(df.head())
