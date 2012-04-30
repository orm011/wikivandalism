import requests
import simplejson
import csv

""" for the example only"""
import trial_file_reader


from user_talk_vandal_vocab_count import *
from user_talk_vandal_vocab_ratio import *
from user_revision_count import *
from user_talk_revision_count import *
from user_article_to_edit_ratio import *
from user_empty_comment_ratio import *
from user_comment_avg_length import *
from user_edit_to_reversion_ratio import *

#from user_external_link_ratio import *

from edited_article_user_num_edits import *
from user_has_edited_talk_page import *

def join_edits_with_feature_on_user(feature_function, edits):
    """edits are the output from parsing trial.xml"""
    result = []
    for edit in edits:
        try:
            featureval = 0
            if feature_function.__name__[0:4] == 'edit':
                featureval = feature_function(edit)
            else:
                featureval = feature_function(edit['user'])
            result.append((featureval, 
                           int(edit['isVandalism'] == 'true')))
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
    """example of how you can use the functions in this file"""
    trialxmlpath = "../workspace/cluebotng/editsets/D/trial.xml"
    trainingset = trial_file_reader.parse_trial_file(trialxmlpath)
    exampleset = trainingset[0:10]
    examplefeature = user_talk_revision_count #user feature defined above
    x = join_edits_with_feature_on_user(examplefeature, exampleset)
    dump_to_csv(x, "examplefeature.csv")

def feature_to_text(feature_function, number_of_examples=10, trialxmlpath = "../workspace/cluebotng/editsets/D/trial.xml"):
    """use this to get a new feature for the dataset stored into a file"""
    print 'reading training set from ' + trialxmlpath
    trainingset = trial_file_reader.parse_trial_file(trialxmlpath)
    print 'done reading training set'
    if number_of_examples <= 0:
        exampleset = trainingset[:]
    else:
        exampleset = trainingset[0:number_of_examples]
    x = join_edits_with_feature_on_user(feature_function, exampleset)
    filename = feature_function.__name__ + '.csv'
    dump_to_csv(x, filename)





