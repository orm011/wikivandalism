from wkv_common import *
from user_talk_vandal_vocab_count import *
from user_talk_revision_count import *

def user_talk_vandal_vocab_ratio(username):
    revision_count = user_talk_revision_count(username)
    if revision_count == 0:
        return 0
    vandal_vocab_count = user_talk_vandal_vocab_count(username)
    return float(vandal_vocab_count) / revision_count
