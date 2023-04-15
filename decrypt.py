import crypt
import controller
import users


class password_cracker:
    username = []
    hashed_passwords = []
    salt_num = []
    saltH = []

    # using the controller class to obtain the passwords from common_passwords.txt
    original_passwords = controller.main.read_passwords()

    # this method will read the hashed passwords originating from the shadow file which are copied over in a text file
    # If the text file and shadow file don't match update the txt file.
    def read_hashed():
        file_path = "hashed_passwords"

        # username
        name = []
        # password_hash
        hashed_password = []
        # salt algorithm
        salt_num = []
        # salt hash
        saltH = []

        i = 0
        j = 0

        with open(file_path, "r+") as file:

            # this for loop will be in charge of splitting the entire hashed password into 4 seperate sections
            for i in range(30):
                line = file.readline()
                username, raw_hash = line.split(':', 1)
                empty, salt_number, salt_hash, password_hash = raw_hash.split(
                    '$', 4)

                name.append(username)
                salt_num.append(salt_number)
                saltH.append(salt_hash)
                hashed_password.append(password_hash)
            file.close()
            return name, salt_num, saltH, hashed_password

    username, salt_num, saltH, hashed_password = read_hashed()

    # this method will try a brute force attack to decrypt the shadow file password (WORK IN PROGRESS)
    def password_decrypt(original_passwords, username, salt_num, saltH, hashed_passwords):
        i = 0
        x = 0
        incorrect_hashes = []

        while i != 1:
            hashed_p = crypt.crypt(original_passwords[i], crypt.METHOD_SHA512)
            fully_hashed = hashed_p + "/:19251:0:99999:7:::"

           # splitting the hashed password into that was produced from common_password.txt
            empty, new_salt_number, new_salt_hash, new_password_hash = fully_hashed.split(
                '$', 4)

            # checking if the shadow file salt hash matches to the salt hash from the common_password.txt password
            if saltH[i] == new_salt_hash:
                print(username, "SALT HASH MATCHED!")
                while j != 1:
                    # checking if the hashed password matches from the common_password.txt password
                    if hashed_passwords[j] == new_password_hash:
                        print(
                            "FOUND a match for ", username[i], new_salt_number, new_salt_hash, new_password_hash)
                        print(incorrect_hashes)
                        j += 1
                        i += 1
                    print("password is no match")

            print(username[i], "no match,retrying")
            incorrect_hashes = new_salt_hash
            x += 1

    password_decrypt(original_passwords, username,
                     salt_num, saltH, hashed_passwords)

    # possible Idea would be to create a list to store all the incorrect salt hashes and salt passwords then compare them to avoid repitition
    # but may encounter performance issues when running this lab
