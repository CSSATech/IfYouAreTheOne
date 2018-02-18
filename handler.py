import hashlib
import receive
import reply


class Handle(object):
	def get(self, request):
		params = request.args

		signature = params.get('signature')
		timestamp = params.get('timestamp')
		nonce = params.get('nonce')
		echostr = params.get('echostr')

		token = 'iajboiJ3ighjIJFIOJ90j0j4j0j'
	
		# hashing and mapping
		l = [token, timestamp, nonce]
		l.sort()
		sha1 = hashlib.sha1()
		map(sha1.update, l)
		hashcode = sha1.hexdigest()

		print('GET - hashcode: {}, signature: {}'.format(hashcode, signature))

		if hashcode == signature:
			return echostr
		else:
			return ""

	def post(self, request):
		params = request.form

		recMsg = receive.parse_xml(params)
		if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
			toUser = recMsg.FromUserName
			fromUser = recMsg.ToUserName
			content = "test"
			replyMsg = reply.TextMsg(toUser, fromUser, content)
			return replyMsg.send()
		else:
			print("暂且不处理")
			return "success"
