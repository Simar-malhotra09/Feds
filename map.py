import os
import json
import folium
from folium.plugins import MousePosition

map = folium.Map(location=[40.6473, -96.67969], zoom_start=5)
with open("fed_loc.json") as file:
    fed_banks= json.load(file) 
MousePosition().add_to(map)
for bank in fed_banks["FRB"]:
    folium.Marker(
        location=bank["coordinates"],
        popup=bank["name"],
        icon=folium.Icon(color="blue")
    ).add_to(map)
map.save("index.html")
