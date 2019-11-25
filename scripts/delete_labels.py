def rename_csv(filename):
    return "0" * (8 - len(filename)) + filename

import os
import shutil

#pepega = open("data_min/GB/CO/2.csv", 'r', encoding="utf-16")
#print(pepega.readline())

countries = os.listdir("./data_min")
for country in countries:
    path_1 = "./data_min/" + country
    pollutants = os.listdir(path_1)
    for pollutant in pollutants:
        path_2 = path_1 + "/" + pollutant
        files = os.listdir(path_2)
        for file in files:
            path_3 = path_2 + "/" + file
            print(file)
            try:
                source_file = open(path_3, 'r', encoding="utf-16")
                source_file.readline()
            except:
                source_file = open(path_3, 'r', encoding="utf-8")
                source_file.readline()
            # this will truncate the file, so need to use a different file name:
            target_file = open(path_2 + "/" + rename_csv(file), 'w', encoding="utf-8")
            shutil.copyfileobj(source_file, target_file)
            source_file.close()
            target_file.close()
            os.remove(path_3)
