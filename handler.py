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
	
