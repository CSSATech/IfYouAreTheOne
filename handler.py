import hashlib
import receive
import reply
import time


users = {}


class Handle(object):
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
		params = request.data
		recMsg = receive.parse_xml(params)

		if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
			toUser = recMsg.FromUserName # wechat user, type 'str'
			fromUser = recMsg.ToUserName # our platform, type 'str'
			content = recMsg.Content.decode() # type 'str'
			now = int(recMsg.CreateTime) # type 'int'

			if toUser in users and now - users[toUser]['createTime'] < 600:
				replyMsg = reply.TextMsg(toUser, fromUser, 'fuck off')
				return replyMsg.send()

			users[toUser] = {}
			users[toUser]['createTime'] = now

			replyMsg = reply.TextMsg(toUser, fromUser, 'From: {}, To: {}, {}'.format(fromUser, toUser, content))
			return replyMsg.send()

		print("Invalid POST request")
		return "success"

