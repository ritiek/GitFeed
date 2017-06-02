#!/usr/bin/env python

# Background color for labels
from colorama import Fore, Back, Style, init
from json import loads
import requests

init(autoreset=True)

#user = raw_input('Enter your username: ')
user = 'ritiek'
url = 'https://api.github.com/users/' + user +'/received_events?page=1'

response = loads(requests.get(url).text)

# review PR
def PRReviewEvent(item):
	#event = item['type']
	#print event
	user = item['actor']['login']
	#print user
	repo = item['repo']['name']
	#print repo
	commit = item['payload']['comment']['commit_id']
	#print commit
	link = item['payload']['pull_request']['html_url']
	title = item['payload']['pull_request']['title']
	#print title
	number = item['payload']['pull_request']['number']
	#print number
	body = item['payload']['comment']['body']
	#print body
	#print link
	created_at = item['payload']['comment']['created_at']
	#print created_at

	print Fore.GREEN + '{} reviewed pull request {} on {}'.format(user, number, repo)
	print body

# open PR, close PR
def PREvent(item):
	#event = item['type']
	#print event
	user = item['actor']['login']
	#print user
	repo = item['repo']['name']
	#print repo
	link = item['payload']['pull_request']['html_url']
	title = item['payload']['pull_request']['title']
	#print title
	state = item['payload']['pull_request']['state']
	#print state
	number = item['payload']['pull_request']['number']
	#print number
	#body = item['payload']['comment']['body']
	#print body
	#print link
	created_at = item['payload']['pull_request']['created_at']
	#print created_at

	print Fore.CYAN + Style.BRIGHT + '{} {} pull request {} on {}'.format(user, state, number, repo)
	print Style.BRIGHT + title

# comment on issue, PR
def issueCommentEvent(item):
	#event = item['type']
	#print event
	user = item['actor']['login']
	#print user
	repo = item['repo']['name']

	#print repo
	link = item['payload']['issue']['html_url']
	labels = item['payload']['issue']['labels']
	#for x in labels:
	#	print x['name']
	state = item['payload']['action']
	#print state
	number = item['payload']['issue']['number']
	#print number
	title = item['payload']['issue']['title']
	#print title
	body = item['payload']['comment']['body']
	#print body
	#print link
	created_at = item['payload']['comment']['created_at']
	#print created_at
	try:
		if item['payload']['issue']['pull_request']:
			group = 'pull request'
	except:
		group = 'issue'

	print Fore.CYAN + '{} commented on {} {} on {}'.format(user, group, number, repo)
	print body

# open issue, close issue
def issuesEvent(item):
	#event = item['type']
	#print event
	user = item['actor']['login']
	#print user
	repo = item['repo']['name']
	#print repo
	link = item['payload']['issue']['html_url']
	title = item['payload']['issue']['title']
	#print title
	state = item['payload']['action']
	number = item['payload']['issue']['number']
	#print number
	#print state
	try:
		body = item['payload']['comment']['body']
		#print body
	except:
		pass
	created_at = item['payload']['issue']['created_at']
	#print created_at
	#print link

	print Fore.RED + Style.BRIGHT + '{} {} issue {} on {}'.format(user, state, number, repo)
	print Style.BRIGHT + title

# starred by following
def watchEvent(item):
	#event = item['type']
	#print event
	user = item['actor']['login']
	#print user
	repo = item['repo']['name']
	#print repo
	link = 'https://github.com/' + item['repo']['name']
	#print link
	created_at = item['created_at']
	#print created_at
	print Fore.YELLOW + '{} starred {}'.format(user, repo)

# forked by following
def forkEvent(item):
	#event = item['type']
	#print event
	user = item['actor']['login']
	#print user
	repo = item['repo']['name']
	link = 'https://github.com/' + item['repo']['name']
	#print link
	created_at = item['created_at']
	#print created_at
	print Fore.GREEN + '{} forked {}'.format(user, repo)

# delete branch
def deleteEvent(item):
	#event = item['type']
	#print event
	user = item['actor']['login']
	#print user
	repo = item['repo']['name']
	#print repo
	link = 'https://github.com/' + item['repo']['name']
	#print link
	branch = item['payload']['ref']
	#print branch
	created_at = item['created_at']
	#print created_at

	print Fore.RED + '{} deleted branch {} at {}'.format(user, branch, repo)

# push commits
def pushEvent(item):
	event = item['type']
	#print event
	user = item['actor']['login']
	#print user
	repo = item['repo']['name']
	#print repo
	link = 'https://github.com/' + item['repo']['name']
	#print link
	size = item['payload']['size']
	#print size
	branch = item['payload']['ref'].split('/')[-1]
	#print branch
	created_at = item['created_at']
	#print created_at

	print Fore.BLUE + '{} pushed {} new commit(s) to {} at {}'.format(user, size, branch, repo)

# create repo, branch
def createEvent(item):
	#event = item['type']
	#print event
	user = item['actor']['login']
	#print user
	repo = item['repo']['name']
	#print repo
	group = item['payload']['ref_type']
	#print group
	link = 'https://github.com/' + item['repo']['name']
	#print link
	created_at = item['created_at']
	#print created_at

	if group == "repository":
		print Fore.MAGENTA + Style.BRIGHT + '{} created {} {}'.format(user, group, repo)
	else:
		branch = item['payload']['ref']
		print Fore.MAGENTA + Style.BRIGHT + '{} created {} {} at {}'.format(user, group, branch, repo)

# make public repo
def publicEvent(item):
	#event = item['type']
	#print event
	user = item['actor']['login']
	#print user
	repo = item['repo']['name']
	#print repo
	link = 'https://github.com/' + item['repo']['name']
	#print link
	created_at = item['created_at']
	#print created_at

	print Fore.MAGENTA + '{} made {} public'.format(user, repo)

# add collab
def memberEvent(item):
	#event = item['type']
	#print event
	user = item['actor']['login']
	#print user
	repo = item['repo']['name']
	#print repo
	link = 'https://github.com/' + item['repo']['name']
	#print link
	collab = item['payload']['member']['login']
	#print collab
	action = item['payload']['action']
	#print action
	created_at = item['created_at']
	#print created_at

	print Fore.MAGENTA + '{} added {} as a collaborator to {}'.format(user, collab, repo)

for item in reversed(response):
	event = item['type']
	#print event

	if event == "PullRequestReviewCommentEvent": # review PR
		PRReviewEvent(item)
	elif event == "PullRequestEvent": # open PR, close PR
		PREvent(item)
	elif event == "IssueCommentEvent": # comment on issue/PR
		issueCommentEvent(item)
	elif event == "IssuesEvent": # open issue, close issue
		issuesEvent(item)
	elif event == "WatchEvent": # starred
		watchEvent(item)
	elif event == "ForkEvent": # fork
		forkEvent(item)
	elif event == "DeleteEvent": # delete branch
		deleteEvent(item)
	elif event == "PushEvent": # push commits
		pushEvent(item)
	elif event == "CreateEvent": # make new repo, branch
		createEvent(item)
	elif event == "PublicEvent": # make repo public
		publicEvent(item)
	elif event == "MemberEvent": # add collab
		memberEvent(item)
	print('')

#print response[1]
