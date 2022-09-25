countries = input().split(', ')
capitals = input().split(', ')
result = dict(zip(countries, capitals))
for country, capital in result.items():
    print(f"{country} -> {capital}")
