from xml.dom.minidom import parse

def parse_trial_file(filename):
    dom = parse(open(filename, "r"))
    #WPEdit is the tag name in the file that seems to correspond to a row
    edits = dom.firstChild.getElementsByTagName("WPEdit")
    return [todict(edit) for edit in edits]

def todict(element):
    elts = element.getElementsByTagName("*")
    leaves = [elt for elt in elts if len(elt.childNodes) == 1]
    answer = {}

    for leaf in leaves:
        try :
            if str(leaf.tagName) != 'text':
                answer[str(leaf.tagName)] = str(leaf.firstChild.nodeValue)
            else:
                answer['text'] = wiki_markup_file(leaf.firstChild.nodeValue)
        except:
            #sometimes it will fail (because it is more than ascii)
            #in that case just copy
            answer[str(leaf.tagName)] = leaf.firstChild.nodeValue
            
    return answer

class wiki_markup_file:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return "length: " + str(len(self.text)) + " "  + self.text[0:200]

    def getText(self):
        return self.text
