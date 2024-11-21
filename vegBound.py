import pandas as pd
import geopandas as gpd
from shapely import wkt
import folium
import mapclassify
from matplotlib import pyplot as plt
from shapely.geometry import box

# Define your bounding box coordinates (in EPSG:4326, lat/lon)
xmin = -5.3572  # Min longitude
xmax = -5.2463  # Max longitude
ymin = 51.8436  # Min latitude
ymax = 51.9173  # Max latitude

# Load your CSV data
df = pd.read_csv('nrw_ph2_low_heath_veg.csv')

# Convert the 'geom' column to Shapely geometries
df['geometry'] = df['geom'].apply(wkt.loads)

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry='geometry')

# Set the CRS to EPSG:27700 (UK National Grid), reproject to EPSG:4326 (lat/lon)
gdf.set_crs('EPSG:27700', allow_override=True, inplace=True)
gdf = gdf.to_crs('EPSG:4326')

# Create the bounding box using the defined coordinates (in EPSG:4326)
bounding_box = box(xmin, ymin, xmax, ymax)

# Convert the bounding box into a GeoDataFrame
bbox_gdf = gpd.GeoDataFrame(geometry=[bounding_box], crs='EPSG:4326')

# Filter the GeoDataFrame using the bounding box to keep only vegetation polygons within the bounds
gdf_filtered = gdf[gdf.intersects(bbox_gdf.geometry[0])]

# Filter the GeoDataFrame to remove geom from displayed data
gdf_filtered = gdf_filtered.drop(columns=['geom'])

# Check the filtered data (make sure it's correct)
print(gdf_filtered.head())
print(gdf_filtered.columns)

# Now, use `explore()` to display only the filtered polygons on the map
m = gdf_filtered.explore(
    column='vegetation_type',  # Show vegetation type as the color coding
    cmap='viridis',  # Choose a color map for the data
    tiles='CartoDB positron',  # Set the basemap
    legend=True,  # Show the legend for the data
    attr="Map tiles by CartoDB, under ODbL. Data by OpenStreetMap."  # Add the attribution
)

# Save the map as an HTML file to view in the browser
m.save('interactive_map_with_vegetation_bbox.html')

print("Interactive map with vegetation data within the bounding box saved as 'interactive_map_with_vegetation_bbox.html'. Open this file in a web browser to view the map.")

# Optional: Plot the filtered data using matplotlib for quick visualization
gdf_filtered.plot()
plt.show()
