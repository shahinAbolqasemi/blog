import re

from hazm import word_tokenize, Normalizer


def tokenize_text(text):
    content_list = word_tokenize(text)
    normalizer = Normalizer()
    return [normalizer.normalize(i) for i in content_list]


def remove_html_tags(text):
    from bs4 import BeautifulSoup
    import re
    pattern = re.compile(r'<.*?>')
    html_text = BeautifulSoup(text, 'html.parser').get_text()
    content = pattern.sub('', html_text)
    return content


def detect_lang(word):
    return 'fa' if re.search(r'^[\u0600-\u06FF]+$', word) else 'etc'
