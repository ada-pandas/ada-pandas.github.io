# Title: How heavily polluted is the Earth’s atmosphere? Air Quality Data Analysis

# Abstract
By pollution of the Earth's atmosphere, we mean bringing new, uncharacteristic physical, chemical and biological substances into the air or changing their natural concentration. But what is the danger and why is it necessary to fight it? 
When we get oxygen by breathing in air of poor quality, pollutants enter the larynx and trachea through the nasopharynx. There, our blood takes particles of contaminated oxygen from the air and moves through the vessels and carries oxygen from the lungs to all organs. Thus, these emissions can cause severe health problems such as asthma, cardiovascular diseases and cancer, leading to serious health problems or even death. Therefore, the life expectancy of the population living in the contaminated regions is reduced. Moreover, according to the World Health Organization, approximately 4.2 million people in the world die every year due to air pollution.

These shocking facts confirm the relevance and importance of this problem. That is why we urgently need to limit the emission of harmful substances into the atmosphere, because the burning of coal, cement production and smelting of cast iron give us tangible benefits, but are these benefits really worth so many human lives?

In order to have a clear plan, we must firstly analyze the data on historical air quality, identify the pollution level dynamics, the main causes of environmental pollution, as well as the most problematic regions or even countries. The next step is to build a proper visualisation to send our results to the general public making a real impact.

# Research questions
How does the pollution level change over throughout the year and how did it change throughout the time period under consideration?

What is the correlation between the pollution level and different external factors (number of cars in cities, geographical position, presence of factories or thermoelectric power stations in the region, etc.)?

What are the common aspects of cities with different pollution levels (cluster analysis)?

# Dataset
The main dataset lists [AirQuality indexes](http://discomap.eea.europa.eu/map/fme/AirQualityExport.htm) for different European cities throughout the time (2013 - 2019). The granularisation is at the city level, approximatively 1 reading being done per day. The pollutants included are CO, NO, NO2, PB, PM10, PM2.5, SO2, THC ...

Not all cities have data for all the years and all pollutants.

We are going to use one ore more extra datasets that can provide us with different insights about some characteristics of the cities (number of inhabitants, cars ...): [European Cities Dataset](https://www.kaggle.com/roshansharma/europe-datasets)

# A list of internal milestones up until project milestone 2

1. Build crawler for downloading the dataset
2. Analyze the data, visualize it, see what insights we can get from it
3. Split the areas we can focus on, start working individually on those
4. Re-group, discuss the results
5. Work on visualizing the results
6. Combine everything into a report (with conclusion ~ what we can do do limit the effects of pollutants & provide a better future)

# Questions for TAa
1. We have a .py script that scrapes data from the web (the total size is about 0.3-0.4 TB). Can we run it on the cluster?
