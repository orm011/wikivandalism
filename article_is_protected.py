from wkv_common import *
from user_is_ip_address import *
from ip_continent import *

def article_is_protected_real(article_title):
    req = construct_protected_query(article_title, 500)
    ans = make_wikipedia_request_json(req)
    categories = [x.get('title')  for x in ans.get('query').get('pages').itervalues().next().get('categories')]
    return sum(__isprotected(cat) for cat in categories)
    
def construct_protected_query(title, limit):
    return "http://en.wikipedia.org/w/api.php?action=query&titles=" + title + "&prop=categories&cllimit=" + str(limit) + "&format=json"


def __isprotected(name):
    return int((name.lower().find('protected') > -1))


def test_article_is_protected():
    assert article_is_protected_real("Barack Obama") >= 2
    assert article_is_protected_real("Al Gore") == 0
    print "success"

def article_is_protected(editinfo):
    return article_is_protected_real(editinfo['title'])
