"""
This script scrapes air pollution data on the following (the most common) pollutants: CO (carbon monoxide),
NO2 (nitrogen dioxide), O3 (ozone), SO2 (sulphur dioxide), PM10 and PM2.5 (particulate matter of different diameter),
Pb (lead) from all available countries. Each country is denoted by a unique 2-letter code, each pollutant is denoted by
an integer number (not always unique, see pollutant_codes). This script groups the results first by country, then by
substance. It requires requests, urllib and bs4 to be installed.
"""

import socket
import time
import os
import requests
from bs4 import BeautifulSoup
import urllib.request
import traceback

timeout = 10
socket.setdefaulttimeout(timeout)

csv_counter = 0
file_failed = open("failed.txt", "w+")

def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print("Directory", dir_name, "created ")
    else:
        print("Directory", dir_name, "already exists")


def file_wr(filename, infos):
    global csv_counter

    csv_counter += 1
    fp = open(filename + '' + str(csv_counter) + '.csv', 'wb+')
    fp.write(infos)
    fp.close()
    print("Finished")


def file_read(filename):
    with urllib.request.urlopen(filename) as response:
        return response


def retry_failed(list_of_failed_downloads):
    for item in list_of_failed_downloads:
        try:
            print("Retrying download " + item[0])
            urllib.request.urlretrieve(item[0], item[1] + ".csv")
            print("Finished")
        except Exception:
            traceback.print_exc()
            file_failed.write(item[0] + ' ' + item[1] + "\n")
            print("Failed")


country_codes = ['AD', 'AL', 'AT', 'BA', 'BE', 'BG', 'CH', 'CY', 'CZ', 'DE',
                 'DK', 'EE', 'ES', 'FI', 'FR', 'GB', 'GI', 'GR', 'HR', 'HU',
                 'IE', 'IS', 'IT', 'LT', 'LU', 'LV', 'ME', 'MK', 'MT', 'NL',
                 'NO', 'PL', 'PT', 'RO', 'RS', 'SE', 'SI', 'SK', 'TR', 'XK']



pollutant_codes = {10: 'CO', 8: 'NO2', 7: 'O3', 1: 'SO2', 12: 'Pb', 7012: 'Pb', 2012: 'Pb',
                   6001: 'PM2.5', 5: 'PM10'}

#list_of_available_pollutants = {'AD': [10, 8, 1, 5], 
#                                'AL': [10, 8, 7, 1, 5],
#                                'AT': [10, 8, 7, 1, 5, 6001, 7012],
#                                'BA': [10, 8, 7, 1, 5, 6001],
#                                'BE': [10, 8, 7, 1, 5, 6001], 
#                                'BG': [10, 8, 7, 1, 5, 6001],
#                                'CH': [10, 8, 7, 1, 5, 6001],
#                                'CY': [10, 8, 7, 1, 12, 5, 6001],
#                                'CZ': [8, 7, 1, 12, 5, 6001],
#                                'DE': [10, 8, 12, 7, 1, 5, 6001],
#                                'DK': [10, 8, 12, 7, 1, 5, 6001], 
#                                'EE': [10, 8, 7, 1, 5, 6001],
#                                'ES': [10, 8, 7, 1, 7012, 5, 6001],
#                                'FI': [10, 8, 7, 1, 5, 6001], 
#                                'FR': [10, 8, 7, 1, 5, 6001],
#                                'GB': [10, 8, 7, 1, 7012, 6001],
#                                'GI': [10, 8, 7, 1, 5, 6001],
#                                'GR': [10, 8, 7, 1, 12, 5, 6001],
#                                'HR': [10, 8, 7, 1, 5, 6001],
#                                'HU': [10, 8, 7, 1, 5, 6001],
#                                'IE': [10, 8, 7, 1, 7012, 5, 6001],
#                                'IS': [10, 8, 1, 5, 6001],
#                                'IT': [10, 8, 1, 7, 5, 6001],
#                                'LT': [10, 8, 1, 7, 5, 6001],
#                                'LU': [10, 8, 1, 7, 5, 6001],
#                                'LV': [10, 8, 1, 7, 7012, 5, 6001],
#                                'ME': [10, 8, 1, 7, 5],
#                                'MK': [10, 8, 1, 7, 5, 6001],
#                                'MT': [10, 8, 1, 7, 5, 6001], 
#                                'NL': [10, 8, 1, 7, 2012, 5, 6001],
#                                'NO': [10, 8, 1, 7, 5, 6001],
#                                'PL': [10, 8, 1, 7, 5, 6001], 
#                                'PT': [10, 8, 1, 7, 2012, 5, 6001],
#                                'RO': [10, 8, 1, 7, 5, 6001],
#                                'RS': [10, 8, 1, 7, 5, 6001],
#                                'SE': [10, 8, 1, 7, 2012, 5, 6001],
#                                'SI': [10, 8, 1, 7, 7012, 5, 6001],
#                                'SK': [10, 8, 1, 7, 5, 6001],
#                                'TR': [10, 8, 1, 7, 5, 6001],
#                                'XK': [10, 8, 1, 7, 5, 6001]}

