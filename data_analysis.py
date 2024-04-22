import pandas as pd
import matplotlib.pyplot as plt

# Load the telematics dataset generated by the "generator" code
df = pd.read_csv('telematics_data.csv')

# Calculate average speed, average carbon emissions, total distance travelled, and total carbon emissions for each vehicle
avg_speed_per_vehicle = df.groupby('reg_number')['current_speed'].mean()
avg_carbon_emissions_per_vehicle = df.groupby('reg_number')['carbon_emissions'].mean()
total_distance_per_vehicle = df.groupby('reg_number')['distance'].sum()
total_carbon_emissions_per_vehicle = df.groupby('reg_number')['carbon_emissions'].sum()
avg_fuel_efficiency_per_vehicle = df.groupby('reg_number')['fuel_efficiency'].mean()
# Convert 'timestamp' column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Plot average speed of each vehicle
plt.figure(figsize=(10, 6))
avg_speed_per_vehicle.plot(kind='bar', color='skyblue')
plt.title('Average Speed of Each Vehicle')
plt.xlabel('Vehicle Registration Number')
plt.ylabel('Average Speed (km/h)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('avg_speed_per_vehicle.png')  # Save as PNG
plt.close()

# Plot average carbon emissions of each vehicle
plt.figure(figsize=(10, 6))
avg_carbon_emissions_per_vehicle.plot(kind='bar', color='lightgreen')
plt.title('Average Carbon Emissions of Each Vehicle')
plt.xlabel('Vehicle Registration Number')
plt.ylabel('Average Carbon Emissions (kg)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('avg_carbon_emissions_per_vehicle.png')  # Save as PNG
plt.close()

# Plot total distance travelled by each vehicle
plt.figure(figsize=(10, 6))
total_distance_per_vehicle.plot(kind='bar', color='orange')
plt.title('Total Distance Travelled by Each Vehicle')
plt.xlabel('Vehicle Registration Number')
plt.ylabel('Total Distance Travelled (km)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('total_distance_per_vehicle.png')  # Save as PNG
plt.close()

# Plot total carbon emissions of each vehicle
plt.figure(figsize=(10, 6))
total_carbon_emissions_per_vehicle.plot(kind='bar', color='lightcoral')
plt.title('Total Carbon Emissions of Each Vehicle')
plt.xlabel('Vehicle Registration Number')
plt.ylabel('Total Carbon Emissions (kg)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('total_carbon_emissions_per_vehicle.png')  # Save as PNG
plt.close()

# Plot fuel efficiency of each vehicle
plt.figure(figsize=(10, 6))
df.groupby('reg_number')['fuel_efficiency'].mean().plot(kind='bar', color='lightgreen')
plt.title('Fuel Efficiency of Each Vehicle')
plt.xlabel('Vehicle Registration Number')
plt.ylabel('Fuel Efficiency (km/L)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('fuel_efficiency_of_each_vehicle.png')  # Save as PNG
plt.close()

# Additional analysis/insights
# Example: Plotting distribution of fuel efficiency
plt.figure(figsize=(10, 6))
df['fuel_efficiency'].hist(bins=20, color='salmon', edgecolor='black')
plt.title('Distribution of Fuel Efficiency')
plt.xlabel('Fuel Efficiency (km/L)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('fuel_efficiency_distribution.png')  # Save as PNG
plt.close()

# Scatter Plot comparing Percent of Time with Engine On/Off to Total Carbon Emissions for each Vehicle
engine_on_percentage = df.groupby('reg_number')['ignition'].apply(lambda x: (x == 'On').mean() * 100)
plt.figure(figsize=(10, 6))
plt.scatter(engine_on_percentage, total_carbon_emissions_per_vehicle, color='red', alpha=0.5)
plt.title('Engine On/Off Percentage vs Total Carbon Emissions for each Vehicle')
plt.xlabel('Engine On Percentage (%)')
plt.ylabel('Total Carbon Emissions (kg)')
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('engine_on_percentage_vs_carbon_emissions.png')
plt.close()

# Plot heatmap of vehicle locations
background_img = plt.imread("map.png")
plt.figure(figsize=(10, 8))
plt.imshow(background_img, extent=[-1.93, -1.86, 52.46, 52.50])
plt.scatter(df['longitude'], df['latitude'], c='red', alpha=0.5)
plt.title('Heatmap of Vehicle Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('vehicle_locations_heatmap.png')
plt.close()

# Calculate carbon emissions by hour
df['hour'] = df['timestamp'].dt.hour
carbon_emissions_by_hour = df.groupby('hour')['carbon_emissions'].sum()

# Plot carbon emissions by hour
plt.figure(figsize=(10, 6))
carbon_emissions_by_hour.plot(kind='bar', color='lightblue')
plt.title('Carbon Emissions by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Total Carbon Emissions (kg)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('carbon_emissions_by_hour.png')  # Save as PNG
plt.close()

# Calculate carbon emissions by day
df['day'] = df['timestamp'].dt.date
carbon_emissions_by_day = df.groupby(df['timestamp'].dt.date)['carbon_emissions'].sum()

# Plot carbon emissions by day
plt.figure(figsize=(10, 6))
carbon_emissions_by_day.plot(kind='bar', color='lightgreen')
plt.title('Carbon Emissions by Day')
plt.xlabel('Date')
plt.ylabel('Total Carbon Emissions (kg)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('carbon_emissions_by_day.png')  # Save as PNG
plt.close()

# Plot total distance vs total carbon emissions per vehicle
total_distance_per_vehicle = df.groupby('reg_number')['distance'].sum()
total_carbon_emissions_per_vehicle = df.groupby('reg_number')['carbon_emissions'].sum()
plt.figure(figsize=(10, 6))
plt.scatter(total_distance_per_vehicle, total_carbon_emissions_per_vehicle, color='purple', alpha=0.7)
plt.title('Total Distance vs Total Carbon Emissions per Vehicle')
plt.xlabel('Total Distance Travelled (km)')
plt.ylabel('Total Carbon Emissions (kg)')
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('total_distance_vs_carbon_emissions_per_vehicle.png')  # Save as PNG
plt.close()

# Filter dataset for the week of April 1st to April 7th
start_date = '2024-04-01'
end_date = '2024-04-07'
week_data = df[(df['timestamp'] >= start_date) & (df['timestamp'] <= end_date)]

# Group data by hourly intervals and calculate total carbon emissions
hourly_carbon_emissions = week_data.resample('h', on='timestamp')['carbon_emissions'].sum()

# Plot the energy curve (carbon emissions over time)
plt.figure(figsize=(12, 6))
hourly_carbon_emissions.plot(color='blue')
plt.title('Energy Curve: Carbon Emissions Over Time (April 1st - April 7th)')
plt.xlabel('Time')
plt.ylabel('Total Carbon Emissions (kg)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('energy_curve_carbon_emissions.png')  # Save as PNG
plt.close()

# Group data by hour of the day and calculate average carbon emissions
hourly_avg_carbon_emissions = df.groupby(df['timestamp'].dt.hour)['carbon_emissions'].mean()

# Plot the energy curve variation by hour of the day
plt.figure(figsize=(10, 6))
hourly_avg_carbon_emissions.plot(kind='bar', color='green')
plt.title('Energy Curve Variation by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Carbon Emissions (kg)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('energy_curve_variation_by_hour.png')  # Save as PNG
plt.close()
