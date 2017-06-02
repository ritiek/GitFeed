#!/usr/bin/env python

# Background color for labels
from colorama import Fore, Back, Style, init
from json import loads
from sys import argv
import requests
import argparse

init(autoreset=True)

def getArgs(argv=None):
	parser = argparse.ArgumentParser(description='Check your GitHub Newsfeed via the command-line.',
	                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-p', '--pages', default=1,
	                    help='number of newsfeed pages to fetch')
	parser.add_argument('-u', '--user', default='ritiek',
	                    help='GitHub username for the user to fetch newsfeed for')
	parser.add_argument('-q', '--quiet', default=False,
	                    help='hide comment body in issues & PRs', action='store_true')
	parser.add_argument('-nt', '--no-time-stamp', default=False,
	                    help='hide time-stamp of events', action='store_true')
	return parser.parse_args(argv)

# review PR
def PRReviewEvent(item, quiet):
	user = item['actor']['login']
	repo = item['repo']['name']
	commit = item['payload']['comment']['commit_id']
	link = item['payload']['pull_request']['html_url']
	title = item['payload']['pull_request']['title']
	number = item['payload']['pull_request']['number']
	body = item['payload']['comment']['body']
	created_at = item['payload']['comment']['created_at']
	#print created_at

	print Fore.GREEN + '{} reviewed pull request {} on {}'.format(user, number, repo)
	if not quiet:
		print body

# open PR, close PR
def PREvent(item, quiet):
	user = item['actor']['login']
	repo = item['repo']['name']
	link = item['payload']['pull_request']['html_url']
	title = item['payload']['pull_request']['title']
	state = item['payload']['pull_request']['state']
	number = item['payload']['pull_request']['number']
	created_at = item['payload']['pull_request']['created_at']
	#print created_at
	if state == 'open':
		print Fore.CYAN + '{} opened pull request {} on {}'.format(user, number, repo)
		print Style.BRIGHT + title
		body = item['payload']['pull_request']['body']
		if not quiet:
			print body
	else:
		print Fore.CYAN + '{} closed pull request {} on {}'.format(user, number, repo)
		print Style.BRIGHT + title

# comment on issue, PR
def issueCommentEvent(item, quiet):
	user = item['actor']['login']
	repo = item['repo']['name']
	link = item['payload']['issue']['html_url']
	labels = item['payload']['issue']['labels']
	#for x in labels:
	#	print x['name']
	state = item['payload']['action']
	number = item['payload']['issue']['number']
	title = item['payload']['issue']['title']
	body = item['payload']['comment']['body']
	created_at = item['payload']['comment']['created_at']
	#print created_at
	try:
		if item['payload']['issue']['pull_request']:
			group = 'pull request'
	except:
		group = 'issue'

	print Fore.CYAN + Style.BRIGHT + '{} commented on {} {} on {}'.format(user, group, number, repo)
	if not quiet:
		print body

# open issue, close issue
def issuesEvent(item, quiet):
	user = item['actor']['login']
	repo = item['repo']['name']
	link = item['payload']['issue']['html_url']
	title = item['payload']['issue']['title']
	state = item['payload']['action']
	number = item['payload']['issue']['number']
	created_at = item['payload']['issue']['created_at']
	#print created_at

	print Fore.RED + Style.BRIGHT + '{} {} issue {} on {}'.format(user, state, number, repo)
	print Style.BRIGHT + title

# starred by following
def watchEvent(item, quiet):
	user = item['actor']['login']
	repo = item['repo']['name']
	link = 'https://github.com/' + item['repo']['name']
	created_at = item['created_at']
	#print created_at
	print Fore.YELLOW + '{} starred {}'.format(user, repo)

# forked by following
def forkEvent(item, quiet):
	user = item['actor']['login']
	repo = item['repo']['name']
	link = 'https://github.com/' + item['repo']['name']
	created_at = item['created_at']
	#print created_at
	print Fore.GREEN + '{} forked {}'.format(user, repo)

# delete branch
def deleteEvent(item, quiet):
	user = item['actor']['login']
	repo = item['repo']['name']
	link = 'https://github.com/' + item['repo']['name']
	branch = item['payload']['ref']
	created_at = item['created_at']
	#print created_at

	print Fore.RED + '{} deleted branch {} at {}'.format(user, branch, repo)

# push commits
def pushEvent(item, quiet):
	event = item['type']
	user = item['actor']['login']
	repo = item['repo']['name']
	link = 'https://github.com/' + item['repo']['name']
	size = item['payload']['size']
	branch = item['payload']['ref'].split('/')[-1]
	created_at = item['created_at']

	print Fore.BLUE + '{} pushed {} new commit(s) to {} at {}'.format(user, size, branch, repo)

# create repo, branch
def createEvent(item, quiet):
	user = item['actor']['login']
	repo = item['repo']['name']
	group = item['payload']['ref_type']
	link = 'https://github.com/' + item['repo']['name']
	created_at = item['created_at']
	#print created_at

	if group == "repository":
		print Fore.MAGENTA + Style.BRIGHT + '{} created {} {}'.format(user, group, repo)
	else:
		branch = item['payload']['ref']
		print Fore.MAGENTA + Style.BRIGHT + '{} created {} {} at {}'.format(user, group, branch, repo)

# make public repo
def publicEvent(item, quiet):
	user = item['actor']['login']
	repo = item['repo']['name']
	link = 'https://github.com/' + item['repo']['name']
	created_at = item['created_at']
	#print created_at

	print Fore.MAGENTA + '{} made {} public'.format(user, repo)

# add collab
def memberEvent(item, quiet):
	user = item['actor']['login']
	repo = item['repo']['name']
	link = 'https://github.com/' + item['repo']['name']
	collab = item['payload']['member']['login']
	action = item['payload']['action']
	created_at = item['created_at']
	#print created_at

	print Fore.MAGENTA + '{} {} {} as a collaborator to {}'.format(user, action, collab, repo)

def getPage(user, page, quiet):
	url = 'https://api.github.com/users/' + user +'/received_events?page='
	response = loads(requests.get(url + str(page)).text)
	for item in reversed(response):
		if not args.no_time_stamp:
			created_at = item['created_at']
			print(Fore.GREEN + Style.BRIGHT + created_at)

		event = item['type']
		if event == "PullRequestReviewCommentEvent": # review PR
			PRReviewEvent(item, quiet)
		elif event == "PullRequestEvent": # open PR, close PR
			PREvent(item, quiet)
		elif event == "IssueCommentEvent": # comment on issue/PR
			issueCommentEvent(item, quiet)
		elif event == "IssuesEvent": # open issue, close issue
			issuesEvent(item, quiet)
		elif event == "WatchEvent": # starred
			watchEvent(item, quiet)
		elif event == "ForkEvent": # fork
			forkEvent(item, quiet)
		elif event == "DeleteEvent": # delete branch
			deleteEvent(item, quiet)
		elif event == "PushEvent": # push commits
			pushEvent(item, quiet)
		elif event == "CreateEvent": # make new repo, branch
			createEvent(item, quiet)
		elif event == "PublicEvent": # make repo public
			publicEvent(item, quiet)
		elif event == "MemberEvent": # add collab
			memberEvent(item, quiet)
		print('')

def getPages(user, max_page, quiet):
	for page in range(max_page, 0, -1):
		getPage(user, page, quiet)

args = getArgs()

user = args.user
max_page = args.pages
quiet = args.quiet
getPages(user, max_page, quiet)
