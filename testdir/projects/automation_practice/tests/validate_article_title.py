from golem.actions import navigate, send_keys, click, verify_element_text

description = 'Search an article in Wikipedia'

tags = []

pages = []


def setup(data):
    pass


def test(data):
    navigate('http://en.wikipedia.org/')
    send_keys(('id', 'searchInput'), data.search_value)
    click(('id', 'searchButton'))
    verify_element_text(('id', 'firstHeading'), data.article_title)
    pass #


def teardown(data):
    pass

