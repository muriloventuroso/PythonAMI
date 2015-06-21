def pattern_login(username,password,actionid):
    p = """Action: Login
Events: off
Username: %(username)s
Secret: %(password)s
ActionID: %(actionid)s
        """
    pattern = p % {
    'username': username,
    'password': password,
    'actionid': actionid
    }

    return pattern

def pattern_originate_local(number,context_local,context,callerid,priority,exten,timeout,actionid):


    p = """Action: Originate
Channel: Local/%(number)s@%(context_local)s
CallerID: <%(callerid)s>
Context: %(context)s
Priority: 1
Exten: %(exten)s
Async: True
Timeout: %(timeout)s
ActionID: %(actionid)s
        """
    pattern = p % {
        'number': number,
        'timeout': (timeout + 7) * 1000,
        'callerid': callerid,
        'context': context,
        'context_local': context_local,
        'exten': exten,
        'actionid': actionid,
        }

    return pattern