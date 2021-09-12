from app import app, socketio

def testRegister():
    flask_test_client = app.test_client()

    r = flask_test_client.post('/register', json={"username": "ankit123",
        "password": "12345", "emailId":"ankit@abc.com", 
        "firstName":"Ankit","lastName":"Kaira"},
         content_type='application/json')
    assert r.status_code == 200

def testLogin():
    flask_test_client = app.test_client()

    r = flask_test_client.post('/login',json={ 
        'username':'ankit123','password': '12345'},
         content_type='application/json')
    assert r.status_code == 200



def testLogout():
    flask_test_client = app.test_client()

    r = flask_test_client.get('/logout')
    assert r.status_code == 401

if __name__ == '__main__':
    testRegister()
    testLogin()
    testLogout()