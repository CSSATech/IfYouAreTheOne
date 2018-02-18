import hashlib
import receive
import reply
import time
import random


users = {} # our database
index_female = 0
index_male = 0
random_numbers = ['%04d' % num for num in random.sample(range(1, 1000), 666)]


class Handler(object):
	def get(self, request):
		params = request.args

		signature = params.get('signature')
		timestamp = params.get('timestamp')
		nonce = params.get('nonce')
		echostr = params.get('echostr')

		if None in [signature, timestamp, nonce, echostr]:
			return ""

		token = 'iajboiJ3ighjIJFIOJ90j0j4j0j'
	
		# hashing and mapping
		l = [token, timestamp, nonce]
		l.sort()
		sha1 = hashlib.sha1()
		for e in l: # python 2 map sucks
			sha1.update(e.encode())
		hashcode = sha1.hexdigest()

		print('GET - hashcode: {}, signature: {}'.format(hashcode, signature))

		if hashcode == signature:
			return echostr
		return ""

	def post(self, request):
		global index_male, index_female, random_numbers

		params = request.data
		recMsg = receive.parse_xml(params)

		if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
			toUser = recMsg.FromUserName # wechat user, type 'str'
			fromUser = recMsg.ToUserName # our platform, type 'str'
			content = recMsg.Content.decode() # type 'str'
			now = int(recMsg.CreateTime) # type 'int'

			if toUser in users and now - users[toUser]['createTime'] < 5:
				replyMsg = reply.TextMsg(toUser, fromUser, 'fuck off')
				return replyMsg.send()

			if content == '我是女生':
				replyMsg = reply.TextMsg(toUser, fromUser, random_numbers[index_female])
				index_female += 1
			elif content == '我是男生':
				replyMsg = reply.TextMsg(toUser, fromUser, random_numbers[index_male])
				index_male += 1
			else:
				replyMsg = reply.TextMsg(toUser, fromUser, 'shut the fuck up')
				return replyMsg.send()
				
			users[toUser] = {}
			users[toUser]['createTime'] = now

			# replyMsg = reply.TextMsg(toUser, fromUser, 'From: {}, To: {}, {}'.format(fromUser, toUser, content))
			return replyMsg.send()

		print("Invalid POST request")
		return "success"

