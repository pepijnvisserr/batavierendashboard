from eca import *

import random
from eca.generators import start_offline_tweets

import datetime
import textwrap
import pprint
import re
## You might have to update the root path to point to the correct path
## (by default, it points to <rules>_static)
# root_content_path = 'template_static'


# binds the 'setup' function as the action for the 'init' event
# the action will be called with the context and the event
@event('init')
def setup(ctx, e):
    ctx.count = 0
    fire('sample', {'previous': 0.0})
	# start the offline tweet stream
    start_offline_tweets('data/bata_2014.txt', 'tweet', time_factor=10000)

# simple word splitter
pattern = re.compile('\W+')

# sample stopword list, needs to be much more sophisticated
stopwords = ['het', 'een', 'aan', 'zijn', 'http', 'www', 'com', 'ben', 'jij']

# define a normal Python function
def clip(lower, value, upper):
    return max(lower, min(value, upper))

@event('sample')
def generate_sample(ctx, e):
    ctx.count += 1
    if ctx.count % 50 == 0:
        emit('debug', {'text': 'Log message #'+str(ctx.count)+'!'})

    # base sample on previous one
    sample = clip(-100, e.data['previous'] + random.uniform(+5.0, -5.0), 100)

    # emit to outside world
    emit('sample',{
        'action': 'add',
        'value': sample
    })

    # chain event
    fire('sample', {'previous': sample}, delay=0.05)

#THIS IS WORDCLOUD

# This function will be called to set up the HTTP server
def add_request_handlers(httpd):
    # use the library content from the template_static dir instead of our own
    # this is a bit finicky, since execution now depends on a proper working directory.
    httpd.add_content('/lib/', 'dashboard_static/lib')
    httpd.add_content('/style/', 'dashboard_static/style')


def words(message):
    result = pattern.split(message)
    result = map(lambda w: w.lower(), result)
    result = filter(lambda w: w not in stopwords, result)
    result = filter(lambda w: len(w) > 2, result)
    return result

@event('tweet')
def echo(ctx,e):
    emit('tweet', e.data)