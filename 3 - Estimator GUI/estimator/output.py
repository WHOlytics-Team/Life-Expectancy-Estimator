from estimator.inputs import get_data_advanced, get_data_sensitive
from estimator.equations import equation_advanced, equation_sensitive
import json

def start_predict():
    print("🌟 Welcome to the Life Expectancy Predictor! 🌟")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    input_data = None
    life_expectancy = None

    try:
        while True:
            print("🔍 This tool helps predict life expectancy based on your data! \n")
            use_advanced = input(
                "🤔 Do you consent to using advanced population data (including protected info) for better accuracy? (Y/N): \n"
            ).strip().lower()

            # Decide which function to call based on consent
            if use_advanced == 'y':
                print("✨ You've chosen the advanced mode! Collecting detailed data... 🌍 \n")
                use_dict = input("\n Do you want to enter the data in the format of a dictionary? (Y/N) \n")
                if use_dict.lower() == 'y':
                    input_dict = input('Please ensure that the JSON dictionary is of the following example format (JSON string): {"region": "Africa", "region_africa": 0, "year": 2006, "adult_mortality": 515.718, "infant_deaths": 48.7, "polio": 79.0, "incidents_hiv": 11.13, "bmi": 26.6, "thinness_ten_nineteen_years": 1.6, "schooling": 9.0, "gdp_per_capita": 5827.0} \n')
                    input_data = json.loads(input_dict)
                elif use_dict.lower() == 'n':
                    input_data = get_data_advanced()
                life_expectancy = equation_advanced(
                    year_input=input_data.get('year'),
                    infant_deaths_input=input_data.get('infant_deaths', 30.363792),
                    adult_mortality_input=input_data.get('adult_mortality', 192.251775),
                    bmi_input=input_data.get('bmi', 25.032926),
                    polio_input=input_data.get('polio', 86.499651),
                    thinness_ten_nineteen_years_input=input_data.get('thinness_ten_nineteen_years', 4.865852),
                    schooling_input=input_data.get('schooling', 7.632123),
                    hiv_input=input_data.get('incidents_hiv', 0.8942877094972066),
                    gdp_input=input_data.get('gdp_per_capita', 11540.924930167597),
                    asia_input=input_data.get('region_asia', 0),
                    central_america_and_caribbean_input=input_data.get('region_central_america_and_caribbean', 0),
                    european_union_input=input_data.get('region_european_union', 0),
                    middle_east_input=input_data.get('region_middle_east', 0),
                    north_america_input=input_data.get('region_north_america', 0),
                    oceania_input=input_data.get('region_oceania', 0),
                    rest_of_europe_input=input_data.get('region_rest_of_europe', 0),
                    south_america_input=input_data.get('region_south_america', 0)
                )
                break
            elif use_advanced == 'n':
                print("📋 You've chosen the basic mode! Collecting essential data... 🌎 \n")
                use_dict = input("\n Do you want to enter the data in the format of a dictionary? (Y/N) \n")
                if use_dict.lower() == 'y':
                    input_dict = input('Please ensure that the JSON dictionary is of the following example format (JSON string): {"region": "Africa", "region_africa": 0, "year": 2006, "adult_mortality": 515.718, "polio": 79.0, "bmi": 26.6, "gdp_per_capita": 5827.0} \n')
                    input_data = json.loads(input_dict)
                elif use_dict.lower() == 'n':
                    input_data = get_data_sensitive()
                
                life_expectancy = equation_sensitive(
                year_input=input_data.get('year'),
                adult_mortality_input=input_data.get('adult_mortality', 192.251775),
                bmi_input=input_data.get('bmi', 25.032926),
                polio_input=input_data.get('polio', 86.499651),
                gdp_input=input_data.get('gdp_per_capita', 11540.924930167597),
                asia_input=input_data.get('region_asia', 0),
                central_america_and_caribbean_input=input_data.get('region_central_america_and_caribbean', 0),
                european_union_input=input_data.get('region_european_union', 0),
                middle_east_input=input_data.get('region_middle_east', 0),
                north_america_input=input_data.get('region_north_america', 0),
                oceania_input=input_data.get('region_oceania', 0),
                rest_of_europe_input=input_data.get('region_rest_of_europe', 0),
                south_america_input=input_data.get('region_south_america', 0)
                )
                break
            else:
                print("🚫 Invalid input. Please enter 'Y' or 'N'.")

    except ValueError as e:
        print(f"⚠️ A value error occurred: {e}")
    except Exception as e:
        print(f"❗ An unexpected error occurred: {e}")
    
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    print("📊 Here are the results based on the data provided: \n")
    if input_data:
        output_message = "🌏✨ WORLD HEALTH DATA INSIGHTS ✨🌏\n"
        output_message += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" 
        output_message += "📊 KEY DATA COLLECTED:\n"
        for key, value in input_data.items():
            if key not in [
                "region_africa",
                "region_asia",
                "region_central_america_and_caribbean",
                "region_european_union",
                "region_middle_east",
                "region_north_america",
                "region_oceania",
                "region_rest_of_europe",
                "region_south_america",
            ]:
                # Format each key-value pair
                formatted_key = key.replace('_', ' ').title().replace('Hiv', 'HIV').replace('Bmi', 'BMI').replace('Gdp', 'GDP')
                output_message += f"★ {formatted_key} ➡️ {value}\n"
                
        output_message += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"

        year = input_data.get('year', 'N/A')
        region = input_data.get('region', 'N/A')

        output_message += "\n⚡ LIFE EXPECTANCY REPORT ⚡\n"
        output_message += f"🏯 Region: {region.upper()}\n"
        output_message += f"🗓️ Year: {year}\n"
        output_message += f"🎉 PREDICTED LIFE EXPECTANCY: {life_expectancy:.2f} YEARS\n"
        output_message += "\nThis analysis contributes to WHO's mission to monitor and improve global health. 🌍✨\n"
        output_message += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        output_message += "THANK YOU FOR BEING PART OF A HEALTHIER WORLD!\n"
        print(output_message)
    else:
        print("No data available to display.")


def print_output(input_data, life_expectancy):
    if input_data:
        output_message = "🌏✨ WORLD HEALTH DATA INSIGHTS ✨🌏\n"
        output_message += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" 
        output_message += "📊 KEY DATA COLLECTED:\n"
        for key, value in input_data.items():
            if key not in [
                "region_africa",
                "region_asia",
                "region_central_america_and_caribbean",
                "region_european_union",
                "region_middle_east",
                "region_north_america",
                "region_oceania",
                "region_rest_of_europe",
                "region_south_america",
            ]:
                # Format each key-value pair
                formatted_key = key.replace('_', ' ').title().replace('Hiv', 'HIV').replace('Bmi', 'BMI').replace('Gdp', 'GDP')
                output_message += f"★ {formatted_key} ➡️ {value}\n"
                
        output_message += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"

        year = input_data.get('year', 'N/A')
        region = input_data.get('region', 'N/A')

        output_message += "\n⚡ LIFE EXPECTANCY REPORT ⚡\n"
        output_message += f"🏯 Region: {region.upper()}\n"
        output_message += f"🗓️ Year: {year}\n"
        output_message += f"🎉 PREDICTED LIFE EXPECTANCY: {life_expectancy:.2f} YEARS\n"
        output_message += "\n🌀 This analysis contributes to WHO's mission to monitor and improve global health. 🌍✨\n"
        output_message += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        output_message += "🔥 THANK YOU FOR BEING PART OF A HEALTHIER WORLD! 💪⚡\n"
        print(output_message)
    else:
        print("No data available to display.")