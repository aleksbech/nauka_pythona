samolot = {'name': 'boeing',
           'przebieg': 1000,
           'type': 'pasazerski'}

print(samolot['name'])
print(samolot['type'])
# print(samolot['nieznany_klucz'])
print(samolot.get('nieznany_klucz'))

for key in samolot:
    print ("{0}:{1}".format(key, samolot[key]))
