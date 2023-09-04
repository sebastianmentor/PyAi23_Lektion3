lista = ['stefan',
        'emma', 
        'fredrick', 
        'stina', 
        'olof', 
        'anna']

namn = input('Skriv in ditt namn: ').lower()

if namn in lista:
    print('Du är en speciel person!')
else:
    print('Du är inte en speciel person!')