list_of_available_pollutants = {'AD': [10, 8, 1, 5], 
                                'AL': [10, 8, 1, 5],
                                'AT': [10, 8, 1, 5],
                                'BA': [10, 8, 1, 5],
                                'BE': [10, 8, 1, 5], 
                                'BG': [10, 8, 1, 5],
                                'CH': [10, 8, 1, 5],
                                'CY': [10, 8, 1, 5],
                                'CZ': [10, 8, 1, 5],
                                'DE': [10, 8, 1, 5],
                                'DK': [10, 8, 1, 5],
                                'EE': [10, 8, 1, 5],
                                'ES': [10, 8, 1, 5],
                                'FI': [10, 8, 1, 5],
                                'FR': [10, 8, 1, 5],
                                'GB': [10, 8, 1, 5],
                                'GI': [10, 8, 1, 5],
                                'GR': [10, 8, 1, 5],
                                'HR': [10, 8, 1, 5],
                                'HU': [10, 8, 1, 5]}

info_time = 'Year'
create_dir('data')

print("Downloading metadata")
try:
    urllib.request.urlretrieve("https://ereporting.blob.core.windows.net/downloadservice/metadata.csv",
                               'data/metadata.csv')
    print("Finished")
except urllib.error.HTTPError:
    print("Failed")


for country in country_codes[:19]:
    create_dir('data/' + country)
    for j in range(len(list_of_available_pollutants[country])):
        failed_downloads = []
        time.sleep(2)
        create_dir('data/' + country + "/" + pollutant_codes[list_of_available_pollutants[country][j]])
        try:
            reqs = requests.get(
                'https://fme.discomap.eea.europa.eu/fmedatastreaming/AirQualityDownload/AQData_Extract.fmw?CountryCode=' +
                country + '&CityName=&Pollutant=' + str(
                    list_of_available_pollutants[country][j]) + '&Year_from=2018&Year_to=2019&Station'
                                                                '=&Samplingpoint=&Source=All&Output=HTML'
                                                                '&UpdateDate=&TimeCoverage=' + info_time,
                timeout=10)
        except:
            print("Request failed")
            continue
        html_content = reqs.content
        soup = BeautifulSoup(html_content, 'html.parser')
        csv_counter = 0
        path = "data/" + country + '/' + pollutant_codes[list_of_available_pollutants[country][j]] + '/'
        for link in soup.find_all('a'):
            linkf = link.get('href')
            print("Downloading", linkf)
            try:
                req = urllib.request.Request(linkf, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/47.0.2526.106 Safari/537.36'})
                html = urllib.request.urlopen(req).read()
                print(path + str(csv_counter) + '.csv')
                file_wr(path, html)
            except:
                failed_downloads.append((linkf, path + str(csv_counter)))
                print("Failed")

        retry_failed(failed_downloads)

file_failed.close()
