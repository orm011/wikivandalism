from wkv_common import *
import calendar
import time

def user_is_first_edit(username):
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=usercontribs&ucuser=' + username + '&uclimit=500&ucdir=older&format=json'
    jsonobj = make_wikipedia_request_json(query)
    print jsonobj
    if len(jsonobj['query']['usercontribs']) > 1:
	return 0
    else:
	return 1

def user_edited_recently(username, threshold_in_seconds):
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=usercontribs&ucuser=' + username + '&uclimit=500&ucdir=older&format=json'
    jsonobj = make_wikipedia_request_json(query)
    if user_is_first_edit(username) == 1:
        return 0
    else:
        second_edit_time = jsonobj['query']['usercontribs'][1]['timestamp'][:10]
	time_in_seconds = calendar.timegm(second_edit_time)
	if time_in_seconds < threshold_in_seconds:
	    return 0
	else:
	    return 1
