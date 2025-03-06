import random
import time
import string
import pyperclip
from cryptography.fernet import Fernet
import sqlite3
import hashlib
import requests
import sys


key = Fernet.generate_key()
cipher = Fernet(key)

with open("secret.key", "wb") as key_file:
    key_file.write(key)
conn = sqlite3.connect('passwords.db')
# def

def check_pwned_password(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    first5, rest = sha1_password[:5], sha1_password[5:]
            


    url = f"https://api.pwnedpasswords.com/range/{first5}"
    response = requests.get(url)
    
    if response.status_code == 200:
        hashes = response.text.splitlines()
        for line in hashes:
            hash_suffix, count = line.split(":")
            if hash_suffix == rest:
                print(f"Password found in {count} breaches!")
                return True
                break
        print("Password is not in known breaches.")
        return False
    else:
        print("ERROR Checking Password")
        return False


def checkpass(password):
    score = 0
    time.sleep(0.3)
    print("-----STARTING SECURITY EXAM------")  
    print("\n")  
    if len(password) < 8:
        print ("(🔴) your password is less than 8 characters")
    time.sleep(0.3)
    print("\n")    
    if len(password) == 8 or len(password) > 8:
        print ("(🟢) your password is equal to or more than 8 characters")
        score += 1
        time.sleep(0.3)
        print("\n")  
    if any(char.isalpha() for char in password):
        print ("(🟢) your password has letters")
        score += 1
        time.sleep(0.3)
        print("\n")  
    else:
        print ("(🔴) your password has no letters")
        time.sleep(0.3)
        print("\n")  
    if any(char.islower() for char in password):
        print ("(🟢) your password has lowercase letters")
        score += 1
        time.sleep(0.3)
        print("  \n")  
    else:
        print ("(🔴) your password has no lowercase letters")
        time.sleep(0.3)
        print("\n")  
    if any(char.isupper() for char in password):
        print ("(🟢) your password has an uppercase letter")
        score += 1
        time.sleep(0.3)
        print("\n")  
    else:
        print ("(🔴) your password has no uppercase letter")
        time.sleep(0.3)
        print("\n")  
    if any(char.isdigit() for char in password):
        print ("(🟢) your password has a digit")
        score += 1
        time.sleep(0.3)
        print("\n")  
    else:
        print ("(🔴) your password has no digit")
        time.sleep(0.3)
        print("\n")  

    if any(char in string.punctuation for char in password):
        print ("(🟢) your password has symbols")
        score += 1
        time.sleep(1)
    else:
        print ("(🔴) your password has no symbols\n")
        time.sleep(1)
    print("Progress: ")
    print("=" * score)
    print(f"\nYou got a score of {score}/6")
    print("Progress:") + ("=" * (score))
    if score in [0, 1, 2]:
        print("Very Weak 🔴\n")
    elif score in [3, 4]:
        print("Moderate 🟡\n")
    elif score in [5, 6]:
        print("Strong 🟢\n")

        print("\n")
        print("Test Completed")
        print("\n")
            
def askexit():
                password = input("What's your Password?\n")
                if exitO == 'y':
                    check_pwned_password(password)
                    password = input("What's your Password?\n")
                    check_pwned_password(password)
                elif exitO == 'n':
                    print("LOADING.")
                    print("LOADING..")
                    print("LOADING...")
        # WHILE TRUE 
        
while True:
    choice = input(f"---------------------------------------------------------------------------\n1. Password Generator         4. Have I Been Pwned? \n2. Password Strength Test            5. \n3. Decrypt Password           99. Exit\n---------------------------------------------------------------------------\n")
    if choice == '1':
            askdigit = input("Do you want digits in your password? (y/n) \n")
            asksymbol = input("Do you want a symbols in your password? (y/n) \n")
            askupper = input("Do you want a uppercase letters in your password? (y/n) \n")
            password = []
            characters = ""
            encryptpass = input("Do you want your password to be encrypted and saved to the file? (y/n)\n")
            if askdigit == 'y':
                characters += string.digits.replace("0", "")
            if asksymbol == 'y':
                characters += string.punctuation
            if askupper == "y":
                characters += string.ascii_uppercase
            if characters == "":
                characters += string.ascii_letters 
            length = int(input("What's the length of your needed password? \n"))
            for i in range(length):
                password.append(random.choice(characters))
            password = "".join(password)
            seepass = input("Do you want to see the password? (y/n)\n")
            if seepass == 'y':
                print(f"Here is your desired password:\n{password}")
                password = []
                regen = input(' 🔄️ Regenerate Password? (y/n):')
                if regen == 'y':
                    for i in range(length):
                        password.append(random.choice(characters))
                    password = "".join(password)
                    print(password)
            
                pyperclip.copy(password)
                print("Password copied to clipboard!")

            elif seepass == 'n':
                file_path = "Password.txt"
                with open(file_path, 'a') as file:
                    file.write(f"{password}\n")
            retrivepass = input("Do you want to see saved passwords (y/n)\n")
            if retrivepass == 'y':
                with open("Password.txt", "r") as file:
                    content = file.read()
                    print(content)
            if encryptpass == "y":
                encryptedpass = cipher.encrypt(password.encode())
                with open("Password.txt", "ab") as file:
                    file.write(encryptedpass + b'\n')
                print(f"Your password has been added to Password.txt,\nRemember this key to decrypt it later:\n{key.decode()}")
            else:
                    continue
    elif choice == '2':
            password_to_check = input("What password do you want to check?\n")
            checkpass(password_to_check)
    elif choice == '3':
            decryptpass  = input("Enter the encrypted password to decrypt:\n").encode()
            try:
                key_input = input("Enter the key to decrypt the password:\n").encode()
                cipher = Fernet(key_input)
                decryptedpass = cipher.decrypt(decryptpass).decode()
                print(f"Decrypted password: {decryptedpass}")
            except Exception as e:
                print(f"An error occurred: {e}")
    elif choice == '4':
            password = input("What's your Password?\n")
            check_pwned_password(password)
            exitO = input("retry? (y/n)\n")
            askexit()
    elif choice == '99':
        sys.exit()