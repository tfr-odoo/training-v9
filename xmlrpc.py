import xmlrpclib
HOST = 'localhost'
PORT = 8069
DB = 'training-v9'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print "Logged in as %s (uid:%d)" % (USER,uid)

proxy = xmlrpclib.ServerProxy(ROOT + 'object')

# 2. Read the sessions
sessions = proxy.execute(DB, uid, PASS, 'openacademy.session','search_read', [], ['name','seats'])
for session in sessions:
    print "Session %s (%s seats)" % (session['name'], session['seats'])
# 3.create a new session

course_id = proxy.execute(DB, uid, PASS, 'openacademy.course', 'search', [('name','ilike','technical')])[0]
print course_id

session_id = proxy.execute(DB, uid, PASS, 'openacademy.session', 'create', {
    'name' : 'My session',
    'course_id' : course_id,
})
