from wkv_common import *

def user_revision_count(editinfo):
    """actual feature, connects to wikpedia"""
    username = editinfo['user']
    req = construct_user_page_edits_request(username,500)
    return len(get_user_page_revisions(make_wikipedia_request(req)))
