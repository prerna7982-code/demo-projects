from firebase import Firebase
import requests
from getpass import getpass
from credentials imort *

config = credentials

firebase = Firebase(config)
auth = firebase.auth()

email = input("Please Enter Your Email Address : \n")
password = getpass("Please Enter Your Password : \n")


#create_user
user = auth.create_user_with_email_and_password(email, password)
print("Successfully created user.... ")

#user_login
login_user = auth.sign_in_with_email_and_password(email, password)
print("login successfull")

#email_verification
auth.send_email_verification(login_user['idToken'])

#reset the password
auth.send_password_reset_email(email)
 
print("Success ... ")


db = firebase.database()

users = db.child("users").get()
print(users.val())

#all users
for user in users.each():
	print(users.val())
	print(users.key())

#firebase_storage

storage = firebase.storage()

image = input("Please Enter image location : \n")

storage.child("images/newimage.png").put(image)
print("image_uploaded")
user_id_token = ''
print(storage.child("images/frog.png").get_url(token= user_idtoken))
