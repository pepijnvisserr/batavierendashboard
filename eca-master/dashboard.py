from eca import *
from eca.generators import start_offline_tweets

import random
import datetime
import textwrap

## You might have to update the root path to point to the correct path
## (by default, it points to <rules>_static)
# root_content_path = 'template_static'


# binds the 'setup' function as the action for the 'init' event
# the action will be called with the context and the event
@event('init')
def setup(ctx, e):
    ctx.counttweets = 0
    fire('activity')
    start_offline_tweets('data/bata_2014.txt', time_factor=100000000)


# define a normal Python function
def clip(lower, value, upper):
    return max(lower, min(value, upper))


@event('activity')
def generate_sample(ctx, e):
    

	# base sample on previous one
	sample = clip(0, ctx.counttweets, 400)
	# emit to outside world
	if (sample == 0):
		sample = 0.0000000000001
	emit('activity',{
		'action': 'add',
		'value': sample
	})


	ctx.counttweets = 0
	# chain event
	fire('activity', delay=2)



@event('chirp')
def tweet(ctx, e):
    # we receive a tweet
    tweet = e.data

    # parse date
    time = datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S %z %Y')

    # nicify text
    text = textwrap.fill(tweet['text'],initial_indent='    ', subsequent_indent='    ')

    # generate output
    output = "[{}] {} (@{}):\n{}".format(time, tweet['user']['name'], tweet['user']['screen_name'], text)
    emit('chirp', output)


@event('tweet')
def echo(ctx,e):
	ctx.counttweets += 1
	emit('tweet', e.data)
	tweetdata = e.data
	announcenames = {"Batavierenrace", "Overijssel_", "GelderlandNieuw"}
	goodname = False
	for y in announcenames:
		if tweetdata['user']['screen_name'] == y:
			goodname = True

	if tweetdata['user']['verified'] or goodname:
		emit('importanttweet', tweetdata)