# GitHub-Newsfeed

Check your GitHub Newsfeed via the command-line

## Screenshots

## Installation

GitFeed can be installed from pypi.

```
pip install gitfeed
```

or if you like to live on the bleeding edge

```
git clone https://github.com/Ritiek/GitFeed
cd GitFeed
python setup.py install
```

## Usage

- Run it using `gitfeed`

- The first time you launch `gitfeed`, it will ask you for GitHub username and set it as the default username to fetch news for.

- You can even fetch news for any other user provided you know their GitHub username.

- Full list of supported options:

```
usage: gitfeed [-h] [-u USER] [-p PAGES] [-q] [-nt] [-ns]

Check your GitHub Newsfeed via the command-line.

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  GitHub username for the user to fetch newsfeed for
                        (default: <user>)
  -p PAGES, --pages PAGES
                        number of newsfeed pages to fetch (default: 1)
  -q, --quiet           hide comment body in issues & PRs (default: False)
  -nt, --no-time-stamp  hide time-stamp of events (default: False)
  -ns, --no-style       show plain white text with no colors or style
                        (default: False)
```

- You can modify the default configuration by editing `~/.gitfeed/gitfeed.ini`

## License

`The MIT License`
