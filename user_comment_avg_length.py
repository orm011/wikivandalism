from wkv_common import *

def user_comment_avg_length(username):
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=usercontribs&ucuser=' + username + '&uclimit=500&ucdir=older&format=json'
    jsonobj = make_wikipedia_request_json(query)
    length_sum = 0
    total = 0
    for entries in jsonobj['query']['usercontribs']:
        if entries['comment'] == "":
            total += 1
        else: 
	    total += 1
	    length_sum += len(entries['comment'])
    if total == 0:
        return 0
    return float(length_sum)/total
