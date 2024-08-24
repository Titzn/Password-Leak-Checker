import argparse
from check_password import check_passwords

def parse_arguments():
    parser = argparse.ArgumentParser(description="Check if your passwords have been compromised.")
    parser.add_argument("--passwords", type=str, required=True, help="Comma-separated list of passwords to check.")
    return parser.parse_args()

def display_results(results):
    print("\n--- Password Compromise Report ---\n")
    for password, status in results.items():
        if status is None:
            print(f"Error checking the password '{password}'.")
        elif status:
            print(f"The password '{password}' has been compromised.")
        else:
            print(f"The password '{password}' is safe.")

def main():
    args = parse_arguments()
    passwords = args.passwords.split(',')
    
    try:
        results = check_passwords(passwords)
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    display_results(results)

if __name__ == "__main__":
    main()
