#def word_lower():



class Word():
    def __init__(self, value, subwords):
        self.value = value
        self.subwords = subwords

    def has_subword(self, word):
        if word.lower() in self.subwords:
            return True
        return False

word = Word('прокрастинация', ['рок', 'кор', 'карп'])

#print(word.has_subword('пар'))

for round in range(3):

    print('Введите слово')
    user_input = input()
    if word.has_subword(user_input):
        print('Слово есть')
    else:
        print('Слова нет')