# Password Validator

The objective of this project is to validate the user passwords and alert him if these passwords are weak. The user inserts the URL of his Facebook profile, answers some questions and this software will analyze it. With this info, a wordlist of the possible weak passwords will be generated. The user can insert the password he wishes and if it's in this wordlist it means that the password is weak.

# Scraping

First of all the user should insert the URL of his Facebook profile. The Validator will scrap this link, looking for and listing any public info useful as names, address, graduation, movies, sports, etc.

# Password generator

The list of likes and profile info as names and birthdays will be combined and generates a wordlist of the possible passwords, combining keywords, dates and other relevant info caught by scraping.

# Validating

Finishing, the user could insert any password and if it is in the wordlist that isn't a good password.

# Usage

* Create a virtualenv in the project folder e.g., "venv".
```
    source venv / Scripts / activate
    pip install - r requirements.txt
    python main.py
```
* In the beginning the user should insert the URL of a Facebook profile, using pt-br. E.g: https://pt-br.facebook.com/SomeName
* If the user decides to not use a Facebook profile, he can skip and insert his name.
* The software will make some questions, and the user can skip pressing 'Enter'.
* After the user can choose to generate a wordlist of weak passwords or validate a password.
* If a wordlist was been created will be necessary to close the software using option 3, that will delete the wordlist created.

# Requirements

* [Python 3.7+](https://www.python.org/downloads/)
* [Python pip](https://pip.pypa.io/en/stable/installing/)
* [Virtualenv](https://virtualenv.pypa.io/en/latest/)
