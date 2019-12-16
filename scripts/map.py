import folium
import pandas as pd

mymap = folium.Map([50.736455, 17.666], zoom_start=4.5)
stations = folium.FeatureGroup("Stations")

metadata = pd.read_csv("metadata.csv", sep="\t")
#metadata.dropna(inplace=True)
metadata.drop_duplicates(["AirQualityStationEoICode"], inplace=True)
metadata.to_csv("pogchamp.csv")

for index, row in metadata.iterrows():
    stations.add_child(folium.Marker(row[["Latitude", "Longitude"]]))

mymap.add_child(stations)
mymap.save('../maps/map1.html')
