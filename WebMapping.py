#  AUTHOR:  Michael O'Brien
#  CREATED:  14 June 2018
#  UPDATED:  15 June 2018
#  DESCRIPTION:  Web mapping application


import pandas
import folium


greenways = pandas.read_csv('greenways.csv')


latitude = list(greenways['lat'])
longitude = list(greenways['lon'])
location = list(greenways['loc'])
distance = list(greenways['dist'])
typeOfTrail = list(greenways['type'])


def color_marker(tot):
    if tot == 'road':
        return 'green'
    else:
        return 'red'


map = folium.Map(location = [36.07, -86.60], zoom_start = 6, tiles = 'Mapbox Bright')
greenwayFeatureGroup = folium.FeatureGroup(name = 'Paved Greenways')


for lat, lon, loc, dist, tot in zip(latitude, longitude, location, distance, typeOfTrail):
    if tot == 'road':
        greenwayFeatureGroup.add_child(folium.Marker(location = [lat, lon], popup = folium.Popup(loc + '\n' + dist, parse_html = True), icon = folium.Icon(color_marker(tot))))

trailsFeatureGroup = folium.FeatureGroup(name = 'Mountain Bike Trails')

for lat, lon, loc, dist, tot in zip(latitude, longitude, location, distance, typeOfTrail):
    if tot == 'mtn bike':
        trailsFeatureGroup.add_child(folium.Marker(location = [lat, lon], popup = folium.Popup(loc + '\n' + dist, parse_html = True), icon = folium.Icon(color_marker(tot))))


mapLinesFeatureGroup = folium.FeatureGroup(name = 'Country Outlines')

mapLinesFeatureGroup.add_child(folium.GeoJson(data = open('world.json', encoding = 'utf-8-sig').read(), style_function = lambda x: {'fillColor':'yellow'}))


map.add_child(greenwayFeatureGroup)
map.add_child(trailsFeatureGroup)
map.add_child(mapLinesFeatureGroup)
map.add_child(folium.LayerControl())

map.save('map.html')
