country = input()   # Add country name
visits = int(input()) # Number of Visits
list_of_cities = eval(input())  #Create List from formatted

travel_log = [
    {
        'country': "France",
        'visits' : 12,
        'cities': ['paris', 'little', 'Dajon']
    },
    {
        'country': 'Germany',
        'Visits': 5,
        'cities': ['Berlin', 'Hamburg', 'Stuttgart']
    }
]

# Do not change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log.
def add_new_country(name, times_visited, cities_visited):
    new_coutry = {}
    new_coutry['country'] = name
    new_coutry['visits'] = times_visited
    new_coutry['cities'] = cities_visited
    travel_log.append(new_coutry)


# Do not Change the code below

add_new_country(country, visits, list_of_cities)
print(f"I've been tp {travel_log[2]['country']}{travel_log[2]}")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")