# Class attributes can be any object such as a function.
# When you add a function to a class, the function becomes a class attribute.
# Since a function is callable, the class attribute is called a callable class attribute. For example:

from pprint import pprint


class HtmlDocument:
    extension = 'html'
    version = '5'

    def render():
        print('Rendering the Html doc...')


pprint(HtmlDocument.__dict__)

# Output:

# mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument' objects>,
#               '__doc__': None,
#               '__module__': '__main__',
#               '__weakref__': <attribute '__weakref__' of 'HtmlDocument' objects>,
#               'extension': 'html',
#               'render': <function HtmlDocument.render at 0x0000010710030310>,
#               'version': '5'})
# Rendering the Html doc...