import requests
import simplejson

__wikipedia_query="http://en.wikipedia.org/w/api.php?action=query"

def construct_user_page_edits_request(username, limit):
    """constructs wikipedia query for user page edits"""
    return  __wikipedia_query + "&titles=User:" + username + "&prop=revisions" + "&format=json" + "&rvlimit="  + str(limit)


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
