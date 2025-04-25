import numpy as np

def equation1(
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


def equation2(
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


def get_data_advanced():
    print("🌍 Please select your region:")
    region_dict = {
        0: 'Africa', 1: 'Asia', 2: 'Central America and Caribbean',
        3: 'European Union', 4: 'Middle East', 5: 'North America',
        6: 'Oceania', 7: 'Rest of Europe', 8: 'South America'
    }

    for k, v in region_dict.items():
        print(f" {k}. {v}")
    region_number = int(input("Enter region number (0-8): "))
    
    region_flags = [0] * 9
    region_flags[region_number] = 1

    year = int(input("Enter the year (e.g. 2015): "))
    infant_deaths = float(input("Enter infant deaths per 1000 live births: "))
    adult_mortality = float(input("Enter adult mortality rate: "))
    bmi = float(input("Enter average BMI: "))
    polio = float(input("Enter polio immunization coverage (%): "))
    thinness = float(input("Enter thinness 10-19 years (%): "))
    schooling = float(input("Enter average years of schooling: "))
    hiv = float(input("Enter HIV/AIDS prevalence rate: "))
    gdp = float(input("Enter GDP per capita: "))

    return {
        "year_input": year,
        "infant_deaths_input": infant_deaths,
        "adult_mortality_input": adult_mortality,
        "bmi_input": bmi,
        "polio_input": polio,
        "thinness_ten_nineteen_years_input": thinness,
        "schooling_input": schooling,
        "hiv_input": hiv,
        "gdp_input": gdp,
        "asia_input": region_flags[1],
        "central_america_and_caribbean_input": region_flags[2],
        "european_union_input": region_flags[3],
        "middle_east_input": region_flags[4],
        "north_america_input": region_flags[5],
        "oceania_input": region_flags[6],
        "rest_of_europe_input": region_flags[7],
        "south_america_input": region_flags[8]
    }


def main():
    print("👋 Welcome to WHOlytics Life Expectancy Predictor!")
    inputs = get_data_advanced()
    
    print("\nRunning predictions...\n")
    result1 = equation1(**inputs)
    result2 = equation2(
        inputs["year_input"],
        inputs["adult_mortality_input"],
        inputs["bmi_input"],
        inputs["polio_input"],
        inputs["gdp_input"],
        inputs["asia_input"],
        inputs["central_america_and_caribbean_input"],
        inputs["european_union_input"],
        inputs["middle_east_input"],
        inputs["north_america_input"],
        inputs["oceania_input"],
        inputs["rest_of_europe_input"],
        inputs["south_america_input"]
    )
    
    print(f"🔮 Prediction using Equation 1: {result1:.2f} years")
    print(f"🔮 Prediction using Equation 2: {result2:.2f} years")


if __name__ == "__main__":
    main()
