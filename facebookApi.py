
from scraping import Scraping as fs
from backup import backup
from generate_passwords import generate_passwords

URL = ("https://www.facebook.com/zuck")

profile = fs.scraping(URL)
# profile = backup()._profile
# backup(profile)
generate_passwords(profile)
#email = input("Insert your email: ")


