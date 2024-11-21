import pandas as pd
import geopandas as gpd
from shapely import wkt
import folium
import mapclassify
from matplotlib import pyplot as plt

df = pd.read_csv('nrw_ph2_low_heath_veg.csv')

df['geometry'] = df['geom'].apply(wkt.loads)

gdf = gpd.GeoDataFrame(df, geometry='geometry')

gdf.set_crs('EPSG:27700', allow_override=True, inplace=True)

print(gdf.head())
print(gdf.columns)

m = gdf.explore(
    column='vegetation_type',  # Replace with the relevant column to visualize
    cmap='viridis',  # Choose a color map for the data
    tiles="Stamen Terrain",  # Set the basemap
    legend=True,  # Show the legend for the data
    attr="Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL."  # Add the attribution
)

m.save('interactive_map_output.html')

print("Interactive map saved as 'interactive_map_output.html'. Open this file in a web browser to view the map.")


gdf.plot()
plt.show()

