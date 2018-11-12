# minimalistic client example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
import pickle
import base64
from node import *
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50007))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()



# Execute in server:
#result = server.swapper('Hello World!')
# "!dlroW olleH"
#print(result)


#print(server.nop({1:[2,3]}))


leaf1 = node("leaf1")
leaf2 = node("leaf2")

root = node("root", [leaf1, leaf1, leaf2])

print("graph before increment")
root.show()

pickledRoot = pickle.dumps(root)

print(pickledRoot)

mystr = pickledRoot.decode('unicode-escape')

print()

print("Converted")
print(mystr)
server.increment(mystr)

#root = pickle.loads(pickledRoot)

#print("graph after increment")
#root.show()

rpc.close() # Closes the socket 's' also


