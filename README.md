# Password-Tool
This Python-based password tool lets you generate customizable secure passwords, test their strength, encrypt and store them, and even check if they've been compromised using the Have I Been Pwned API. It's a handy utility for basic cybersecurity and password management.


# LONG VERSION:
This password tool is a multi-functional utility designed to help users generate secure passwords, assess their strength, encrypt and store them, and even check if a password has been compromised in known data breaches. The script combines several Python libraries and functionalities into one interactive command-line interface, making it both a learning project and a practical tool for basic password management.

The tool begins by generating a new encryption key using the Fernet module from the cryptography library. This key is then saved to a file called secret.key, ensuring that any encrypted passwords can later be decrypted if needed. Simultaneously, the script establishes a connection to a SQLite database (passwords.db), which is intended for storing passwords, although its functionality isn’t fully implemented in the current version.

One of the main features of the tool is its password generator. Users are prompted to specify if they want their password to include digits (with 0 excluded), symbols, and uppercase letters. If no specific characters are chosen, the generator defaults to using all ASCII letters. The generator then creates a password of user-defined length by randomly picking characters from the selected set. Additionally, users have the option to view the generated password, regenerate it if they’re not satisfied, or have it copied to the clipboard using the pyperclip module. There is also an option to save the generated password to a file, and if the user chooses, to encrypt the password before saving it, adding an extra layer of security.

In addition to generating passwords, the tool includes a password strength tester. This feature evaluates the strength of a user-provided password by checking if it meets several criteria: minimum length, the presence of letters (including both uppercase and lowercase), digits, and symbols. The tester assigns a score out of six based on these criteria, then displays a progress bar along with a qualitative assessment ranging from "Very Weak" to "Strong." This immediate feedback helps users understand how secure their passwords are and what improvements might be needed.

Another critical component is the decryption feature. If a user has an encrypted password, they can input the ciphertext along with the corresponding key to decrypt and reveal the original password. The script uses the provided key to reinitialize the Fernet cipher and attempts decryption, handling any errors gracefully by outputting a helpful message if the decryption process fails.

The tool also integrates with the Have I Been Pwned API to check if a password has been exposed in any data breaches. Before making the API call, the password is hashed using SHA1, and only the first five characters of the hash are sent to the API. This design helps maintain privacy by ensuring that the full password is never exposed. The tool then processes the API response to see if the remainder of the hash appears among the returned hashes, alerting the user if the password has been found in any breaches.

An interactive menu ties all these features together, presenting users with clear options to generate a password, test its strength, decrypt an encrypted password, or check a password against known breaches. This looped menu system makes it easy for users to continuously work with the tool without needing to restart it for each new task.

Overall, this password tool is an excellent example of how to integrate multiple functionalities into one Python script. It not only covers essential aspects of password management—such as secure generation, strength evaluation, encryption, and breach checking—but also demonstrates the use of various libraries and APIs. This makes it a valuable project for anyone looking to deepen their understanding of Python programming and basic cybersecurity practices.
