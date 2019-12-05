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

1. Build crawler for downloading the dataset [DONE]
2. Analyze the data, visualize it, see what insights we can get from it [DONE]
3. Split the areas we can focus on, start working individually on those [DONE]
4. Re-group, discuss the results [DONE]
5. Work on visualizing the results [DONE]
6. Combine everything into a report (with conclusion ~ what we can do do limit the effects of pollutants & provide a better future) [WORK-IN-PROGRESS]


# Milestone 2 aspects
The dataset that we have chosen is pretty broad as it offers plently of areas to dig in and investigate. 

**Until now he have focused on**:
The dataset that we have chosen is pretty broad as it offers plenty of areas to dig in and investigate. 

**Until now we have focused on**:
1. How to get the data; the whole dataset has 250GB, so we needed to put the dataset on the cluster and on our machine to only work with a subset of the data (that can by filter by the country or timestamp)
2. Clean the data
3. Do preliminary analysis and investigate further areas that we can focus on
4. Visualization pollutants level through time
5. Geoplot pollutants levels (also make use of the spatial coordinates we can link the pollutants level to - initial work)


In terms of analysis the first action point that was to focus only on a specific area (we choose Switzerland) and see each pollutant value. 

We looked at the histogram of pollutants value and analyze if the most found values are within healthy parameters. 

Then we took different time intervals and see how pollutants vary through time (24 hrs period, a few days, a few years). During this investigation we found some trends like the CO levels increasing during the summer. We validated this assumption by searching online for possible reasons and summer wildfire is the biggest cause of such an increase.

**What we want to focus on for Milestone 3 and presentation**
 
 1. We have decided to dig deeper into CO increased levels during the summer, thus we want to cross-reference the periods with elevated CO values with fire events, also load data from different countries that are closer to the sources of these fire and see if we can correlate a bigger increase in those areas (as they are closed to the source of the fires)

 2. Until now we mainly focused on the time variation, we are going to start and load data from different places and analyze the geographical aspects that cause pollutants to stick to certain levels.

 3. As we are aiming for a data story, our research is headed towards finding specific action points that we as citizens should be aware of into trying to make the world a better place (learn from the mistakes of others / the good policies that other countries have in place to limit certain pollutants levels)


# Questions for TAa
1. We have a .py script that scrapes data from the web (the total size is about 0.3-0.4 TB). Can we run it on the cluster?
