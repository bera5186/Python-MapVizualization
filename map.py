"""
Folium is a python module for creating interactive map
vizualizations

"""
import folium

# create a map object
mapObject = folium.Map(location=[28.391263, 77.416735], zoom_start=12)

#create map markers
folium.Marker([28.410686, 76.703507],
            popup='<strong>Lingyas</strong>',
            icon=folium.Icon(icon='cloud'),
            tooltip='Click').add_to(mapObject)

folium.Marker([28.391263, 77.416735],
            popup='<strong>Aravali</strong>',
            tooltip='Click').add_to(mapObject)

folium.Marker([28.391263, 75.418335],
            popup='<strong>Aravali</strong>',
            icon=folium.Icon(color='purple'),
            tooltip='Click').add_to(mapObject)

folium.Marker([28.391263, 75.455555],
            popup='<strong>Aravali</strong>',
            icon=folium.Icon(color='green', icon='leaf'),
            tooltip='Click').add_to(mapObject)

folium.CircleMarker(
    location=[28.391215, 77.424063],
    popup='Hello',
    radius=30,
    color='#e3b2cc',
    fill=True,
    tooltip='pewpew'
).add_to(mapObject)



mapObject.save('map.html')