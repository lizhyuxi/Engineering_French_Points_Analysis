#########################################################
# Use Stanford POS tagger to get the tag of each word in the text
# Usage: python3 postagger.py $(input_txt_file_name) $(output_tag_file_name)
#########################################################

### Initializing NLTK and Spcay
import nltk, spacy

nlp = spacy.load('fr_core_news_md')

def process_word(word): # Try to erase extra characters in this word
    word = word.lower()
    # if '\'' in word: # Erase l', m' etc.
    #     word = word.split('\'')[-1]
    if len(word) > 0 and word[0] == '(': word = word[1:] # Erase brackets
    if len(word) > 0 and word[-1] in ',.)': word = word[:-1] # Erase trailing characters
    return word

def postagging(blob):
    nlp_res = nlp(blob + '.')
    ret = []
    for token in nlp_res:
        if len(token.text) > 0 and token.pos_ != 'SPACE':
            ret.append((token.text, token.pos_, token.lemma_))
    print('\rDone      ')
    return ret

if __name__ == '__main__':
    import sys, codecs

    ### Files processing
    assert(len(sys.argv) == 3)
    inp_name = sys.argv[1]
    out_name = sys.argv[2]

    inp = codecs.open(inp_name, 'r', 'utf-8')
    out = codecs.open(out_name, 'w', 'utf-8')

    blob = inp.read()

    res = postagging(blob)
    out.write('\n'.join(' '.join(tup) for tup in res))
