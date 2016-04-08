#bklo94
#simple bot to look at sales thread on reddit and alert myself

import praw
import time
import sqlite3
import traceback

KEYWORDS = ['GPU', 'HDD', 'SSD', 'MOBO','CPU']

KEYAUTHORS = []

SUBREDDIT = "buildapcsales"

MAILRECIPIENT = "kenshin421"

MAILSUBJECT = "NEW SALES THREAD"

MAILMESSAGE = "[/u/_author_ said these keywords in /r/_subreddit_:_results_](_permalink_)"

MULTIPLE_MESSAGE_SEPERATOR = '\n\n_____\n\n'

MAXPOSTS = 100

WAIT = 30

DO_COMMENTS = False
DO_SUBMISSIONS = True

PERMALINK_SUBMISSION = 'https://reddit.com/r/%s/comments/%s'
PERMALINK_COMMENT = 'https://reddit.com/r/%s/comments/%s/_/%s'

CLEANCYCLES = 10

try:
	import obot
	r = obot.login()
	print('Logging in')
except ImportError:
	pass

sql = sqlite3.connect('sql.db')
cur = sql.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS oldposts(id TEXT)')
sql.commit()

KEYWORDS =[k.lower() for k in KEYWORDS]

def mailme():
	print('Searching %s.' % SUBREDDIT)
	subreddit = r.get_subreddit(SUBREDDIT)

	posts = []
	if DO_SUBMISSIONS:
		print('Collecting Submissions')
		posts += list(subreddit.get_new(limit=MAXPOSTS))
	if DO_COMMENTS:
		print('Collecting Comments')
		posts += list(subreddit.get_comments(limit=MAXPOSTS))

	posts.sort(key= lambda x: x.created_utc)

	message_results = []

	for post in posts:
		pid = post.id


		try:
			pauthor = post.author.name
		except AttributeError:
			continue

		if r.has_scope('identity'):
			myself = r.user.name.lower()
		else:
			myself = ''

		if pauthor.lower() in [myself, MAILRECIPIENT.lower()]:
			print('Will not reply to myself.')
			continue

		if KEYAUTHORS != [] and all(auth.lower() != pauthor for auth in KEYAUTHORS):
			continue

		cur.execute('SELECT * FROM oldposts WHERE ID=?', [pid])
		sql.commit()

		subreddit = post.subreddit.display_name
		if isinstance(post,praw.objects.Submission):
			pbody = '%s\n\n%s' % (post.title.lower(), post.selftext.lower())
			permalink = PERMALINK_SUBMISSION % (subreddit, post.id)

		elif isinstance(post, praw.objects.Comment):
			pbody = post.body.lower()
			link = post.link_id.split('_')[-1]
			permalink = PERMALINK_COMMENT % (subreddit, link, post.id)

		matched_keywords = []
		for key in KEYWORDS:
			if key not in pbody:
				continue
			matched_keywords.append(key)
		if len(matched_keywords) == 0:
			continue

		message = MAILMESSAGE
		message = message.replace('_author_', pauthor)
		message = message.replace('_subreddit_', subreddit)
		message = message.replace('_id_', pid)
		message = message.replace('_permalink_', permalink)
		if '_results_' in message:
			matched_keywords = [('"%s"' % x) for x in matched_keywords]
			matched_keywords = '[%s]' % (', '.join(matched_keywords))
			message = message.replace('_results_', matched_keywords)

		message_results.append(message)

		if len(message_results) == 0:
			return

		print('Sending MailMe Message with %d results' % len(message_results))
		message = MULTIPLE_MESSAGE_SEPERATOR.join(message_results)
		r.send_message(MAILRECIPIENT,MAILSUBJECT,message)

cycles = 0
while True:
	try:
		mailme()
		cycles += 1
	except Exception as e:
		traceback.print_exc()
	if cycles >= CLEANCYCLES:
		print('Cleaning database')
		cur.execute('DELETE FROM oldposts WHERE id NOT IN (SELECT id FROM oldposts ORDER BY id DESC LIMIT?)', [MAXPOSTS *2])
		sql.commit()
		cycles = 0
	print('Running again in %d seconds \n' % WAIT)
	time.sleep(WAIT)
