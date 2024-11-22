import geopandas as gpd
import folium
import mapclassify
from matplotlib import pyplot as plt

# %%  
file = gpd.read_file('ComArea_ACS14_f.shp')
file = file[['community', 'Pop2014', 'Property_C', 'geometry']]
file = file.rename(columns={'community': 'Neighbourhood', 'Pop2014': 'Population in 2014', 'Property_C': 'Property Crime'})
print(file.head())
print(file.columns)


m = file.explore('Property Crime')
m.save('map_output.html')

print("Map saved as 'map_output.html'. Open this file in a web browser to view the map.")
