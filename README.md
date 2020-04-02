# Password Validator

The objective of this project is to validate the user passwords and alert him if these passwords are weak. The user inserts the URL of his Facebook profile, answers some questions and this software will analyze it. With this info, a wordlist of the possibles weak passwords will be generated. The user can insert the password he wishes and if it's in this wordlist it means that the password is weak.

# Steps

- [x] Scraping
- [X] Password generator
- [ ] Validating

# Scraping

First of all the user should insert the URL of his Facebook profile. The Validator will make a web scraping in this link, looking for and list any public info useful as names, address, graduation, movies, sports, etc. Some libraries are necessary to do the scraping, they are:

* mechanize
* requests
* bs4
* pandas

# Password generator

The list of likes and profile info as names and birthdays will be combined and generates a wordlist of the possibles passwords, combining keywords, dates and other relevant info caught by scraping.

# Validating

Finishing, the user could insert any password and if it is in the wordlist that isn't a good password.

# Requirements

 * [Python 3.7 or best](https://www.python.org/downloads/)
 * [Python pip](https://pip.pypa.io/en/stable/installing/)
 * [Virtualenv](https://virtualenv.pypa.io/en/latest/)

# Usage

 * Create a virtualenv in the project folder e.g., "venv".
 * Run `source venv/Scripts/activate`
 * Run `pip install -r requirements.txt`
 * Run `python facebookApi.py`
