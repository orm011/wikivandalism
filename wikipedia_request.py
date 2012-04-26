import requests
import simplejson
import csv

""" for the example only"""
import trial_file_reader


from user_talk_vandal_vocab_count import *
from user_talk_vandal_vocab_ratio import *
from user_revision_count import *
from user_talk_revision_count import *


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

def join_edits_with_feature_on_user(feature_function, edits):
    """edits are the output from parsing trial.xml"""
    result = []
    for edit in edits:
        try:
            result.append((feature_function(edit['user']), int(edit['isVandalism'] == 'true')))
        except:
            print 'error requesting for: ', edit['user'], 'moving on...'
            
    return result

def dump_to_csv(tuple_list, file_name):
    f = open(file_name, "w")
    wr = csv.writer(f)
    for tup in tuple_list:
        wr.writerow(tup)
    f.close()
    
def example():
    trialxmlpath = "../workspace/cluebotng/editsets/D/trial.xml"
    trainingset = trial_file_reader.parse_trial_file(trialxmlpath)
    exampleset = trainingset[0:10]
    examplefeature = user_talk_revision_count #user feature defined above
    x = join_edits_with_feature_on_user(examplefeature, exampleset)
    dump_to_csv(x, "examplefeature.csv")


