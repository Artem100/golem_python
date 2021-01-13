from golem.actions import navigate, send_keys, click, verify_element_text

description = ''

tags = []

pages = []


def setup(data):
    pass


def test(data):
    navigate('http://en.wikipedia.org/')
    send_keys(('id', 'searchInput'), 'automation')
    click(('id', 'searchButton'))
    verify_element_text(('id', 'firstHeading'), 'Automation')
    pass


def teardown(data):
    pass

