import requests
import simplejson
import csv

""" for the example only"""
import trial_file_reader

import redis
rdb = redis.StrictRedis(host='localhost', port=6379, db=0)
print 'connected to redis database'

class WikipediaError(Exception):
    pass


def make_wikipedia_request(req):
    """connects to wikipedia and collects answer"""
    rcached = rdb.get(req)
    if rcached:
      return rcached
    try:
        res = requests.get(req)
        if not res.ok:
            raise  WikipediaError, res.error
    except:
            raise  WikipediaError
    rdb.set(req, res.text)
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

__wikipedia_query="http://en.wikipedia.org/w/api.php?action=query"


def construct_user_page_edits_request(username, limit):
    """constructs wikipedia query for user page edits"""
    return  __wikipedia_query + "&titles=User:" + username + "&prop=revisions" + "&format=json" + "&rvlimit="  + str(limit)

def construct_user_talk_page_edits_request(username, limit):
    return  __wikipedia_query + "&titles=User_talk:" + username + "&prop=revisions" + "&format=json" + "&rvlimit="  + str(limit)

def construct_user_talk_page_contents_request(username, limit):
    return  __wikipedia_query + "&titles=User_talk:" + username + "&prop=revisions&rvprop=comment|tags|content" + "&format=json" + "&rvlimit="  + str(limit)
