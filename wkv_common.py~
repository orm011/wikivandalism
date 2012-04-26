import requests
import simplejson
import csv

""" for the example only"""
import trial_file_reader

__wikipedia_query="http://en.wikipedia.org/w/api.php?action=query"

def construct_user_page_edits_request(username, limit):
    """constructs wikipedia query for user page edits"""
    return  __wikipedia_query + "&titles=User:" + username + "&prop=revisions" + "&format=json" + "&rvlimit="  + str(limit)

def construct_user_talk_page_edits_request(username, limit):
    return  __wikipedia_query + "&titles=User_talk:" + username + "&prop=revisions" + "&format=json" + "&rvlimit="  + str(limit)

def construct_user_talk_page_contents_request(username, limit):
    return  __wikipedia_query + "&titles=User_talk:" + username + "&prop=revisions&rvprop=comment|tags|content" + "&format=json" + "&rvlimit="  + str(limit)
