import sqlite3
    
users = {}

user_input = ""
password = ""

while user_input != "done":
    print("Welcome to the registration system!\n")
    user_input = input("Please enter the username you wish to use to register:   ")
    password = input("Please enter the password that you would like to use:     ")

    users[user_input] = password

    user_input = input("Would you like to add another user?      ")
    if user_input == "no":
        break
    elif user_input == "yes":
        continue
for user, password in users.items():
    print(f"The user: {user}    password:   {password}")


with sqlite3.connect("db.sqlite3") as connection:
    command = "INSERT INTO users VALUES(?, ?)"
    for user, password in users.items():
        user_credentials = [user, password]
        connection.execute(command, tuple(user_credentials))

    connection.commit()
