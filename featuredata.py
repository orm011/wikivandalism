#!/usr/bin/python

import wikipedia_request
import sys

featurename = sys.argv[1]
if featurename[-3:] == '.py':
  featurename = featurename[:-3]
featurefn = getattr(wikipedia_request, featurename)
numexamples = 0
if len(sys.argv) > 2:
  numexamples = int(sys.argv[2])
wikipedia_request.feature_to_text(featurefn, numexamples)

