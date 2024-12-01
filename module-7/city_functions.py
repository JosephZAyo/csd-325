def city_country(city, country, population=None, language=None):
# Return a string in the format 'City, Country - population X, language'.
# If population or language is not provided, display 'population not found'.
    if population is None:
        population = "not found"
    if language is None:
        language = "language not found"
    return f"{city}, {country} - population {population}, {language}"
print(city_country("Santiago", "Chile"))
print(city_country("New York", "United States", 5000000))
print(city_country("Tokyo", "Japan", 1600000, "Japanese"))
# Calling the function three times with different cities and countries
