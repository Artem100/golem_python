from golem.actions import navigate, send_keys, click, verify_element_text

from testdir.projects.automation_practice.pages import header, article

description = 'Search an article in Wikipedia'

tags = []

pages = ['header', 'article']


def setup(data):
    pass

def test(data):
    navigate(data.URL)
    send_keys(header.search_input, data.search_value)
    click(header.search_button)
    verify_element_text(article.title, data.article_title)



def teardown(data):
    pass

