# PasswordLeakChecker

**PasswordLeakChecker** is a Python tool that checks if your passwords have been compromised in known data breaches using the "Have I Been Pwned" API. It securely hashes passwords locally and generates a detailed compromise report.

## Features

- Check if passwords have been compromised by querying the "Have I Been Pwned" API.
- Securely hash passwords locally using SHA-1.
- Generate a report indicating which passwords have been compromised.

## Prerequisites

- Python 3.7 or higher

## Installation

1. Clone the GitHub repository:

    ```bash
    git clone https://github.com/Titzn/PasswordLeakChecker.git
    cd PasswordLeakChecker
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    ```

    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```

    - On macOS and Linux:
        ```bash
        source env/bin/activate
        ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the main script with Python, providing a list of passwords to check:

    ```bash
    python main.py --passwords "password1,password2,password3"
    ```

### Example

To check the passwords "123456" and "password":

    ```bash
    python main.py --passwords "123456,password"
    ```

## Testing

To run the unit tests, use:

    ```bash
    python -m unittest discover tests
    ```

## Contribution

Contributions are welcome! Please open an issue to discuss any changes you would like to make. Pull requests are also welcome.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
