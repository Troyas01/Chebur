from dataset import users, countries
from pprint import pprint

users_wrong_password = []


for user in users:
    if 'password' in user:
        users_wrong_password.append(user['password'])
    if 'mail' in user:
        users_wrong_password.append(user['mail'])
print(users_wrong_password) 
      

        


