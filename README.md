# PythonAMI
Simple Python library for sending calls through Asterisk Manager Interface


#Purpouse
PythonAMI is a simple library for sending Python calls to an Asterisk server using AMI. 

For the next versions will be available sending variables for the Asterisk context and implement new AMI commands.

#Usage

Sign in server AMI passing your credentials.

```
from ami import *

options_login = {
	'host':HOST,
	'username':USENAME,
	'password':PASSWORD

}

asterisk = AMI(**options_login)
```

Check whether the login was made and send the call.
```
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
```
