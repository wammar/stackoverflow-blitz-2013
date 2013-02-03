B1;2cstackoverflow-blitz-2013
========================

dump version: 2012/08/12

the following command pretty-prints the stackoverflow answers data at ./response
python scripts/pprint-file.py responses/train.json.sample

the following command extracts features from one of the files at the ./response directory
python scripts/extract-baseline-features.py responses/train.json.sample > trainFeatures/features1.json
python scripts/extract-baseline-features.py responses/dev.json.sample > evalFeatures/features1.json

the following command trains a linear regression model using creg (the python interface) with features extracted with the previous commands, and computes the mean square error for a given evaluation set
python scripts/train-and-test-scores.py -tf trainFeatures/features1.json -ef evalFeatures/features1.json -tr responses/train.json.sample -er responses/dev.json.sample 

