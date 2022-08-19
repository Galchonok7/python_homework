
def thesaurus_adv(*names):
    res = {}
    for name in names:
        key = name[0].capitalize()
        if key not in res:
            res[key] = []
        res[key].append(name)
    return res

print(thesaurus_adv(input()))


"Иван", "Мария", "Галия", "Ирина", "Михаил"