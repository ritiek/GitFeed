#!/usr/bin/env python

# Background color for labels
from json import loads
import requests

#user = raw_input('Enter your username: ')
user = 'Ritiek'
url = 'https://api.github.com/users/' + user +'/received_events?page=1'

response = loads(requests.get(url).text)

def PRReviewEvent(item):
	commit = item['payload']['comment']['commit_id']
	print commit
	link = item['payload']['pull_request']['html_url']
	title = item['payload']['pull_request']['title']
	print title
	body = item['payload']['comment']['body']
	print body
	created_at = item['payload']['comment']['created_at']
	print created_at
	print link

def PREvent(item):
	link = item['payload']['pull_request']['html_url']
	title = item['payload']['pull_request']['title']
	print title
	#body = item['payload']['comment']['body']
	#print body
	created_at = item['payload']['pull_request']['created_at']
	print created_at
	print link

def issueCommentEvent(item):
	link = item['payload']['issue']['html_url']
	labels = item['payload']['issue']['labels']
	for x in labels:
		print x['name']
	state = item['payload']['action']
	print state
	title = item['payload']['issue']['title']
	print title
	body = item['payload']['comment']['body']
	print body
	created_at = item['payload']['comment']['created_at']
	print created_at
	print link

def issuesEvent(item):
	link = item['payload']['issue']['html_url']
	title = item['payload']['issue']['title']
	print title
	state = item['payload']['action']
	print state
	try:
		body = item['payload']['comment']['body']
		print body
		created_at = item['payload']['comment']['created_at']
		print created_at
	except:
		pass
	print link

def watchEvent(item):
	link = 'https://github.com/' + item['repo']['name']
	print link

def forkEvent(item):
	link = 'https://github.com/' + item['repo']['name']
	print link

def deleteEvent(item):
	link = 'https://github.com/' + item['repo']['name']
	print link
	branch = item['payload']['ref']
	print branch

def pushEvent(item):
	link = 'https://github.com/' + item['repo']['name']
	print link
	size = item['payload']['distinct_size']
	print size

for item in response:
	user = item['actor']['login']
	print user
	event = item['type']
	print event

	if event == "PullRequestReviewCommentEvent": # review PR
		PRReviewEvent(item)
	elif event == "PullRequestEvent": # open PR
		PREvent(item)
	elif event == "IssueCommentEvent": # comment on issue/PR
		issueCommentEvent(item)
	elif event == "IssuesEvent": # open issue/close issue
		issuesEvent(item)
	elif event == "WatchEvent": # starred
		watchEvent(item)
	elif event == "ForkEvent": # fork
		forkEvent(item)
	elif event == "DeleteEvent": # delete branch
		deleteEvent(item)
	elif event == "PushEvent": # push commits
		pushEvent(item)
	print('')

#print response[1]
