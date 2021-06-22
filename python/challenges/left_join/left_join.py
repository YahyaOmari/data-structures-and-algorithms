def left_join(key, key2):
    result = []

    for i in key.keys():
        if i in key2.keys():
            result.append([i, key[i], key2[i]])
        else:
            result.append([i, key[i], "None"])
    return result

key = {
    'first':'Yahya',
    'second':'Zakaria',
    'third':'Hasan',
    'fourth':'Mustafa',
    'fifth':'Mohammed',
    'sixth':'Yaqoub'
}
key2 = {
    'first':'Muhannad',
    'second':'Laith',
    'third':'Ahmad',
    'fourth':'Khaled',
    'family':'Mughrabi'
}

print(left_join(key, key2))