from wkv_common import *

def user_has_edited_talk_page(username):
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=usercontribs&ucuser=' + username + '&uclimit=500&ucdir=older&format=json'
    jsonobj = make_wikipedia_request_json(query)
    for entries in jsonobj['query']['usercontribs']:
        if entries['title'][0:5] == 'Talk:':
            return 1
    return 0
