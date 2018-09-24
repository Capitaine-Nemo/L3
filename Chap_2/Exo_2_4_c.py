def mots_position(mots, x, n):
    l = []
    for m in mots:
        if n<len(m):
            if m[n]==x:
                l.append(m)
    return l
 
def create_mots_dict(mots):
    d = dict()
    for m in mots:
        for i in range(len(m)):
            if (m[i].lower(), i) in d:
                d[(m[i].lower(), i)].append(m)
            else:
                d[(m[i].lower(), i)]=[m]
    return d

mots = ['Abricot', 'Airelle', 'Ananas', 'Banane', 'Cassis', 'Cerise', 'Citron','Clémentine', 'Coing', 'Datte', 'Fraise', 'Framboise', 'Grenade', 'Groseille','Kaki', 'Kiwi', 'Litchi', 'Mandarine', 'Mangue', 'Melon', 'Mirabelle', 'Nectarine', 'Orange', 'Pamplemousse', 'Papaye', 'Pêche', 'Poire', 'Pomme', 'Prune', 'Raisin']

print(mots_position(mots, "e", 4))
mots_dict = create_mots_dict(mots)

print(mots_dict["e", 4])
