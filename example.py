from ami import *


options_login = {
	'host':HOST,
	'username':USERNAME,
	'password':PASSWORD

}

asterisk = AMI(**options_login)

if asterisk.status_login:
	options_originate = {
	'number':NUMBER,
	'context_local':CONTEXT_LOCAL,
	'context':CONTEXT,
	'callerid':CALLERID,
	'priority':PRIORITY,
	'exten':EXTENSION,
	'timeout':TIMEOUT

}
	call = asterisk.originate(**options_originate)
	print(call)
