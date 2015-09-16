import openerplib
HOST = 'localhost'
PORT = 8069
DB = 'training-v9'
USER = 'admin'
PASS = 'admin'

connection = openerplib.get_connection(hostname=HOST, database=DB, login=USER, password=PASS, protocol='xmlrpc', port=PORT)
session_obj = connection.get_model('openacademy.session')
sessions = session_obj.search_read([])

for session in sessions:
    print "Session %s (%s seats)" % (session['name'], session['seats'])

course_id = connection.get_model('openacademy.course').search([('name','ilike','technical')])[0]
session_obj.create({
    'name' : 'My session',
    'course_id' : course_id,
})