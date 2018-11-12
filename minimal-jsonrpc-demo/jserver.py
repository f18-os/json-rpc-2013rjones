# minimalistic server example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart
import socket
import pickle
from node import *
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)


# Class providing functions for the client to use:
@service_class
class ServerServices(object):

  @request
  def swapper(self, txt):
    return ''.join(reversed(list(txt)))

  @request
  def nop(self, txt):
    print(txt)
    return txt


  @request
  def increment(self,fileName):
    #print('fileName: '+ fileName)
    
    #print('Trying load')
    with open(fileName, 'rb') as f:
                root = pickle.load(f)
       
    increment(root)
    #dump back the incremented root
    with open(fileName, "wb") as f:
        pickle.dump(root, f)
    
    
        
# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50009))
ss.listen(10)

while True:
  s, _ = ss.accept()
  # JSONRpc object spawns internal thread to serve the connection.
  JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)
