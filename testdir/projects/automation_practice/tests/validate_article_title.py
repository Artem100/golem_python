from golem.actions import navigate, send_keys, click, verify_element_text, wait

from pages import header, article

description = 'Search an article in Wikipedia'

tags = []

pages = ['header', 'article']


def setup(data):
    pass

def test(data):
    navigate(data.env.url)
    wait(2)
    header.search_article_field_input(data.search_value)
    wait(2)
    # article.Locator.title_check(data.article_title)
    verify_element_text(article.Locator().title, data.article_title)
    pass



def teardown(data):
    pass

