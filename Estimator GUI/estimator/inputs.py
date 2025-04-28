def get_data_advanced():
    country_data = {}
    # REGION
    while True:
        try:
            region_dict = {
                0: 'Africa', 1: 'Asia', 2: 'Central America and Caribbean',
                3: 'European Union', 4: 'Middle East', 5: 'North America',
                6: 'Oceania', 7: 'Rest of Europe', 8: 'South America'
            }
            region_number = int(input(
            "🌍 Please enter the number that best represents the region of your country out of the following: (0-8):\n"
            " 0. Africa \n"
            " 1. Asia \n"
            " 2. Central America and Caribbean \n"
            " 3. European Union \n"
            " 4. Middle East \n"
            " 5. North America \n"
            " 6. Oceania \n"
            " 7. Rest of Europe \n"
            " 8. South America \n ➡️"
        ))
            if 0 <= region_number <= 8:
                country_data['region'] = region_dict[region_number]
                for key in region_dict:
                    country_data[f"region_{region_dict[key].replace(' ', '_').lower()}"] = (key == region_number)
                break
            else:
                print("🚫 Invalid input. Please enter a number between 0 and 8.")
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")

    # YEAR
    while True:
        try:
            year = int(input("\n📅 Please enter the year of the dataset you would like to predict for in number format, any year from 2000 onwards (2000 or later): ➡️ "))
            if year >= 2000:
                country_data['year'] = year
                break
            else:
                print("🚫 Invalid input. The year must be 2000 or later.")
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")

    # ADULT MORTALITY
    while True:
        try:
            adult_mortality = float(input("\n💔 Enter adult mortality rate per 1000 population (0-1000): ➡️ "))
            if 0 <= adult_mortality <= 1000:
                country_data['adult_mortality'] = adult_mortality
                break
            else:
                print("🚫 Invalid input. Must be between 0 and 1000.")
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")

    # INFANT DEATHS
    while True:
        try:
            infant_deaths = float(input("\n👶 Enter infant deaths per 1000 population (0-1000): ➡️ "))
            if 0 <= infant_deaths < 1000:
                country_data['infant_deaths'] = infant_deaths
                break
            else:
                print("🚫 Invalid input. Must be between 0 and 1000.")
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")

    # POLIO
    while True:
        try:
            polio = float(input("\n💉 Enter your Polio (Pol3) immunization coverage among 1-year-olds as a percentage (%) (0-100): ➡️ "))
            if 0 <= polio <= 100:
                country_data['polio'] = polio
                break
            else:
                print("🚫 Invalid input. Must be between 0 and 100.")
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")

    # HIV
    while True:
        try:
            incidents_hiv = float(input("\n🦠 Enter the number of deaths per 1,000 live births due to HIV/AIDS for children aged 0-4 in your country (0-1000): ➡️ "))
            if 0 <= incidents_hiv <= 1000:
                country_data['incidents_hiv'] = incidents_hiv
                break
            else:
                print("🚫 Invalid input. Must be between 0 and 1000.")
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")

    # BMI
    while True:
        try:
            bmi = float(input("\n⚖️ Enter your country's average Body Mass Index (BMI): ➡️ "))
            if 0 <= bmi <= 1000:
                country_data['bmi'] = bmi
                break
            else:
                print("🚫 Invalid input. Must be between 0 and 1000.")
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")

    # THINNESS
    while True:
        try:
            thinness = float(input("\n📉 Enter prevalence of thinness among ages 10-19 (%) (0-100): ➡️ "))
            if 0 <= thinness <= 100:
                country_data['thinness_ten_nineteen_years'] = thinness
                break
            else:
                print("🚫 Invalid input. Must be between 0 and 100.")
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")

    # SCHOOLING
    while True:
        try:
            schooling = float(input("\n📚 Enter average years of schooling (0-100): ➡️ "))
            if 0 <= schooling <= 100:
                country_data['schooling'] = schooling
                break
            else:
                print("🚫 Invalid input. Must be between 0 and 100.")
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")

    # GDP PER CAPITA
    while True:
        try:
            gdp = float(input("\n💰 Enter your country's Gross domestic product (GDP) per capita in USD (without the $, e.g., 5000): ➡️ "))
            country_data['gdp_per_capita'] = gdp
            break
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("✅ Advanced data collection complete. Proceeding with analysis...")
    return country_data


def get_data_sensitive():
    country_data = {}
    # REGION
    while True:
        try:
            region_dict = {
                0: 'Africa', 1: 'Asia', 2: 'Central America and Caribbean',
                3: 'European Union', 4: 'Middle East', 5: 'North America',
                6: 'Oceania', 7: 'Rest of Europe', 8: 'South America'
            }
            region_number = int(input(
            "🌍 Please enter the number that best represents the region of your country out of the following: (0-8):\n"
            " 0. Africa \n"
            " 1. Asia \n"
            " 2. Central America and Caribbean \n"
            " 3. European Union \n"
            " 4. Middle East \n"
            " 5. North America \n"
            " 6. Oceania \n"
            " 7. Rest of Europe \n"
            " 8. South America \n ➡️"
        ))
            if 0 <= region_number <= 8:
                country_data['region'] = region_dict[region_number]
                for key in region_dict:
                    country_data[f"region_{region_dict[key].replace(' ', '_').lower()}"] = (key == region_number)
                break
            else:
                print("🚫 Invalid input. Please enter a number between 0 and 8.")
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")

    # YEAR
    while True:
        try:
            year = int(input("\n📅 Please enter the year of the dataset you would like to predict for in number format, any year from 2000 onwards (2000 or later): ➡️ "))
            if year >= 2000:
                country_data['year'] = year
                break
            else:
                print("🚫 Invalid input. The year must be 2000 or later.")
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")

    # ADULT MORTALITY
    while True:
        try:
            adult_mortality = float(input("\n💔 Enter adult mortality rate per 1000 population (0-1000): ➡️ "))
            if 0 <= adult_mortality <= 1000:
                country_data['adult_mortality'] = adult_mortality
                break
            else:
                print("🚫 Invalid input. Must be between 0 and 1000.")
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")

        # POLIO
    while True:
        try:
            polio = float(input("\n💉 Enter your Polio (Pol3) immunization coverage among 1-year-olds as a percentage (%) (0-100): ➡️ "))
            if 0 <= polio <= 100:
                country_data['polio'] = polio
                break
            else:
                print("🚫 Invalid input. Must be between 0 and 100.")
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")
    
    # BMI
    while True:
        try:
            bmi = float(input("\n⚖️ Enter your country's average Body Mass Index (BMI): ➡️ "))
            if 0 <= bmi <= 1000:
                country_data['bmi'] = bmi
                break
            else:
                print("🚫 Invalid input. Must be between 0 and 1000.")
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")

    # GDP PER CAPITA
    while True:
        try:
            gdp = float(input("\n💰 Enter your country's Gross domestic product (GDP) per capita in USD (without the $, e.g., 5000): ➡️ "))
            country_data['gdp_per_capita'] = gdp
            break
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("✅ Data collection complete. Proceeding with analysis...")
    return country_data