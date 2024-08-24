import requests
from utils.hash_util import hash_password

API_URL = "https://api.pwnedpasswords.com/range/"

def check_passwords(passwords):
    compromised_status = {}
    
    for password in passwords:
        hashed_password = hash_password(password)
        prefix = hashed_password[:5]
        suffix = hashed_password[5:]

        try:
            response = requests.get(f"{API_URL}{prefix}", timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error contacting the API for password '{password}': {e}")
            compromised_status[password] = None
            continue

        hashes = (line.split(':') for line in response.text.splitlines())
        compromised = any(suffix.upper() == hash_suffix for hash_suffix, _ in hashes)
        compromised_status[password] = compromised

    return compromised_status
