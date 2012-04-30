from wkv_common import *

__wikipedia_query = "http://en.wikipedia.org/w/api.php?action=query"
def article_is_living_person(article_title):
    req = construct_article_category_request(article_title)
    answer = make_wikipedia_request_json(req)
    ##works for 
    return answer.get('query').get('pages').items()[0][1].has_key('categories')
    
def construct_article_category_request(title):
    return     __wikipedia_query + "&titles=" + title + "&prop=categories&format=json&clcategories=Category:Living%20people"


def test_article_is_living_person():
    assert not article_is_living_person("White House")
    assert article_is_living_person("Barack Obama")
    assert not article_is_living_person("Talk:User Rimoll")
    print("success")
