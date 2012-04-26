import requests
import simplejson

__wikipedia_query="http://en.wikipedia.org/w/api.php?action=query"

def construct_user_page_edits_request(username, limit):
    """constructs wikipedia query for user page edits"""
    return  __wikipedia_query + "&titles=User:" + username + "&prop=revisions" + "&format=json" + "&rvlimit="  + str(limit)

def construct_user_talk_page_edits_request(username, limit):
    return  __wikipedia_query + "&titles=User_talk:" + username + "&prop=revisions" + "&format=json" + "&rvlimit="  + str(limit)

def construct_user_talk_page_contents_request(username, limit):
    return  __wikipedia_query + "&titles=User_talk:" + username + "&prop=revisions&rvprop=comment|tags|content" + "&format=json" + "&rvlimit="  + str(limit)

class WikipediaError(Exception):
    pass


def make_wikipedia_request(req):
    """connects to wikipedia and collects answer"""
    try:
        res = requests.get(req)
        if not res.ok:
            raise  WikipediaError, res.error
    except:
            raise  WikipediaError
        
    return res.text

def make_wikipedia_request_json(req):
    jsontext = make_wikipedia_request(req)
    return simplejson.loads(jsontext)

def get_user_page_revisions(json_result):
    """returns a list of page edits"""
    parsed = simplejson.loads(json_result)
    try:
        return parsed.items()[0][1].items()[0][1].values()[0]['revisions']
    except:
        ##users without profile have no results in revisions
        return []

def user_revision_count(username):
    """actual feature, connects to wikpedia"""
    req = construct_user_page_edits_request(username,500)
    return len(get_user_page_revisions(make_wikipedia_request(req)))

def user_talk_revision_count(username):
    req = construct_user_talk_page_edits_request(username, 500)
    return len(make_wikipedia_request_json(req)['query']['pages'].values()[0]['revisions'])

def user_talk_vandal_vocab_count(username):
    req = construct_user_talk_page_contents_request(username, 500)
    jsontxt = make_wikipedia_request(req)
    vandalvocab = ['unconstructive', 'revert', 'vandal', 'block', 'warn']
    wordsInText = jsontxt.replace(',', ' ').split(' ')
    vandalwordcount = 0
    for vandalword in vandalvocab:
        for w in wordsInText:
            if vandalword in w:
                vandalwordcount += 1
    return vandalwordcount
