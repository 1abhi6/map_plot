from geopy.geocoders import ArcGIS
import folium

obj = ArcGIS()
locToBeSearched = input("Input the location to be searched: ")
s = obj.geocode(locToBeSearched)
map = folium.Map(location=[s.latitude, s.longitude], zoom_start=5)
map.add_child(folium.Marker(location=[s.latitude, s.longitude],
              popup=locToBeSearched.capitalize(), icon=folium.Icon(color="blue")))
map.save('index.html')
