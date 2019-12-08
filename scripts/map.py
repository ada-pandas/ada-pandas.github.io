import folium
import pandas as pd

mymap = folium.Map([50.736455, 17.666], zoom_start=4.5)
stations = folium.FeatureGroup("Stations")

metadata = pd.read_csv("../data/metadata.csv")
metadata.drop_duplicates(["AirQualityStationEoICode"], inplace=True)
metadata.dropna(inplace=True)

for index, row in metadata.iterrows():
    stations.add_child(folium.Marker(row[["Latitude", "Longitude"]]))

mymap.add_child(stations)
mymap.save('../maps/map.html')
