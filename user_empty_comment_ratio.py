from wkv_common import *

def user_empty_comment_ratio(username):
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=usercontribs&ucuser=' + username + '&uclimit=500&ucdir=older&format=json'
    jsonobj = make_wikipedia_request_json(query)
    commented = 0
    total = 0
    for entries in jsonobj['query']['usercontribs']:
        if entries['comment'] == "":
            total +=1
        else:
            total +=1
            commented +=1
    if total == 0:
        return 0
    return float(commented)/total
