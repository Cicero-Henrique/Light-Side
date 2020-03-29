
# from facebook_scraping import facebook_scraping as fs
# from cupp import cupp
from backup import backup
from generate_passwords import generate_passwords

URL = ("https://www.facebook.com/zuck")

# profile = fs.scraping(URL)
#cupp(profile)
profile = backup()._profile
# backup(profile)
generate_passwords(profile)
#email = input("Insert your email: ")


