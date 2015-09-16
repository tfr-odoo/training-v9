'''
Created on 15 sept. 2015

@author: odoo
'''
# sudo pip install jsonrpclib
import jsonrpclib

HOST = 'localhost'
PORT = 8069
DB = 'training-v9'
USER = 'admin'
PASS = 'admin'
# server proxy object
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
server = jsonrpclib.Server(url)

# log in the given database
uid = server.call(service="common", method="login", args=[DB, USER, PASS])

# helper function for invoking model methods
def invoke(model, method, *args):
    args = [DB, uid, PASS, model, method] + list(args)
    return server.call(service="object", method="execute", args=args)

# create a new note
res = invoke('openacademy.session', 'search_read', [])
import pprint
pprint.pprint(res)