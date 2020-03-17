
from facebook_scraping import facebook_scraping as fs
from cupp.cupp import cupp

URL = ("https://www.facebook.com/zuck")

profile = fs.scraping(URL)
cupp(profile)

email = input("Insert your email: ")


