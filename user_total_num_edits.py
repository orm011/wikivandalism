from wkv_common import *

def user_total_num_edits(editinfo):
    numedits = user_total_num_edits_real(editinfo)
    return numedits

def user_total_num_edits_real(editinfo):
    username = editinfo['user']
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=usercontribs&ucuser=' + username + '&uclimit=500&ucdir=older&format=json'
    jsonobj = make_wikipedia_request_json(query)
    try:
        return len(jsonobj['query']['usercontribs'])
    except:
        return 0
