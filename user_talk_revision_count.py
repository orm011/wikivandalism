from wkv_common import *

def user_talk_revision_count(username):
    req = construct_user_talk_page_edits_request(username, 500)
    try:
        count = len(make_wikipedia_request_json(req)['query']['pages'].values()[0]['revisions'])
    except:
        count = 0

    return count
