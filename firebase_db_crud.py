from firebase import firebase
 
 
firebase = firebase.FirebaseApplication(database_url, None)
data =  { 'Name': 'Raj Singh',
          'RollNo': 3,
          'Percentage': 70.02
          }

#post data
result = firebase.post('/python-example-bdb32/Students/',data)
print(result)
 
# get data
result2 = firebase.get('/python-example-bdb32/Students/', '')
print(result2)

#update data
firebase.put('/python-example-bdb32/Students/<token>','Name','Bob')
print('Record Updated')

#delete data
firebase.delete('/python-example-bdb32/Students/',<token>)
print('Record Deleted')

# data to save
data = {
    "name": "Joe Tilsed"
}

# Pass the user's idToken to the push method

data = {"name": "Joe Tilsed"}
try:
	db.child("users").push(data)
except requests.exceptions.ConnectionError:
    requests.status_code = "Connection refused"
    print(requests.status_code)



