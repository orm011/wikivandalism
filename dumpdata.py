#!/usr/bin/python

import wikipedia_request
import sys

featurename = sys.argv[1]
if featurename[-3:] == '.py':
  featurename = featurename[:-3]
featurefn = getattr(wikipedia_request, featurename)
wikipedia_request.editid_to_featurevalues(featurefn)

