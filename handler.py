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
		else:
			return ""

	def post(self, request):
		params = request.data
		recMsg = receive.parse_xml(params)

		if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
			createTime = recMsg.CreateTime
			toUser = recMsg.FromUserName # wechat user
			fromUser = recMsg.ToUserName # our platform
			content = recMsg.Content.decode()
			now = time.time()

			print(type(toUser))
			print(type(createTime))
			print(type(fromUser))
			print(type(content))
			print(toUser)
			print(createTime)
			print(fromUser)
			print(content)

			replyMsg = reply.TextMsg(toUser, fromUser, 'From: {}, To: {}, {}'.format(fromUser, toUser, content))

			return replyMsg.send()
		else:
			print("Invalid POST request")
			return "success"

