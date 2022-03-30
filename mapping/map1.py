
from unicodedata import name
import pandas
import folium
from pyparsing import And
map=folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="OpenStreetMap")
fgv=folium.FeatureGroup(name="Volcanoes")
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
elev=list(data["ELEV"])
def color_producer(elevation):
    if elevation<1500:
       return 'green'
    elif  1500<=elevation<3000:
        return 'orange'
    else:
        return 'red'


for lt,ln,na,el  in zip(lat,lon,name,elev):  
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=na+" "+ str(el)+"m",fill_color=color_producer(el),fill=True,fill_opacity=0.7,radius=8,color='grey'))


fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'yellow'  if 10000000<=x['properties']['POP2005']<50000000 else  'red'}))
# fill ccolor is not in the json file we are accessing,we can add the attribute we need.
map.add_child(fgv)
map.add_child(fgp)
# we have changed fg to fgv and fgp to access the objects seprately
# and use them in the layer control seperately.

# it is important to add the feature group b4 adding the layer contro👆
# layer control
# layer control looks for objects added to map
map.add_child(folium.LayerControl())

map.save("practiceMap.html")























# fg.add_child(folium.CircleMarker(location=coordinates,    color="#3186cc", fill=True,fill_color="#3186cc",radius=50))
    # fg.add_child(folium.LatLngPopup())
    # fg.add_child(folium.ClickForMarker(popup="Waypoint"))

