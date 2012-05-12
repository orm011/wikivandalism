from wkv_common import *

def user_uses_editing_tool(editinfo):
    username = editinfo['user']
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=usercontribs&ucuser=' + username + '&uclimit=500&ucdir=older&format=json'
    jsonobj = make_wikipedia_request_json(query)
    for entries in jsonobj['query']['usercontribs']:
        if entries['comment'][:1] == '[':
            return 1
    return 0
