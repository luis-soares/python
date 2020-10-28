names=['luis','ana','fla','lais']
usuario=dict(name = 'luis', idade=34,pais='br')
usuario2={'name':'luis','idade':34,'pais':'us'}
usuarios=[]
usuarios.append({'name':'luis','idade':34,'pais':'us'})
usuarios.append({'name':'Fla','idade':40,'pais':'uk'})
print('inserir o nome do usuario')
username=input()

for usr in usuarios:
    if usr["name"].lower() == username.lower():
        print('o usuario {} tem {} anos'.format(usr["name"],usr["idade"]))

print(usuarios)

print(names[0:4])

for name in names:
    print("the name is", name)

print('O usuario', usuario['name'], 'tem', usuario['idade'], 'e nasceu no', usuario['pais'])
print('O usuario {name} tem {idade} e nasceu no {pais}'.format(**usuario))
print(f'O usuario {usuario["name"]} tem {usuario["idade"]} e nasceu no {usuario["pais"]}')

print('O usuario {name} tem {idade} e nasceu no {pais}'.format(name=usuario['name'], idade=usuario['idade'],pais=usuario2['pais']))

print('O usuario {} tem {} e nasceu no {}'.format(usuario['name'], usuario['idade'],usuario2['pais']))


print('O usuario {0} tem {2} e nasceu no {1}'.format(usuario['name'], usuario['idade'],usuario2['pais']))
