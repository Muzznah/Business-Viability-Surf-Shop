# Business Viability Analysis Surf-Shop
## Background
This analysis was conducted to determine the impact of weather and precipitation on, a surf and ice cream shop, being opened in Ohau. The key questions that need to be answered are could the weather and season, affect the surf and ice cream shop business. Specifically, are there certain times of the year when business might be slower, or the type of customer could be different? Will there be enough customers between seasons to sustain the business throughout the year?

## Resources
### Data:
- <[hawaii.sqlite](https://github.com/Muzznah/surfs_up/blob/master/hawaii.sqlite)>

### Software used:
- Python 3.7.7, sqlalchemy 1.3.17, Jupyter Notebook 6.0.3, pandas 1.0.3, numpy 1.18.1, matplotlib 3.1.3

## Analysis:
The analysis was done on the weather and precipitation data, of Oahu, from year 2010 to year 2017.
For detailed code check <[analysis.ipynb](https://github.com/Muzznah/surfs_up/blob/master/challenge_analysis.ipynb)>
### Precipitation:
The following table and graph, shows some key statistical measures, calculated, and plotted for the months of June and Dec.
![](https://github.com/Muzznah/surfs_up/blob/master/Analysis/Prcp.png)

![](https://github.com/Muzznah/surfs_up/blob/master/Analysis/Prcp_bar.png)

### Observation:
1.	From the table and plot, we can see that the measurement count for June is higher as compared to December.
2.	The average precipitation for June and Dec is, 0.14 and 0.22 (inches) respectively. Which falls in the category of light to moderate rain (light<=0.1 and moderate<=0.3 inches).
3.	Looking at the quartile ranges we can see that 75% of the observations were less than 0.12(for June) and 0.15(for Dec). which shows that most of the precipitation would be categorized as light rain. It also highlights that the average for the month of Dec is slightly spiked because of one or two large values.
4.	Quartile ranges show that the variation between the precipitation measurement for June and Dec is extremely low and they have almost similar readings.
5.	We do see a noticeable difference in the maximum readings, of both months but it gets discounted by the fact that that larger chunk (75%), of the readings of both months is similar.
6.	The higher standard deviation of Dec shows that it has a wider range of temperature data as compared to June.

### Temperature:
![](https://github.com/Muzznah/surfs_up/blob/master/Analysis/Temp.png)

![](https://github.com/Muzznah/surfs_up/blob/master/Analysis/Temp_bar.png)

### Observation:
1.	From the table and plot, we can see that the measurement count for June is higher as compared to December.
2.	The average temperature for June (75 F) is approximately 4 degree Fahrenheit higher as compared to Dec (71 F).
3.	The maximum temperature of June (85 F) and Dec (83 F) vary by 2-degree Fahrenheit only.
4.	The minimum temperature of June(F) and Dec( F) vary by 8 -degree Fahrenheit, which seems to be a significant difference, but if we look at Q1 values for both we see that not only the difference is again just 4 F but also that only 25% of values for Dec have a temperature <=69-degree Fahrenheit.
5.	Q3 values for both show a 3 F difference, it also tells us that the 75% readings are below 74 and 77 F.
6.	The higher standard deviation of Dec shows that it has a wider range of temperature data as compared to June.
## Summary:
The analysis showed that the seasonal variation between Dec and June is not significant, and that both the months had temperate average temperature and precipitation measurements.

## Recommendation:
1.	The analysis should be conducted on other months as well, as June and Dec might not be the right months for gauging seasonal variability.
2.	In addition to precipitation other weather parameters should be considered like wind speed and sunny days.
3.	To the answer the additional questions:

  a.	Are there certain times of the year when business might be slower?
  
  b.	or the type of customer could be different?
  
  c.	 Will there be enough customers between seasons to sustain the business throughout the year?
  
An analysis should be conducted on the number of tourists visiting in Dec as compared to June. For between the season’s customers would be local so checking if enough business comes from the local clientele. What competitors exist in the market and how are they performing.
