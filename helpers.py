import time

def recv_timeout(the_socket,timeout=2):
    
    #make socket non blocking
    the_socket.setblocking(0)
     
    #total data partwise in an array
    total_data=[];
    data='';
     
    #beginning time
    begin=time.time()
    while 1:
        #if you got some data, then break after timeout
        if total_data and time.time()-begin > timeout:
            break
         
        #if you got no data at all, wait a little longer, twice the timeout
        elif time.time()-begin > timeout*2:
            break
         
        #recv something
        try:
            data = the_socket.recv(8192)
            if data:
                retorno = dict([tuple(x.split(': ')) for x in data.decode('UTF-8').split('\r\n') if x != ''])
                total_data.append(retorno)
                #change the beginning time for measurement
                begin=time.time()
            else:
                #sleep for sometime to indicate a gap
                time.sleep(0.1)
        except:
            pass
     
    dict_data = {}
    for d in total_data: dict_data.update(d)      
    return dict_data