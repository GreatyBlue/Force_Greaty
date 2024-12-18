import hashlib
import itertools
import string
import os

# Function to perform a dictionary attack
def dictionary_attack(hash_to_crack, wordlist_path, hash_method):
    try:
        with open(wordlist_path, 'r') as wordlist:
            for word in wordlist:
                word = word.strip()
                hashed_word = hash_method(word.encode('utf-8')).hexdigest()
                if hashed_word == hash_to_crack:
                    print(f"Password found: {word}")
                    return word
        print("Password not found in wordlist.")
        return None
    except FileNotFoundError:
        print(f"Error: Wordlist file '{wordlist_path}' not found.")
        return None

# Function to perform a brute-force attack
def brute_force_attack(hash_to_crack, hash_method):
    chars = string.ascii_lowercase + string.digits  # Characters to use in brute-force
    for length in range(1, 5):  # Try passwords from length 1 to 4
        for password in itertools.product(chars, repeat=length):
            password = ''.join(password)
            hashed_password = hash_method(password.encode('utf-8')).hexdigest()
            if hashed_password == hash_to_crack:
                print(f"Password found: {password}")
                return password
    print("Password not found using brute-force.")
    return None

# Main function to initiate the password cracking tool
def crack_password():
    print("\nWelcome to your Custom Password Cracker Tool!")
    
    # Ask user for the type of attack
    attack_type = input("Choose attack type (1: Dictionary, 2: Brute-force): ")

    # Choose hash method (default: SHA-256)
    hash_method = hashlib.sha256
    
    if attack_type == '1':
        # Dictionary attack
        hash_to_crack = input("Enter the hash to crack: ")
        wordlist_path = input("Enter the path to the wordlist: ")
        dictionary_attack(hash_to_crack, wordlist_path, hash_method)
    elif attack_type == '2':
        # Brute-force attack
        hash_to_crack = input("Enter the hash to crack: ")
        brute_force_attack(hash_to_crack, hash_method)
    else:
        print("Invalid option. Please choose 1 or 2.")

# Function to display help message
def display_help():
    print("""
    Custom Password Cracker Tool by GreatyBlue
    Usage:
    python cracker.py --crack <hash-to-crack> --method <attack-method> --wordlist <wordlist-path>
    
    Available attack methods:
    --method dictionary     : Use a wordlist for cracking (dictionary attack)
    --method brute-force    : Use brute-force for cracking (brute-force attack)
    
    Example:
    python cracker.py --crack <hash> --method dictionary --wordlist /path/to/wordlist.txt
    """)

# Main Command Line Interface (CLI) for the tool
def main():
    # Check if user provided a command line argument
    if len(os.sys.argv) > 1:
        if '--help' in os.sys.argv:
            display_help()
        elif '--crack' in os.sys.argv:
            try:
                hash_to_crack = os.sys.argv[os.sys.argv.index('--crack') + 1]
                method = os.sys.argv[os.sys.argv.index('--method') + 1]
                
                if method == 'dictionary':
                    wordlist_path = os.sys.argv[os.sys.argv.index('--wordlist') + 1]
                    dictionary_attack(hash_to_crack, wordlist_path, hashlib.sha256)
                elif method == 'brute-force':
                    brute_force_attack(hash_to_crack, hashlib.sha256)
                else:
                    print("Invalid method. Use 'dictionary' or 'brute-force'.")
            except IndexError:
                print("Error: Missing arguments. Use --help to see usage.")
        else:
            print("Invalid command. Use --help for guidance.")
    else:
        crack_password()

if __name__ == "__main__":
    main()
