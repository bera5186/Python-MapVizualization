"""
Folium is a python module for creating interactive map
vizualizations

"""
import folium

# create a map object
mapObject = folium.Map(location=[15.490053, 73.821448], zoom_start=12)

mapObject.save('map.html')