import os
import subprocess
import sys
import getpass
import users
import crypt

# runner to allow the creation of 30 accounts


class main:

    passwords = []
    usernames = []

    # Read the passwords from the text file only from lines 1-30 and store them in an array

    def read_passwords():
        file_path = "CommonPasswords"
        passwords = []
        i = 0

        # specify the lines that will be read in the text file
        lines = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                 16, 17, 28, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

        with open(file_path, "r+") as file:

            while True:
                line = file.readline()

                if i in lines:
                    passwords.append(line.strip())

                if i > lines[-1]:
                    break
                i += 1

        file.close()
        return passwords

    # creating user1 through user29 and storing them in a list
    def create_usernames():
        accounts = []
        i = 0
        while i != 30:

            name = "user"+str(i)
            accounts.append(name)
            i += 1
        return accounts

    # store usernames and passwords in arrays to create the accounts
    passwords = read_passwords()
    usernames = create_usernames()

    accounts = []

    # Create the accounts with the usernames and passwords by using the users class and to return a list of accounts
    def create_account(usernames, passwords):
        count = 0
        account_list = []

        for i in range(len(usernames)):
            account = users.accounts(usernames[i], passwords[i])
            account_list.append(account)

        return account_list

    # store account information in an array
    accounts = create_account(usernames, passwords)

    # script to add user0 to user29 in to the command line

    def add_user(accounts):
        hashed_passwords = []
        for i in range(len(accounts)):
            username = accounts[i].getUsername()
            password = accounts[i].getPassword()

            encrypted_p = crypt.crypt(password)
            print(encrypted_p)

            hashed_passwords = encrypted_p

            subprocess.run(["sudo", "useradd", "-p", encrypted_p, username])

        return hashed_passwords

    # add_user(accounts)

    # to delete all the users if its needed

    def delete_user(accounts):
        for i in range(len(accounts)):
            username = accounts[i].getUsername()
            password = accounts[i].getPassword()

            os.system("sudo deluser --remove-home "+username)

    # delete_user(accounts)
