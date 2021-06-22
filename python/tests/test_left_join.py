from challenges.left_join.left_join import left_join


def test_left_join():
    actual = left_join(key={
        'first': 'Yahya',
        'second': 'Zakaria',
        'third': 'Hasan',
        'fourth': 'Mustafa',
        'fifth': 'Mohammed',
        'sixth': 'Yaqoub'
    }, key2={
        'first': 'Muhannad',
        'second': 'Laith',
        'third': 'Ahmad',
        'fourth': 'Khaled',
        'family': 'Mughrabi'
    })
    excepted = [['first', 'Yahya', 'Muhannad'], ['second', 'Zakaria', 'Laith'], ['third', 'Hasan', 'Ahmad'], ['fourth', 'Mustafa', 'Khaled'], ['fifth', 'Mohammed', 'None'], ['sixth', 'Yaqoub', 'None']]
    assert actual == excepted
