import pycountry

countries = list(pycountry.countries)

country_names = [country.name for country in countries]

print(country_names)