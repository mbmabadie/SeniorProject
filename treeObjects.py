from stanfordcorenlp import StanfordCoreNLP
from opencc import OpenCC
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag, word_tokenize, RegexpParser


#sentence = input('Enter a string:')
#print('The inputted string is:', sentence)


def getParse(sentence) -> str:
    # Preset
    nlp = StanfordCoreNLP('stanford-corenlp-4.2.0/', memory='8g')
    cc = OpenCC('t2s')


    # sentence = 'Those two splendid old electric trains.'
    print("##################################################################################")
    # # POS
    print('POS：', nlp.pos_tag(sentence))
    print("##################################################################################")

    # # Tokenize
    print('Tokenize：', nlp.word_tokenize(sentence))
    print("##################################################################################")

    # # NER
    print('NER：', nlp.ner(sentence))
    print("##################################################################################")


    # Parser
    tree = nlp.parse(sentence)
    parse_string = ' '.join(str(tree).split())
    print(parse_string)

    # ParserTest
    print('Parser：')
    print(nlp.parse(sentence))
    print("##################################################################################")


    #TREE Graph
    tagged = pos_tag(word_tokenize(sentence))
    # Extract all parts of speech from any text
    chunker = RegexpParser("""
                           NP: {<DT>?<JJ>*<NN>}    #To extract Noun Phrases
                           P: {<IN>}               #To extract Prepositions
                           V: {<V.*>}              #To extract Verbs
                           PP: {<P> <NP>}          #To extract Prepostional Phrases
                           VP: {<V> <NP|PP>*}      #To extarct Verb Phrases
                           """)

    # Print all parts of speech in above sentence
    output = chunker.parse(tagged)
    print("After Extracting\n", output)
    # To draw the parse tree
    output.draw()
    print("##################################################################################")


    # Close Stanford Parser
    nlp.close()
    return str(parse_string)
