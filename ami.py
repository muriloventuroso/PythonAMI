import socket
from helpers import recv_timeout
from pattern import *
class AMI(object):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.connect()


    def connect(self):
        import uuid
        from datetime import datetime
        
        actionid = str(uuid.uuid4())
        timeout = 10
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, 5038))
        data = self.s.recv(8192)

        login = pattern_login(self.username,self.password,actionid)

        for l in login.split('\n'):
            self.s.send(bytes(l+'\r\n','UTF-8'))

        self.s.send(bytes('\r\n','UTF-8'))
        data = recv_timeout(self.s)
        begin = datetime.now()
        while 1:

            if 'Success' in data.values() and actionid in data.values():

                self.status_login = True
                return
            elif 'Failure' in data.values() and actionid in data.values():
                self.status_login = False
                return
            else:
                difference = datetime.now() - begin

                if  difference.seconds > timeout + 7:
                    self.status_login = False
                    return
                data = recv_timeout(self.s)


    def originate(self,**kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        import uuid
        actionid = str(uuid.uuid4())

        originate = pattern_originate_local(
            self.number,
            self.context_local,
            self.context,
            self.callerid,
            self.priority,
            self.exten,
            self.timeout,
            actionid
            )

        for l in originate.split('\n'):

            self.s.send(bytes(l+'\r\n','UTF-8'))

        
        self.s.send(bytes('\r\n','UTF-8'))
        data = recv_timeout(self.s)




        result = False
        from datetime import datetime
        begin = datetime.now()
        
        while 1:

            if 'Success' in data.values() and actionid in data.values():
                result = True
                break
            elif 'Failure' in data.values() and actionid in data.values():
                break
            else:
                difference = datetime.now() - begin

                if  difference.seconds > self.timeout + 7:

                    break
                data = recv_timeout(self.s)


        return result

    def close(self):
        self.s.close()
