import numpy as np
import pandas as pd
import datetime
import folium
import json
from folium.plugins import TimestampedGeoJson
from branca.colormap import LinearColormap

avg_all = pd.read_csv("avg.csv", names=['Countrycode', 'Pollutant', 'Year', 'Month', 'Value'])
area = pd.read_csv("../area.csv")
avg_with_codes = pd.merge(area, avg_all, on="Countrycode")

with open("../json_data/world-countries.json", "r") as world_json:
    countries = json.load(world_json).get("features")
    world_json.close()
with open("../json_data/complementary.json", "r") as compl_json:
    compl = json.load(compl_json)
    compl_json.close()

pollutants = ['CO', 'NO2', 'O3', 'PM10', 'PM2.5', 'SO2']
color_scale = np.array(['#ffffd9', '#edf8b1', '#c7e9b4', '#7fcdbb', '#41b6c4', '#1d91c0', '#225ea8', '#253494',
                        '#081d58'])
scales = {'CO': np.linspace(200, 1600, 8), 'NO2': np.linspace(10, 80, 8), 'O3': np.linspace(15, 120, 8),
          'PM10': np.linspace(15, 120, 8), 'PM2.5': np.linspace(10, 80, 8), 'SO2': np.linspace(10, 80, 8)}
geo_dict = {}

for country in countries:
    geo_dict[country.get("id")] = country.get("geometry")


def color_coding(value):
    index = np.digitize(value, bin_edges, right=True)
    return color_scale[index]


def create_date(year, month):
    return datetime.datetime(year, month, 1)


date_vectorized = np.vectorize(create_date)

for pollutant in pollutants:
    avg = avg_with_codes[avg_with_codes["Pollutant"] == pollutant].copy()
    bin_edges = scales[pollutant]
    avg["Color"] = avg["Value"].apply(color_coding)
    avg["Datetime"] = date_vectorized(avg["Year"], avg["Month"])
    features = []
    for idx, row in avg.iterrows():
        if str(row["id"]) in geo_dict:
            feature = {
                'type': 'Feature',
                'geometry': geo_dict[row["id"]],
                'properties': {
                    'time': str(row['Datetime']),
                    'style': {'color': row['Color']}
                }
            }
            features.append(feature)
            if row["id"] in ["DNK", "FRA", "ITA", "GBR", "GRC"]:
                for geometry in compl.get(row["id"]).get("geometries"):
                    feature_new = dict(feature)
                    feature_new["geometry"] = geometry
                    features.append(feature_new)
    new_map = folium.Map([50.736455, 17.666], zoom_start=4.5)

    TimestampedGeoJson(
        {'type': 'FeatureCollection',
         'features': features},
        period='P1M', duration='P1M',
        add_last_point=True,
        auto_play=False,
        loop=False,
        max_speed=1,
        loop_button=True,
        date_options='YYYY/MM',
        time_slider_drag_update=True
    ).add_to(new_map)
    colormap = LinearColormap(color_scale, vmin=0, vmax=bin_edges[-1])
    colormap.caption = "Monthly average " + pollutant + " (in µg/m3)"
    colormap.add_to(new_map)
    new_map.save("../maps/avg_" + pollutant + ".html")
