import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.image import imread
from mpl_toolkits.basemap import Basemap

# Load the telematics dataset
df = pd.read_csv('telematics_data.csv')

# Load the background image
background_img = plt.imread('map.png')

# Create a Basemap instance with Mercator projection
m = Basemap(projection='merc', llcrnrlat=52.46, urcrnrlat=52.50,
            llcrnrlon=-1.93, urcrnrlon=-1.86, resolution='i')

# Plot the background image
plt.imshow(background_img, extent=[-1.93, -1.86, 52.46, 52.50])

# Plot heatmap of vehicle locations
x, y = m(df['Longitude'].values, df['Latitude'].values)
plt.scatter(x, y, alpha=0.5, color='red')  # Adjust color if needed

# Add a title
plt.title('Heatmap of Vehicle Locations')

# Save the map as a PNG image
plt.savefig('heatmap_on_map.png')
