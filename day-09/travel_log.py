from calendar import c
from itertools import count


travel_log = [
    {
        "country": "Australia",
        "visits": "1",
        "cities": ["Brisbane", "Melbourne", "Sydney"]
    },
    {
        "country": "Singapore",
        "visits": 1,
        "cities": "Singapore"
    }
]

def add_new_country(country, visits, cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })

add_new_country(country="Malaysia", visits=1, cities=["China Town", "Malaca"])
print(travel_log)