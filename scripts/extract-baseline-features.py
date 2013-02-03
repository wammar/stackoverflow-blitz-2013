import sys
import json
#import defaultdict

inFilename = sys.argv[-1]

inFile = open(inFilename, 'r')

for line in inFile:
  obj = json.loads(line)
  features = {}
  features['id'] = int(obj[u'Id'])
#  features['bodyLength'] = len(obj[u'Body'])
#  features['commentCount'] = int(obj[u'Question'][u'CommentCount']) if u'Question' in obj and u'CommentCount' in obj[u'Question'] else 0
#  features['answerId'] = int(obj[u'Id']) 
#  features['ownerUserId'] = int(obj[u'OwnerUserId']) if u'OwnerUserId' in obj else 0
#  features['questionAnswersCount'] = int(obj[u'Question'][u'AnswerCount'])
#  features['questionScore'] = int(obj[u'Question'][u'Score'])
#  features['userReputation'] = int(obj[u'User'][u'Reputation']) if u'User' in obj and obj[u'User'] != None and u'Reputation' in obj[u'User'] else 0
#  features['userDownVotes'] = int(obj[u'User'][u'DownVotes']) if u'User' in obj and obj[u'User'] != None and u'DownVotes' in obj[u'User'] else 0
#  features['userUpVotes'] = int(obj[u'User'][u'UpVotes']) if u'User' in obj and obj[u'User'] != None and u'UpVotes' in obj[u'User'] else 0
#  for(tag in obj[u'Question'][u'Tags'].replace('<', ' ').replace('>', '').split()):
#    features['tag:{0}'.format(tag)] = 1
#  features['questionViews'] = int(obj[u'Question'][u'ViewCount'])
  features['viewCount'] = int(obj[u'ViewCount']) if obj[u'ViewCount'] != u'' else 0
  print json.dumps(features)

inFile.close()
