import socket
import time
import os
import requests
from bs4 import BeautifulSoup
import urllib.request

timeout = 10
socket.setdefaulttimeout(timeout)

csv_counter = 0


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


country_codes = ['AD', 'AL', 'AT', 'BA', 'BE', 'BG', 'CH', 'CY', 'CZ', 'DE', 'DK', 'EE', 'ES', 'FI', 'FR', 'GB', 'GI',
                 'GR', 'HR', 'HU', 'IE', 'IS', 'IT', 'LT', 'LU', 'LV', 'ME', 'MK', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO',
                 'RS', 'SE', 'SI', 'SK', 'TR', 'XK']

pollutant_codes = {10: 'CO', 8: 'NO2', 7: 'O3', 1: 'SO2', 12: 'Pb', 7012: 'Pb', 2012: 'Pb',
                   6001: 'PM2.5', 5: 'PM10'}

pol2 = {'AD': [10, 8, 1, 5], 'AL': [10, 8, 7, 1, 5], 'AT': [10, 8, 7, 1, 5, 6001, 7012], 'BA': [10, 8, 7, 1, 5, 6001],
        'BE': [10, 8, 7, 1, 5, 6001], 'BG': [10, 8, 7, 1, 5, 6001], 'CH': [10, 8, 7, 1, 5, 6001],
        'CY': [10, 8, 7, 1, 12, 5, 6001], 'CZ': [8, 7, 1, 12, 5, 6001], 'DE': [10, 8, 12, 7, 1, 5, 6001],
        'DK': [10, 8, 12, 7, 1, 5, 6001], 'EE': [10, 8, 7, 1, 5, 6001], 'ES': [10, 8, 7, 1, 7012, 5, 6001],
        'FI': [10, 8, 7, 1, 5, 6001], 'FR': [10, 8, 7, 1, 5, 6001], 'GB': [10, 8, 7, 1, 7012, 6001],
        'GI': [10, 8, 7, 1, 5, 6001], 'GR': [10, 8, 7, 1, 12, 5, 6001], 'HR': [10, 8, 7, 1, 5, 6001],
        'HU': [10, 8, 7, 1, 5, 6001], 'IE': [10, 8, 7, 1, 7012, 5, 6001], 'IS': [10, 8, 1, 5, 6001],
        'IT': [10, 8, 1, 7, 5, 6001], 'LT': [10, 8, 1, 7, 5, 6001], 'LU': [10, 8, 1, 7, 5, 6001],
        'LV': [10, 8, 1, 7, 7012, 5, 6001], 'ME': [10, 8, 1, 7, 5], 'MK': [10, 8, 1, 7, 5, 6001],
        'MT': [10, 8, 1, 7, 5, 6001], 'NL': [10, 8, 1, 7, 2012, 5, 6001], 'NO': [10, 8, 1, 7, 5, 6001],
        'PL': [10, 8, 1, 7, 5, 6001], 'PT': [10, 8, 1, 7, 2012, 5, 6001], 'RO': [10, 8, 1, 7, 5, 6001],
        'RS': [10, 8, 1, 7, 5, 6001], 'SE': [10, 8, 1, 7, 2012, 5, 6001], 'SI': [10, 8, 1, 7, 7012, 5, 6001],
        'SK': [10, 8, 1, 7, 5, 6001], 'TR': [10, 8, 1, 7, 5, 6001], 'XK': [10, 8, 1, 7, 5, 6001]}

path = os.getcwd()

info_time = 'Year'
create_dir('data')

for country in country_codes:
    create_dir('data/' + country)
    for j in range(len(pol2[country])):
        time.sleep(2)
        create_dir('data/' + country + "/" + pollutant_codes[pol2[country][j]])
        reqs = requests.get(
            'https://fme.discomap.eea.europa.eu/fmedatastreaming/AirQualityDownload/AQData_Extract.fmw?CountryCode=' +
            country + '&CityName=&Pollutant=' + str(pol2[country][j]) + '&Year_from=2018&Year_to=2019&Station'
                                                                        '=&Samplingpoint=&Source=All&Output=HTML'
                                                                        '&UpdateDate=&TimeCoverage=' + info_time,
            timeout=10)
        html_content = reqs.content
        soup = BeautifulSoup(html_content, 'html.parser')
        csv_counter = 0
        for link in soup.find_all('a'):
            linkf = link.get('href')
            print("Downloading", linkf)
            try:
                req = urllib.request.Request(linkf, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'})
                html = urllib.request.urlopen(req).read()
                print("data/" + country + '/' + pollutant_codes[pol2[country][j]] + '/' + str(csv_counter) + '.csv')
                file_wr('data/' + country + '/' + pollutant_codes[pol2[country][j]] + '/', html)
            except urllib.error.HTTPError:
                print("Failed")
