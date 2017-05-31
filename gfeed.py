#!/usr/bin/env python

# Background color for labels
from json import loads
import requests

#user = raw_input('Enter your username: ')
user = 'Ritiek'
url = 'https://api.github.com/users/' + user +'/received_events?page=1'

response = loads(requests.get(url).text)

print 'done'
for item in response:
	user = item['actor']['login']
	print user
	event = item['type']
	print event
	if event == "PullRequestReviewCommentEvent": # review PR
		commit = item['payload']['comment']['commit_id']
		print commit
		link = item['payload']['pull_request']['html_url']
		title = item['payload']['pull_request']['title']
		print title
		body = item['payload']['comment']['body']
		print body
		created_at = item['payload']['comment']['created_at']
		print created_at
	elif event == "PullRequestEvent": # open PR
		link = item['payload']['pull_request']['html_url']
		title = item['payload']['pull_request']['title']
		print title
		#body = item['payload']['comment']['body']
		#print body
		#created_at = item['payload']['comment']['created_at']
		#print created_at
	elif event == "IssueCommentEvent": # comment on issue/PR
		link = item['payload']['issue']['html_url']
		labels = item['payload']['issue']['labels']
		for x in labels:
			print x['name']
		title = item['payload']['issue']['title']
		print title
		body = item['payload']['comment']['body']
		print body
		created_at = item['payload']['comment']['created_at']
		print created_at
	elif event == "IssuesEvent": # open issue
		link = item['payload']['issue']['html_url']
		title = item['payload']['issue']['title']
		print title
		body = item['payload']['comment']['body']
		print body
		created_at = item['payload']['comment']['created_at']
		print created_at
	elif event == "WatchEvent": # starred
		link = 'https://github.com/' + item['repo']['name']
	elif event == "ForkEvent": # fork
		link = 'https://github.com/' + item['repo']['name']

	print link

#print response[1]
