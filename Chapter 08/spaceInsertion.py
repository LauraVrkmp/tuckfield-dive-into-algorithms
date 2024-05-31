import re, nltk
# nltk.download('brown')
from nltk.corpus import brown
import numpy as np

wordlist = set(brown.words())
word_list = list(wordlist)

word_list = [word.replace('*','') for word in word_list]
word_list = [word.replace('[','') for word in word_list]
word_list = [word.replace(']','') for word in word_list]
word_list = [word.replace('?','') for word in word_list]
word_list = [word.replace('.','') for word in word_list]
word_list = [word.replace('+','') for word in word_list]
word_list = [word.replace('/','') for word in word_list]
word_list = [word.replace(';','') for word in word_list]
word_list = [word.replace(':','') for word in word_list]
word_list = [word.replace(',','') for word in word_list]
word_list = [word.replace(')','') for word in word_list]
word_list = [word.replace('(','') for word in word_list]
word_list.remove('')

text = "The oneperfectly divine thing, the oneglimpse of God's paradisegiven" \
        "on earth, is to fight a losingbattle - and notlose it."

# word_list = ['The', 'one', 'perfectly', 'devine']
# word_list_copy = [word for word in word_list if 'n' in word]

def insertSpaces(text, word_list):
    locs = list(set([(m.start(),m.end()) for word in word_list 
                     for m in re.finditer(word, text)]))

    spacestarts = [m.start() for m in re.finditer(' ', text)]
    spacestarts.append(-1)
    spacestarts.append(len(text))
    spacestarts.sort()
    spacestarts_affine = [ss+1 for ss in spacestarts]
    spacestarts_affine.sort()

    partial_words = [loc for loc in locs if loc[0] in spacestarts_affine and 
                    loc[1] not in spacestarts]

    partial_words_end = [loc for loc in locs if loc[0] not in spacestarts_affine and
                        loc[1] in spacestarts]
    
    between_spaces = [(spacestarts[k] + 1, spacestarts[k + 1]) 
                    for k in range(0, len(spacestarts) - 1)]

    between_spaces_notvalid = [loc for loc in between_spaces 
                            if text[loc[0]:loc[1]] not in word_list]

    textnew = text

    for loc in between_spaces_notvalid:
        endsofbeginnings = [loc2[1] for loc2 in partial_words if loc2[0] == loc[0] and
                            (loc2[1] - loc[0]) > 1]
        beginningsofends = [loc2[0] for loc2 in partial_words_end if loc2[1] == loc[1] and
                            (loc2[1] - loc[0]) > 1]

        pivot = list(set(endsofbeginnings).intersection(beginningsofends))
        if (len(pivot) > 0):
            pivot = np.min(pivot)
            textnew = textnew.replace(text[loc[0]:loc[1]], text[loc[0]:pivot] + 
                                      ' ' + text[pivot:loc[1]])
    textnew = textnew.replace('  ', ' ')
    return textnew
    
print(insertSpaces(text, word_list))