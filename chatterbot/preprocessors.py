def clean_whitespace(chatbot, statement):

    import re

    statement.text = statement.text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    statement.text = statement.text.strip()
    statement.text = re.sub(' +', ' ', statement.text)
    return statement


def unescape_html(chatbot, statement):

    import sys

    if sys.version_info[0] < 3:
        from HTMLParser import HTMLParser
        html = HTMLParser()
    else:
        import html
    statement.text = html.unescape(statement.text)
    return statement


def convert_to_ascii(chatbot, statement):

    import unicodedata
    import sys

    if sys.version_info[0] < 3:
        statement.text = unicode(statement.text) # NOQA
    text = unicodedata.normalize('NFKD', statement.text)
    text = text.encode('ascii', 'ignore').decode('utf-8')
    statement.text = str(text)
    return statement