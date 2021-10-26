from golem.actions import navigate, send_keys

description = 'Hey! this test has infile data!'
data = [
        {
        'numbers': 12,
        'boolean': False,
        'none': None,
        'list': [1,2,3],
        'dict': {'key': 'string'},
        'tuple': (1, '2', 3.0),
        'str_single': 'test',
        'str_double': "test",
        },
        {
        'numbers': 12,
        'boolean': True,
        'none': None,
        'list': ['a', 'b', 'c'],
        'dict': {"key": 12},
        'tuple': ('a', 'a"b"c', "a'b'c"),
        'str_single': 'a "b" c',
        'str_double': "a 'b' c",
        },
        ]

def test(data):
    navigate('https://www.google.com')
    send_keys(('name', 'q'), data.str_single)
    #