import sys
import main
from nltk.tree import Tree
import treeObjects

#sentence = "%s" % (sys.argv[1])
sentence = sys.argv[1]
examples = main.getInput(sentence)

print(main.getHead(examples))



