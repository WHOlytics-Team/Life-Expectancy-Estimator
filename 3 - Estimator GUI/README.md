# WHOlytics Life Expectancy Prediction Model
(modelled on data for each country between 2000 - 2015)

Thanks for using our model to predict the life expectancy for your country. Please note all metrics should be calculated on an annual basis specific to the year you want to predict for. 

Please be informed that you will be required to provide the following information at <I> minimum </I> for the model to predict:

- The <B>region</B> your country is in (Africa, Asia etc.);
- The <B>year</B> you would like to predict your country's life expectancy for;
- Your country's <B>adult mortality rate</B> per 1000 population;
- Your country's <B>Polio (Pol3) immunization</B> coverage among 1-year-olds as a percentage;
- Your country's <B>average Body Mass Index (BMI)</B>; and
- Your country's <B>Gross Domestic Product (GDP) per capita (in USD)</B>

If you would like to use the advanced model, you will be required to provide the following <I>additional</I> information:

- Your country's number of <B>infant deaths</B> per 1000 population;
- The number of deaths per 1,000 live births due to <B>HIV/AIDS</B> for children aged 0-4 in your country;
- The percentage <B>prevalence of thinness</B> among children and adolescents (ages 10 to 19) in your country; and
- The average years of number of <B>years of schooling</B> in your country.

---

**Please note that you can input the data as a JSON string if preferable, please see examples below:**

For Advanced Mode: (JSON Data Example):
```
{"region": "Africa", "region_africa": 0, "year": 2006, "adult_mortality": 515.718, "infant_deaths": 48.7, "polio": 79.0, "incidents_hiv": 11.13, "bmi": 26.6, "thinness_ten_nineteen_years": 1.6, "schooling": 9.0, "gdp_per_capita": 5827.0}
```
For Sensitive Mode: (JSON Data Example):
```
{"region": "South America", "region_south_america": 1, "year": 2012, "adult_mortality": 150.2245, "polio": 96, "bmi": 26.1, "gdp_per_capita": 9057.0}
```
Please note that the region should be inputed into the JSON string in the following pairs for accurate data entry - this is due to the One-hot encoding (OHE) of the region columns:

```
"region": "Africa", "region_africa": 0
"region": "Asia", "region_asia": 1
"region": "Central America and Caribbean", "region_central_america_and_caribbean": 1
"region": "European Union", "region_european_union": 1
"region": "Middle East", "region_middle_east": 1
"region": "North America", "region_north_america": 1
"region": "Oceania", "region_oceania": 1
"region": "Rest of Europe","region_rest_of_europe": 1
"region": "South America", "region_south_america": 1
```

Run the program in Terminal

---

Please run from **the folder "3 - Estimator GUI"** containing `main.py`

```
python3 main.py
```

