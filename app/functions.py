def get_doge(dogs):
    dog_stats = {
        'breed': {},
        'age': {},
        'size': {},
        'gender': {},
        'color': {}
    }
    for pupper in dogs:
        #print(pupper)
        if (pupper['breed']):
            #print('Breed:' + pupper['breed'])
            key = pupper['breed']
            #print(key)
            if key in dog_stats['breed']:
                dog_stats['breed'][key] += 1
            else:
                dog_stats['breed'][key] = 1
            #do the same for age
        if (pupper['age']):
            key = pupper['age']
            if key in dog_stats['age']:
                dog_stats['age'][key] += 1
            else:
                dog_stats['age'][key] = 1

        #do the same for size
        if (pupper['size']):
            key = pupper['size']
            if key in dog_stats['size']:
                dog_stats['size'][key] += 1
            else:
                dog_stats['size'][key] = 1

        #do the same for gender
        if (pupper['gender']):
            key = pupper['gender']
            if key in dog_stats['gender']:
                dog_stats['gender'][key] += 1
            else:
                dog_stats['gender'][key] = 1

    #do the same for color
        if (pupper['color']):
            key = pupper['color']
            if key in dog_stats['color']:
                dog_stats['color'][key] += 1
            else:
                dog_stats['color'][key] = 1
    return dog_stats

def get_kitteh(kittehz):
    cat_facts = {
        'breed': {},
        'age': {},
        'size': {},
        'gender': {},
        'color': {}
    }
    for kitteh in kittehz:
        #print(pupper)
        if (kitteh['breed']):
            #print('Breed:' + pupper['breed'])
            key = kitteh['breed']
            #print(key)
            if key in cat_facts['breed']:
                cat_facts['breed'][key] += 1
            else:
                cat_facts['breed'][key] = 1
            #do the same for age
        if (kitteh['age']):
            key = kitteh['age']
            if key in cat_facts['age']:
                cat_facts['age'][key] += 1
            else:
                cat_facts['age'][key] = 1

        #do the same for size
        if (kitteh['size']):
            key = kitteh['size']
            if key in cat_facts['size']:
                cat_facts['size'][key] += 1
            else:
                cat_facts['size'][key] = 1

        #do the same for gender
        if (kitteh['gender']):
            key = kitteh['gender']
            if key in cat_facts['gender']:
                cat_facts['gender'][key] += 1
            else:
                cat_facts['gender'][key] = 1

    #do the same for color
        if (kitteh['color']):
            key = kitteh['color']
            if key in cat_facts['color']:
                cat_facts['color'][key] += 1
            else:
                cat_facts['color'][key] = 1
    return cat_facts
