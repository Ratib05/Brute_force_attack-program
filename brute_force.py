# allows program to use hashing algorithms
import hashlib

#allows program to work with regular expressions
import re

# Asks the user to input the word or hash that they want to check out
target = input("Enter word or hash to check: ")

wordlist = "C:\\Users\\ratib\\Desktop\\python_scripts\\wordlist.txt"

# Asks the user to input the hashing algorithm they want
hash_algorithm = input("Choose hash algorithm. sha256 or md5: ")

# This function checks if the value input by the user is a hash or a normal word
def is_hashed(target_word):
    if re.fullmatch(r'[0-9a-fA-F]+', target_word) and len(target_word) == 64 or len(target_word) == 32:
        return True
    else:
        return False

# This is the main function. It takes input value, the path of the wordlist and sets a default hash algorithm for the program to use
def brute_force_attack(target_word, wordlist_path, hash_algorithm="md5"):
    
    # The following two lines take the output from the is_hashed function and use it to decide if the target word has to be hashed
    # If the input from the user is a hash value, then - 
    if is_hashed(target_word):
        target_hashed = target_word

    # If the input from the user isn't a hash value
    else:
        if hash_algorithm == "md5":
            
            # Hashes the input word using the specified algorithm
            target_hashed = hashlib.md5(target.encode()).hexdigest()
        elif hash_algorithm == "sha256":
            target_hashed = hashlib.sha256(target.encode()).hexdigest()

    # Opens the wordlist.txt file as "read", encoded using utf-8 and referenced in the code as "wordlist"
    with open(wordlist_path, "r", encoding="utf-8") as wordlist:
        
        # Goes through the file of words
        for word in wordlist:
            
            # Cleans the word of useless stuff
            word = word.strip()
            
            # Hashes the word based on the specified algorithm
            if hash_algorithm == "md5":
                hashed_word = hashlib.md5(word.encode()).hexdigest()
            elif hash_algorithm == "sha256":
                hashed_word = hashlib.sha256(word.encode()).hexdigest()
            else:
                print("unsupported hashing algorithm")
                return
            
            # Prints input word, the hash of the word in the list (if found) and the hash of the input word
            print(f"{word}, {hashed_word} and {target_hashed}")

            # Prints if the input word's hash was found in the list
            if target_hashed == hashed_word:
                print(f"Target found in list: {target}")
                return

        # Prints if the input word's hash was found in the list
        print(f"Target not found in list: {target}")

# Calls the function with arguments: input value, wordlist path and a hash algorithm
brute_force_attack(target, wordlist, "md5")