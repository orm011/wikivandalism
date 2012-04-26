from wkv_common import *

def user_article_to_edit_ratio(username):
    '''number of articles the user has edited, to how many edits he makes total'''
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=usercontribs&ucuser=' + username + '&uclimit=500&ucdir=older&format=json'
    jsonobj = make_wikipedia_request_json(query)
    titles = set()
    numedits = 0
    for edit in jsonobj['query']['usercontribs']:
        title = edit['title']
        titles.add(title)
        numedits += 1
    if numedits == 0:
        return 0
    numarticles = len(titles)
    return float(numarticles)/numedits
