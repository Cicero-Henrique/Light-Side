
from facebook_scraping import facebook_scraping as fs
from cupp import cupp
from test_facebook_api import backup as backup

URL = ("https://www.facebook.com/zuck")

profile = fs.scraping(URL)
#cupp(profile)
backup(profile)
#email = input("Insert your email: ")


