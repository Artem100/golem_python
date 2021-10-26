from golem.actions import *

search_input = ('id', 'searchInput')
search_button = ('id', 'searchButton')


def search_article_field_input(some_data):
    send_keys(search_input, some_data)
    click(search_button)
