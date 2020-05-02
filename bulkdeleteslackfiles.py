import urllib
import urllib2
import time
import json

#Slack legacy-token (You can get this from https://api.slack.com/custom-integrations/legacy-tokens)
legacy_token_id = '<account_token>'

#Your Slack account url
base_url = 'https://<slack_account>.slack.com'

#Delete All files across Slack (Account id using Admin account token id) older than 30 days:
d = 10
skippedDays = int(time.time()) - d * 24 * 60 * 60

#Other Slack URL used 
fileListURL = '/api/files.list'
fileDeleteURL = '/api/files.delete'

def listAllfiles(skipNoOfDays):
  params = {
    'token': legacy_token_id,
    'ts_to': skipNoOfDays,
    'count': 600,
  }
  
  
  url = base_url + fileListURL
  response = urllib2.urlopen(url + '?' + urllib.urlencode(params)).read()
  return json.loads(response)['files']

def deletefiles(slackFileIDofFiles):
  for file_id in slackFileIDofFiles:
    params = {
      'token': legacy_token_id
      ,'file': file_id
      }
    url = base_url + fileDeleteURL
    response = urllib2.urlopen(url + '?' + urllib.urlencode(params)).read()
    print "Delete Status:", json.loads(response)['ok'], ", File ID :", file_id, "deleted."

print "Starting File deletion script..."
filesToBeDeleted = listAllfiles(skippedDays)
if len(filesToBeDeleted) == 0:
  print "No files found older than", d, "days"
else:
  print "Files to be deleted are :", len(filesToBeDeleted)
  slackFileIDofFiles = [f['id'] for f in filesToBeDeleted]
  deletefiles(slackFileIDofFiles)
  print "Deletion completed for ",len(filesToBeDeleted), "files."
