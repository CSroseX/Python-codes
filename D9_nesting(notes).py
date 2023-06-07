#Nesting 
#   i) nesting lists inside a dictionary
#  ii) nesting dictionaries inside lists

#Nesting lists inside a dictionary

movie_list = ['Rio','Inside Out','Hachi','Shutter Island','Predestination']
series_list = ['Breaking Bad','Prison Break','Money heist','Better Call Saul']
anime_list = ['Classroom of ELite','Noragami','Aot','Demon Slayer']

media_content = {
    'movies' : {'movies' : movie_list, 'watch_count' : 'over 900', 'status': 'slim but still updating'},
    'series' : {'series' : series_list, 'watch_count': 'around 10', 'status': 'continuing'},
    'animes' : {'animes': anime_list},
}

#Nesting dictionaries inside a list 

audiovisual_content = [
    {'movies' : movie_list, 'watch_count' : 'over 900', 'status': 'slim but still updating'},
    {'series' : series_list, 'watch_count': 'around 10', 'status': 'continuing'},
    {'animes': anime_list},
]

#####       adding dictionary to already existing list
print()
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(arg_country,arg_visits,arg_cities):
    travel_log.append(
        {"country":arg_country,
         "visits":arg_visits,
         "cities":arg_cities})

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

print()