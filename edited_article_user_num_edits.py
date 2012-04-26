from wkv_common import *

def edited_article_user_num_edits(editinfo):
    '''number of edits the user has made to the article'''
    username = editinfo['user']
    articletitle = editinfo['title']
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=usercontribs&ucuser=' + username + '&uclimit=500&ucdir=older&format=json'
    jsonobj = make_wikipedia_request_json(query)
    numedits = 0
    for edit in jsonobj['query']['usercontribs']:
        title = edit['title']
        if title == articletitle:
            numedits += 1
    return numedits
