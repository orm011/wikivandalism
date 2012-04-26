from wkv_common import *

def user_external_link_ratio(username):
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=usercontribs&ucuser=' + username + '&uclimit=100&ucdir=older&format=json'
    jsonobj = make_wikipedia_reques_json(query)

    query2 = 'http://en.wikipedia.org/w/api.php?action=query&list=exturlusage&ucuser=' + username + '&uclimit=100&ucdir=older&format=json'
    jsonobj2 = make_wikipedia_request_json(query2)
    total = 0
    urlcount = 0
    for entries in jsonobj['query']['usercontribs']:
	      total += 1
        urlcount = entries in jsonobj2['query']['exturlusage']
    if total == 0:
        return 0
    return float(urlcount)/total 
