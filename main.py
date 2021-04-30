from nltk.tree import Tree
import treeObjects
import sys

# examples = [
#     '(ROOT (NP (NP (DT the) (NN person)) (SBAR (WHNP (WDT that)) (S (VP (VBD gave) (NP (DT the) (NN talk)))))))'
# ]


# The sentence you want to parse (Python)

#sentence = input('Enter a string:')
#print('The inputted string is:', sentence)

# get input from user (HTML)

sentence = sys.argv[1]
print('The inputted string is:', sentence)

# String to Parsed
examples = [treeObjects.getParse(sentence)]



def find_noun_phrases(tree):
    return [subtree for subtree in tree.subtrees(lambda t: t.label()=='NP')]

def find_head_of_np(np):
    noun_tags = ['NN', 'NNS', 'NNP', 'NNPS']
    top_level_trees = [np[i] for i in range(len(np)) if type(np[i]) is Tree]
    ## search for a top-level noun
    top_level_nouns = [t for t in top_level_trees if t.label() in noun_tags]
    if len(top_level_nouns) > 0:
        ## if you find some, pick the rightmost one, just 'cause
        return top_level_nouns[-1][0]
    else:
        ## search for a top-level np
        top_level_nps = [t for t in top_level_trees if t.label()=='NP']
        if len(top_level_nps) > 0:
            ## if you find some, pick the head of the rightmost one, just 'cause
            return find_head_of_np(top_level_nps[-1])
        else:
            ## search for any noun
            nouns = [p[0] for p in np.pos() if p[1] in noun_tags]
            if len(nouns) > 0:
                ## if you find some, pick the rightmost one, just 'cause
                return nouns[-1]
            else:
                ## return the rightmost word, just 'cause
                return np.leaves()[-1]

for example in examples:
    tree = Tree.fromstring(example)
    for np in find_noun_phrases(tree):
        print("noun phrase:")
        print(" ".join(np.leaves()))
        head = find_head_of_np(np)
        print("------------>>>>> head <<<<<------------")
        print(head)
        print("##################################################################################")
