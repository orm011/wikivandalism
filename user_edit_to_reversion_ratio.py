from wkv_common import *

#Also does not work because of lack of rollback token permission
'''
def user_edit_to_reversion_ratio(username):
    reversion_count = 0
    total = 0
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=usercontribs&ucuser=' + username + '&uclimit=500&ucdir=older&format=json'
    jsonobj = make_wikipedia_request_json(query)
    print jsonobj
    for articles in jsonobj['query']['usercontribs']:
	title = articles['title']
	query2 = 'http://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=' + title + '&rvtoken=rollbacktoken'
	jsonobj2 = make_wikipedia_request_json(query2)
	if jsonobj2 == "": 
	    total += 1
	else:
	    total += 1
	    reversion_count += 1
    if total == 0:
	return 0
    return float(reversion_count)/total

def user_edit_reversion(username):
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=usercontribs&ucuser=' + username + '&uclimit=500&ucdir=older&format=json'
    jsonobj = make_wikipedia_request_json(query)
    return jsonobj

def user_edit_reversion2(username, title):
    #articles = jsonobj['query']['usercontribs'][1]['title']
    query = 'http://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=' + title + '&rvtoken=rollback&format=json'
    jsonobj = make_wikipedia_request_json(query)
    return jsonobj'''





