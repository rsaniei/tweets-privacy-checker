import stanza
import json


def get_stats(source_file):
    # stanza.download('en')
    # stanza_nlp = stanza.Pipeline('en')

    hashtag_count = []
    mention_count = []
    url_count = []
    sentence_count = []
    token_count = []

    verb_count = []
    noun_count = []
    propnoun_count = []
    pronoun_count = []
    adj_count = []
    adv_count = []

    k = 0
    nlp = stanza.Pipeline(lang='en', processors='tokenize')
    nlp_2 = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos')

    with open(source_file, 'r') as f:

        for line in f.readlines():
            k = k + 1
            print(k)
            # counting hashtags and mentions in each tweet
            i = 0
            j = 0
            z = 0
            a = b = c = d = e = f = 0
            for word in line.split():
                if word.startswith("#"):
                    i = i + 1
                if word.startswith("@"):
                    j = j + 1
                if word.startswith("http"):
                    z = z + 1


            hashtag_count.append(i)
            mention_count.append(j)
            url_count.append(z)

            #  counting POSs in each tweet
            doc_2 = nlp_2(line)
            for sent in doc_2.sentences:
                for word in sent.words:
                    # print(word.upos)
                    if word.upos == ('VERB' or 'AUX'):
                        a = a + 1
                    if word.upos == 'NOUN':
                        b = b + 1
                    if word.upos == ('PROPN'):
                        c = c + 1
                    if word.upos == ('PRON'):
                        d = d + 1
                    if word.upos == ('ADJ'):
                        e = e + 1
                    if word.upos == ('ADV'):
                        f = f + 1

            verb_count.append(a)
            noun_count.append(b)
            propnoun_count.append(c)
            pronoun_count.append(d)
            adj_count.append(e)
            adv_count.append(f)

            #  counting sentences in each tweet
            doc = nlp(line)
            sentence_count.append(len(doc.sentences))

            # counting tokens in each tweet
            y = 0
            for s, sentence in enumerate(doc.sentences):
                y = y + (len(sentence.tokens))
            token_count.append(y)

    print("hashtags:", sum(hashtag_count))
    print("mentions:", sum(mention_count))
    print("urls:", sum(url_count))
    print("sentences:", sum(sentence_count))
    print("tokens:", sum(token_count))
    print("verb:", sum(verb_count))
    print("noun:", sum(noun_count))
    print("propnoun:", sum(propnoun_count))
    print("pronoun:", sum(pronoun_count))
    print("adj:", sum(adj_count))
    print("adv:", sum(adv_count))
