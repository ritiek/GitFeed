#!/usr/bin/env python

# Background color for labels
from json import loads
import requests

user = raw_input('Enter your username: ')
url = 'https://api.github.com/users/' + user +'/received_events?page=1'

response = loads(requests.get(url).text)

user = response[0]['actor']['login']
print user
event = response[0]['type']
print event
if event == "PullRequestReviewCommentEvent":
	commit = response[0]['payload']['comment']['commit_id']
	print commit
	link = response[0]['payload']['pull_request']['html_url']
elif event == "IssueCommentEvent":
	link = response[0]['payload']['issue']['html_url']
	labels = response[0]['payload']['issue']['labels']
	for x in labels:
		print x['name']

print link
body = response[0]['payload']['comment']['body']
print body
created_at = response[0]['payload']['comment']['created_at']
print created_at

#print response[1]
