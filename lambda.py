people = [
    {"name": "harry","house": "microprogramming"},
    {"name": "raj","house": "Ranvindaram"},
    {"name": "singhaniya","house":"slutherin way"}
]

people.sort(key=lambda person: person["name"])

print(people)