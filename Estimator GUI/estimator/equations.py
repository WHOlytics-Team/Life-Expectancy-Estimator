import numpy as np

def equation_advanced(
    year_input,
    infant_deaths_input,
    adult_mortality_input,
    bmi_input,
    polio_input,
    thinness_ten_nineteen_years_input,
    schooling_input,
    hiv_input,
    gdp_input,
    asia_input,
    central_america_and_caribbean_input,
    european_union_input,
    middle_east_input,
    north_america_input,
    oceania_input,
    rest_of_europe_input,
    south_america_input
):
    return (
        68.2364 +
        (0.1831 * ((year_input - 2007.5) / 4.610577)) +
        (-3.1212 * ((infant_deaths_input - 30.363792) / 27.538117)) +
        (-5.0882 * ((adult_mortality_input - 192.251775) / 114.910281)) +
        (-0.484 * ((bmi_input - 25.032926) / 2.193905)) +
        (0.1278 * ((polio_input - 86.499651) / 15.080365)) +
        (-0.0803 * ((thinness_ten_nineteen_years_input - 4.865852) / 4.438234)) +
        (0.4661 * ((schooling_input - 7.632123) / 3.171556)) +
        (-0.2834 * ((np.log(hiv_input) -1.594968) / 1.572341)) +
        (1.0065 * ((np.log(gdp_input) - 8.399358) / 1.444216)) +
        (0.443 * asia_input) +
        (1.9606 * central_america_and_caribbean_input) +
        (0.9536 * european_union_input) +
        (0.1072 * middle_east_input) +
        (1.8726 * north_america_input) +
        (-0.081 * oceania_input) +
        (0.6233 * rest_of_europe_input) +
        (1.6252 * south_america_input)
    )



def equation_sensitive(
    year_input,
    adult_mortality_input,
    bmi_input,
    polio_input, 
    gdp_input,
    asia_input,
    central_america_and_caribbean_input,
    european_union_input,
    middle_east_input,
    north_america_input,
    oceania_input,
    rest_of_europe_input,
    south_america_input
):
    return (
        67.0214 +
        (0.3767 * ((year_input - 2007.5) / 4.610577)) +
        (-5.9612 * ((adult_mortality_input - 192.251775) / 114.910281)) +
        (-0.0396 * ((bmi_input - 25.032926) / 2.193905)) +
        (1.2279 * ((polio_input - 86.499651) / 15.080365)) +
        (2.0575 * ((np.log(gdp_input) - 8.399358) / 1.444216)) +
        (0.443 * asia_input) +
        (1.9606 * central_america_and_caribbean_input) +
        (0.9536 * european_union_input) +
        (0.1072 * middle_east_input) +
        (1.8726 * north_america_input) +
        (-0.081 * oceania_input) +
        (0.6233 * rest_of_europe_input) +
        (1.6252 * south_america_input)
    )