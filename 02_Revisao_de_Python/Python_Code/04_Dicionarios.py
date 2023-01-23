dicionario = {}

dicionario2 = dict()

familia = {'01': 'Felicity', '02': 'Arrow', '03': 'Flash', '04': 'Arrow', '05': 'Supergirl', '06': 'Batman',
           '07': 'Black Lightning'}

familia2 = dict(Pai="Jair", Mae="Maria", Filho="Joao", Filha="Maria", TemFilhos=True)

print(familia)
print(familia2)

lista_tuplas = [('Pai', 'Jair'), ('Mae', 'Maria'), ('Filho', 'Joao'), ('Filha', 'Maria'), ('TemFilhos', True)]

print(lista_tuplas)
print(lista_tuplas[0])

familia3 = dict(lista_tuplas)

print(familia3)
print(familia2['Pai'])
print(familia2.get('Pai'))
print(familia2.get('Mae'))
print(len(familia2))
print(familia2.keys())
print(familia2.values())
print(familia2.items())

familia2['Cachorro'] = 'Marley'
print(familia2)

familia2.update({'Casa': False, 'Gato': 'Garfield'})
print(familia2)

familia2.pop('Casa')
print(familia2)

del familia2['Gato']
print(familia2)

familia2['Cachorro'] = 'Marley e Eu'
print(familia2)

print('Mae' in familia2)

familia2['Animais'] = {'Casa', 'Gato', 'Passarinho'}
print(familia2)
