#!/usr/bin/env python

# Background color for labels
from json import loads
import requests

#user = raw_input('Enter your username: ')
user = 'Ritiek'
url = 'https://api.github.com/users/' + user +'/received_events?page=1'

response = loads(requests.get(url).text)

# review PR
def PRReviewEvent(item):
	event = item['type']
	print event
	commit = item['payload']['comment']['commit_id']
	print commit
	link = item['payload']['pull_request']['html_url']
	title = item['payload']['pull_request']['title']
	print title
	body = item['payload']['comment']['body']
	print body
	print link
	created_at = item['payload']['comment']['created_at']
	print created_at

# open PR, close PR, comment on PR
def PREvent(item):
	event = item['type']
	print event
	link = item['payload']['pull_request']['html_url']
	title = item['payload']['pull_request']['title']
	print title
	#body = item['payload']['comment']['body']
	#print body
	print link
	created_at = item['payload']['pull_request']['created_at']
	print created_at

# comment on issue
def issueCommentEvent(item):
	event = item['type']
	print event
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
	print link
	created_at = item['payload']['comment']['created_at']
	print created_at

# open issue, close issue
def issuesEvent(item):
	event = item['type']
	print event
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

# starred by following
def watchEvent(item):
	event = item['type']
	print event
	link = 'https://github.com/' + item['repo']['name']
	print link
	created_at = item['created_at']
	print created_at

# forked by following
def forkEvent(item):
	event = item['type']
	print event
	link = 'https://github.com/' + item['repo']['name']
	print link
	created_at = item['created_at']
	print created_at

# delete branch
def deleteEvent(item):
	event = item['type']
	print event
	link = 'https://github.com/' + item['repo']['name']
	print link
	branch = item['payload']['ref']
	print branch
	created_at = item['created_at']
	print created_at

# push commits
def pushEvent(item):
	event = item['type']
	print event
	link = 'https://github.com/' + item['repo']['name']
	print link
	size = item['payload']['distinct_size']
	print size
	created_at = item['created_at']
	print created_at

# create repo
def createEvent(item):
	event = item['type']
	print event
	link = 'https://github.com/' + item['repo']['name']
	print link
	created_at = item['created_at']
	print created_at

# make public repo
def publicEvent(item):
	event = item['type']
	print event
	link = 'https://github.com/' + item['repo']['name']
	print link
	created_at = item['created_at']
	print created_at

# add collab
def memberEvent(item):
	event = item['type']
	print event
	link = 'https://github.com/' + item['repo']['name']
	print link
	collab = item['payload']['member']['login']
	print collab
	action = item['payload']['action']
	print action
	created_at = item['created_at']
	print created_at

for item in response:
	user = item['actor']['login']
	print user
	event = item['type']

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
	elif event == "CreateEvent":
		createEvent(item)
	elif event == "PublicEvent":
		publicEvent(item)
	elif event == "MemberEvent":
		memberEvent(item)
	print('')

#print response[1]
