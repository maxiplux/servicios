__author__ = 'Juan'

def capitalize(line):

    words = line.split(' ')
    capitalized_words = []
    for word in words:
        if word!="":
            title_case_word = word[0].upper() + word[1:]
            capitalized_words.append(title_case_word)
    output = ' '.join(capitalized_words)
    return u'%s '% output

def dcapitalize(f):
    def _inner(*args):
        return capitalize(f(*args))
    return _inner