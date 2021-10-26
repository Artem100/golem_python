from golem.actions import verify_element_text

# title = ('id', 'firstHeading')

class Locator:

    title = ('id', 'firstHeading')

    def title_check(self, some_data):
        verify_element_text(self.title, some_data)